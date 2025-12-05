import { app } from "/scripts/app.js";
import { ComfyWidgets } from "/scripts/widgets.js";

// Display text on nodes when they execute
app.registerExtension({
    name: "SimpleVariables",

    beforeRegisterNodeDef(nodeType, nodeData, appInstance) {
        if (["SimpleSet", "SimpleGet", "SimpleList", "SimpleClear"].includes(nodeData.name)) {

            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function(message) {
                if (onExecuted) onExecuted.apply(this, arguments);

                if (message?.text) {
                    // Find or create display widget
                    let widget = this.widgets?.find(w => w.name === "_display");

                    if (!widget) {
                        widget = ComfyWidgets.STRING(this, "_display", [
                            "STRING", { multiline: true }
                        ], appInstance).widget;
                        widget.inputEl.readOnly = true;
                        widget.inputEl.style.opacity = "0.7";
                        widget.inputEl.style.fontFamily = "monospace";
                        widget.inputEl.style.fontSize = "12px";
                    }

                    const text = Array.isArray(message.text) ? message.text[0] : message.text;
                    widget.value = text || "";

                    // Resize node
                    requestAnimationFrame(() => {
                        const sz = this.computeSize();
                        if (sz[0] < this.size[0]) sz[0] = this.size[0];
                        if (sz[1] < this.size[1]) sz[1] = this.size[1];
                        this.onResize?.(sz);
                        appInstance.graph?.setDirtyCanvas(true, false);
                    });
                }
            };

            // Update title based on name
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function() {
                if (onNodeCreated) onNodeCreated.apply(this, arguments);

                const node = this;
                const nameWidget = this.widgets?.find(w => w.name === "name");
                if (nameWidget) {
                    const origCallback = nameWidget.callback;
                    nameWidget.callback = function(value) {
                        if (origCallback) origCallback.apply(this, arguments);
                        if (nodeData.name === "SimpleSet") {
                            node.title = value ? `Set: ${value}` : "SimpleSet";
                        } else if (nodeData.name === "SimpleGet") {
                            node.title = value ? `Get: ${value}` : "SimpleGet";
                        }
                    };
                }
            };
        }
    }
});
