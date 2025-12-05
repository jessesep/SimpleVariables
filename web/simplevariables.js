import { app } from "/scripts/app.js";

// Pure frontend Set/Get Variable nodes - no Python execution needed
// Based on KJNodes SetGet implementation

const LGraphNode = LiteGraph.LGraphNode;

app.registerExtension({
    name: "SimpleVariables.SetVariable",
    registerCustomNodes() {
        class SetVariableNode extends LGraphNode {
            constructor(title) {
                super(title);

                const node = this;

                this.properties = this.properties || {};
                this.properties.variableName = "";

                // Variable name widget
                this.addWidget("text", "name", "", (value) => {
                    node.properties.variableName = value;
                    node.title = value ? `Set: ${value}` : "Set Variable";
                    node.updateGetters();
                });

                // Input and passthrough output
                this.addInput("value", "*");
                this.addOutput("value", "*");

                this.onConnectionsChange = function(slotType, slot, isConnect, linkInfo) {
                    if (slotType === 1 && node.inputs[0]) { // Input changed
                        if (isConnect && linkInfo) {
                            const type = node.getInputType(0);
                            if (type) {
                                node.inputs[0].type = type;
                                node.inputs[0].name = type;
                                node.outputs[0].type = type;
                                node.outputs[0].name = type;
                            }
                        } else if (!isConnect) {
                            node.inputs[0].type = "*";
                            node.inputs[0].name = "value";
                            node.outputs[0].type = "*";
                            node.outputs[0].name = "value";
                        }
                        node.updateGetters();
                    }
                };

                this.isVirtualNode = true;

                console.log("[SimpleVariables] SetVariableNode created, type:", this.type);
            }

            getInputType(slot) {
                const link = this.getInputLink(slot);
                if (link) {
                    const originNode = this.graph._nodes_by_id[link.origin_id];
                    if (originNode && originNode.outputs[link.origin_slot]) {
                        return originNode.outputs[link.origin_slot].type;
                    }
                }
                return null;
            }

            updateGetters() {
                if (!this.graph) return;
                const name = this.properties.variableName;
                console.log("[SimpleVariables] Updating getters for:", name);
                this.graph._nodes.forEach(n => {
                    console.log("[SimpleVariables] Checking node:", n.type, n.properties?.variableName);
                    if (n.type === "SetVariableNode/variables" || n.type === "GetVariableNode/variables") {
                        console.log("[SimpleVariables] Found variable node");
                    }
                });
            }

            onRemoved() {
                this.updateGetters();
            }
        }

        LiteGraph.registerNodeType("SetVariableNode/variables", Object.assign(SetVariableNode, {
            title: "Set Variable",
        }));

        console.log("[SimpleVariables] SetVariableNode registered");
    }
});

app.registerExtension({
    name: "SimpleVariables.GetVariable",
    registerCustomNodes() {
        class GetVariableNode extends LGraphNode {
            constructor(title) {
                super(title);

                this.properties = this.properties || {};
                this.properties.variableName = "";

                const node = this;

                // Variable name dropdown (shows available setters)
                this.addWidget("combo", "name", "", (value) => {
                    node.properties.variableName = value;
                    node.title = value ? `Get: ${value}` : "Get Variable";
                    node.syncWithSetter();
                }, {
                    values: () => {
                        if (!node.graph) {
                            console.log("[SimpleVariables] No graph available");
                            return [""];
                        }
                        console.log("[SimpleVariables] Looking for setters in", node.graph._nodes.length, "nodes");
                        const setters = node.graph._nodes.filter(n => {
                            const isSet = n.type === "SetVariableNode/variables";
                            if (isSet) console.log("[SimpleVariables] Found setter:", n.properties?.variableName, n.widgets?.[0]?.value);
                            return isSet;
                        });
                        const names = setters
                            .map(n => n.properties?.variableName || n.widgets?.[0]?.value || "")
                            .filter(n => n !== "")
                            .sort();
                        console.log("[SimpleVariables] Available names:", names);
                        return ["", ...names];
                    }
                });

                this.addOutput("value", "*");

                this.onConnectionsChange = () => {
                    this.validateLinks();
                };

                this.isVirtualNode = true;

                console.log("[SimpleVariables] GetVariableNode created, type:", this.type);
            }

            findSetter() {
                if (!this.graph || !this.properties.variableName) return null;
                const name = this.properties.variableName;
                return this.graph._nodes.find(n =>
                    n.type === "SetVariableNode/variables" &&
                    (n.properties?.variableName === name || n.widgets?.[0]?.value === name)
                );
            }

            syncWithSetter() {
                const setter = this.findSetter();
                if (setter && setter.inputs[0]) {
                    this.outputs[0].type = setter.inputs[0].type || "*";
                    this.outputs[0].name = setter.inputs[0].name || "value";
                } else {
                    this.outputs[0].type = "*";
                    this.outputs[0].name = "value";
                }
                this.validateLinks();
            }

            validateLinks() {
                if (!this.outputs[0].links || this.outputs[0].type === "*") return;
                const linksToRemove = [];
                this.outputs[0].links.forEach(linkId => {
                    const link = this.graph.links[linkId];
                    if (link && link.type !== "*" && link.type !== this.outputs[0].type) {
                        linksToRemove.push(linkId);
                    }
                });
                linksToRemove.forEach(id => this.graph.removeLink(id));
            }

            // This is the magic - redirect to the setter's input
            getInputLink(slot) {
                const setter = this.findSetter();
                if (setter && setter.inputs[0]) {
                    return this.graph.links[setter.inputs[0].link];
                }
                return null;
            }

            onAdded() {
                this.syncWithSetter();
            }
        }

        LiteGraph.registerNodeType("GetVariableNode/variables", Object.assign(GetVariableNode, {
            title: "Get Variable",
        }));

        console.log("[SimpleVariables] GetVariableNode registered");
    }
});
