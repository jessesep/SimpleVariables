import { app } from "/scripts/app.js";
import { ComfyWidgets } from "/scripts/widgets.js";

function displayText(nodeType, nodeData, appInstance) {
    const onExecutedOriginal = nodeType.prototype.onExecuted;
    nodeType.prototype.onExecuted = function (message) {
        onExecutedOriginal?.apply(this, arguments);

        if (message?.text) {
            // Find or create text widget
            let textWidget = this.widgets?.find(w => w.name === "display_text");

            if (!textWidget) {
                textWidget = ComfyWidgets.STRING(this, "display_text", [
                    "STRING", { multiline: true }
                ], appInstance).widget;
                textWidget.inputEl.readOnly = true;
                textWidget.inputEl.style.opacity = 0.7;
                textWidget.inputEl.style.fontFamily = "monospace";
            }

            // Get text from message
            let text = message.text;
            if (Array.isArray(text)) {
                text = text[0] || "";
            }
            textWidget.value = text;

            // Resize node to fit
            requestAnimationFrame(() => {
                const sz = this.computeSize();
                if (sz[0] < this.size[0]) sz[0] = this.size[0];
                if (sz[1] < this.size[1]) sz[1] = this.size[1];
                this.onResize?.(sz);
                appInstance.graph.setDirtyCanvas(true, false);
            });
        }
    };
}

app.registerExtension({
    name: "SimpleVariables",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (["SetVariable", "GetVariable", "ListVariables", "ClearVariables"].includes(nodeData.name)) {
            displayText(nodeType, nodeData, app);
        }
    },
});
