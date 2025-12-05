"""
SimpleVariables - Pure frontend Set/Get Variable nodes for ComfyUI

These nodes are implemented entirely in JavaScript (web/simplevariables.js).
They work by redirecting graph connections - no Python execution needed.
"""

# No Python nodes - everything is in JavaScript
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
