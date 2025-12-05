import { app } from "/scripts/app.js";

// Override Python nodes with virtual node behavior
app.registerExtension({
    name: "SimpleVariables",

    beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "SimpleSet") {
            // Make it a virtual node - passes data through without Python execution
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function() {
                if (onNodeCreated) onNodeCreated.apply(this, arguments);

                const node = this;
                this.isVirtualNode = true;

                // Update title when name changes
                const nameWidget = this.widgets?.find(w => w.name === "name");
                if (nameWidget) {
                    const origCallback = nameWidget.callback;
                    nameWidget.callback = function(value) {
                        if (origCallback) origCallback.apply(this, arguments);
                        node.title = value ? `Set: ${value}` : "SimpleSet";
                    };
                }

                // Update slot types when connection changes
                this.onConnectionsChange = function(slotType, slot, isConnect, linkInfo) {
                    if (slotType === 1 && node.inputs?.[0]) {
                        if (isConnect && node.graph) {
                            const link = node.graph.links?.[node.inputs[0].link];
                            if (link) {
                                const originNode = node.graph._nodes_by_id[link.origin_id];
                                if (originNode?.outputs?.[link.origin_slot]) {
                                    const type = originNode.outputs[link.origin_slot].type;
                                    node.inputs[0].type = type;
                                    node.inputs[0].name = type;
                                    if (node.outputs?.[0]) {
                                        node.outputs[0].type = type;
                                        node.outputs[0].name = type;
                                    }
                                }
                            }
                        } else {
                            node.inputs[0].type = "*";
                            node.inputs[0].name = "value";
                            if (node.outputs?.[0]) {
                                node.outputs[0].type = "*";
                                node.outputs[0].name = "value";
                            }
                        }
                    }
                };
            };
        }

        if (nodeData.name === "SimpleGet") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function() {
                if (onNodeCreated) onNodeCreated.apply(this, arguments);

                const node = this;
                this.isVirtualNode = true;

                // Replace name widget with combo that shows available setters
                const nameWidget = this.widgets?.find(w => w.name === "name");
                if (nameWidget) {
                    // Convert to combo widget
                    nameWidget.type = "combo";
                    nameWidget.options = {
                        values: () => {
                            if (!node.graph?._nodes) return [""];
                            const names = node.graph._nodes
                                .filter(n => n.type === "SimpleSet")
                                .map(n => n.widgets?.find(w => w.name === "name")?.value || "")
                                .filter(n => n !== "");
                            return ["", ...names.sort()];
                        }
                    };

                    const origCallback = nameWidget.callback;
                    nameWidget.callback = function(value) {
                        if (origCallback) origCallback.apply(this, arguments);
                        node.title = value ? `Get: ${value}` : "SimpleGet";
                        node.syncWithSetter();
                    };
                }

                this.syncWithSetter = function() {
                    const setter = this.findSetter();
                    if (setter?.inputs?.[0] && this.outputs?.[0]) {
                        this.outputs[0].type = setter.inputs[0].type || "*";
                        this.outputs[0].name = setter.inputs[0].name || "value";
                    } else if (this.outputs?.[0]) {
                        this.outputs[0].type = "*";
                        this.outputs[0].name = "value";
                    }
                };

                this.findSetter = function() {
                    if (!this.graph) return null;
                    const name = this.widgets?.find(w => w.name === "name")?.value;
                    if (!name) return null;
                    return this.graph._nodes.find(n =>
                        n.type === "SimpleSet" &&
                        n.widgets?.find(w => w.name === "name")?.value === name
                    );
                };

                // Override getInputLink to get data from setter
                this.getInputLink = function(slot) {
                    const setter = this.findSetter();
                    if (setter?.inputs?.[0]?.link != null) {
                        return this.graph.links[setter.inputs[0].link];
                    }
                    return null;
                };
            };
        }
    }
});
