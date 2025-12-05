import { app } from "/scripts/app.js";

// Pure frontend Set/Get Variable nodes - based on KJNodes pattern
const LGraphNode = LiteGraph.LGraphNode;

// Shared storage for variables (persists during session)
const variableStorage = {};

app.registerExtension({
    name: "SimpleVariables.Set",
    registerCustomNodes() {
        class SimpleSetNode extends LGraphNode {
            constructor(title) {
                super(title);
                const node = this;

                this.properties = { variableName: "" };

                this.addWidget("text", "name", "", (value) => {
                    node.properties.variableName = value;
                    node.title = value ? `Set: ${value}` : "SimpleSet";
                });

                this.addInput("value", "*");
                this.addOutput("value", "*");

                this.onConnectionsChange = function(slotType, slot, isConnect, linkInfo) {
                    if (slotType === 1 && node.inputs[0]) {
                        if (isConnect) {
                            const link = node.graph?.links?.[node.inputs[0].link];
                            if (link) {
                                const originNode = node.graph._nodes_by_id[link.origin_id];
                                if (originNode?.outputs?.[link.origin_slot]) {
                                    const type = originNode.outputs[link.origin_slot].type;
                                    node.inputs[0].type = type;
                                    node.inputs[0].name = type;
                                    node.outputs[0].type = type;
                                    node.outputs[0].name = type;
                                }
                            }
                        } else {
                            node.inputs[0].type = "*";
                            node.inputs[0].name = "value";
                            node.outputs[0].type = "*";
                            node.outputs[0].name = "value";
                        }
                    }
                };

                this.isVirtualNode = true;
            }
        }

        LiteGraph.registerNodeType("SimpleSet", Object.assign(SimpleSetNode, {
            title: "SimpleSet",
        }));
        SimpleSetNode.category = "SimpleVariables";
    }
});

app.registerExtension({
    name: "SimpleVariables.Get",
    registerCustomNodes() {
        class SimpleGetNode extends LGraphNode {
            constructor(title) {
                super(title);
                const node = this;

                this.properties = { variableName: "" };

                this.addWidget("combo", "name", "", (value) => {
                    node.properties.variableName = value;
                    node.title = value ? `Get: ${value}` : "SimpleGet";
                    node.syncType();
                }, {
                    values: () => {
                        if (!node.graph?._nodes) return [""];
                        const names = node.graph._nodes
                            .filter(n => n.type === "SimpleSet")
                            .map(n => n.properties?.variableName || n.widgets?.[0]?.value || "")
                            .filter(n => n !== "");
                        return ["", ...names.sort()];
                    }
                });

                this.addOutput("value", "*");
                this.isVirtualNode = true;
            }

            syncType() {
                const setter = this.findSetter();
                if (setter?.inputs?.[0]) {
                    this.outputs[0].type = setter.inputs[0].type || "*";
                    this.outputs[0].name = setter.inputs[0].name || "value";
                } else {
                    this.outputs[0].type = "*";
                    this.outputs[0].name = "value";
                }
            }

            findSetter() {
                if (!this.graph || !this.properties.variableName) return null;
                return this.graph._nodes.find(n =>
                    n.type === "SimpleSet" &&
                    (n.properties?.variableName === this.properties.variableName ||
                     n.widgets?.[0]?.value === this.properties.variableName)
                );
            }

            getInputLink(slot) {
                const setter = this.findSetter();
                if (setter?.inputs?.[0]?.link != null) {
                    return this.graph.links[setter.inputs[0].link];
                }
                return null;
            }
        }

        LiteGraph.registerNodeType("SimpleGet", Object.assign(SimpleGetNode, {
            title: "SimpleGet",
        }));
        SimpleGetNode.category = "SimpleVariables";
    }
});

app.registerExtension({
    name: "SimpleVariables.List",
    registerCustomNodes() {
        class SimpleListNode extends LGraphNode {
            constructor(title) {
                super(title);
                const node = this;

                this.addWidget("button", "Refresh", null, () => {
                    node.updateList();
                });

                this.addOutput("list", "STRING");
                this.isVirtualNode = true;
                this.size = [200, 100];
            }

            updateList() {
                if (!this.graph?._nodes) return;
                const setters = this.graph._nodes.filter(n => n.type === "SimpleSet");
                const names = setters
                    .map(n => n.properties?.variableName || n.widgets?.[0]?.value || "")
                    .filter(n => n !== "");

                // Update title to show variables
                if (names.length === 0) {
                    this.title = "SimpleList (empty)";
                } else {
                    this.title = "SimpleList:\n" + names.join("\n");
                }
            }

            onAdded() {
                this.updateList();
            }
        }

        LiteGraph.registerNodeType("SimpleList", Object.assign(SimpleListNode, {
            title: "SimpleList",
        }));
        SimpleListNode.category = "SimpleVariables";
    }
});

app.registerExtension({
    name: "SimpleVariables.Clear",
    registerCustomNodes() {
        class SimpleClearNode extends LGraphNode {
            constructor(title) {
                super(title);
                const node = this;

                this.addWidget("button", "Clear All Variables", null, () => {
                    if (!node.graph?._nodes) return;
                    const setters = node.graph._nodes.filter(n => n.type === "SimpleSet");
                    let count = 0;
                    setters.forEach(setter => {
                        if (setter.inputs?.[0]?.link != null) {
                            node.graph.removeLink(setter.inputs[0].link);
                            count++;
                        }
                    });
                    node.title = `SimpleClear (cleared ${count})`;
                });

                this.isVirtualNode = true;
            }
        }

        LiteGraph.registerNodeType("SimpleClear", Object.assign(SimpleClearNode, {
            title: "SimpleClear",
        }));
        SimpleClearNode.category = "SimpleVariables";
    }
});
