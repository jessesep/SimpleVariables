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

                this.properties = this.properties || {};
                this.properties.variableName = "";

                // Variable name widget
                this.addWidget("text", "name", "", (value) => {
                    this.properties.variableName = value;
                    this.title = value ? `Set: ${value}` : "Set Variable";
                    this.updateGetters();
                });

                // Input and passthrough output
                this.addInput("value", "*");
                this.addOutput("value", "*");

                this.onConnectionsChange = (slotType, slot, isConnect, linkInfo) => {
                    if (slotType === 1 && this.inputs[0]) { // Input changed
                        if (isConnect && linkInfo) {
                            const type = this.getInputType(0);
                            if (type) {
                                this.inputs[0].type = type;
                                this.inputs[0].name = type;
                                this.outputs[0].type = type;
                                this.outputs[0].name = type;
                            }
                        } else if (!isConnect) {
                            this.inputs[0].type = "*";
                            this.inputs[0].name = "value";
                            this.outputs[0].type = "*";
                            this.outputs[0].name = "value";
                        }
                        this.updateGetters();
                    }
                };

                this.isVirtualNode = true;
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
                this.graph._nodes.forEach(node => {
                    if (node.type === "GetVariableNode" && node.properties.variableName === name) {
                        node.syncWithSetter();
                    }
                });
            }

            onRemoved() {
                this.updateGetters();
            }
        }

        LiteGraph.registerNodeType("SetVariableNode", Object.assign(SetVariableNode, {
            title: "Set Variable",
        }));
        SetVariableNode.category = "variables";
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
                        if (!node.graph) return [""];
                        const setters = node.graph._nodes.filter(n => n.type === "SetVariableNode");
                        const names = setters
                            .map(n => n.properties?.variableName || n.widgets?.[0]?.value || "")
                            .filter(n => n !== "")
                            .sort();
                        return ["", ...names];
                    }
                });

                this.addOutput("value", "*");

                this.onConnectionsChange = () => {
                    this.validateLinks();
                };

                this.isVirtualNode = true;
            }

            findSetter() {
                if (!this.graph || !this.properties.variableName) return null;
                const name = this.properties.variableName;
                return this.graph._nodes.find(n =>
                    n.type === "SetVariableNode" &&
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
                // Remove incompatible links
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

        LiteGraph.registerNodeType("GetVariableNode", Object.assign(GetVariableNode, {
            title: "Get Variable",
        }));
        GetVariableNode.category = "variables";
    }
});
