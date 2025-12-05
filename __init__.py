"""
SimpleVariables - Set and Get nodes for storing/retrieving any data by name in ComfyUI
"""
import time


class AnyType(str):
    """A special type that bypasses ComfyUI's type checking - always matches any type."""
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False


# Create the any type instance
ANY = AnyType("*")

# Global storage for variables
_variable_storage = {}


def get_preview_text(variable_name, value):
    """Generate preview text for a value"""
    if value is None:
        return f"{variable_name} = None"

    type_name = type(value).__name__

    if hasattr(value, 'shape'):
        return f"{variable_name} = {type_name} {list(value.shape)}"
    elif isinstance(value, str):
        val_str = value[:50] + "..." if len(value) > 50 else value
        return f'{variable_name} = "{val_str}"'
    elif isinstance(value, (int, float, bool)):
        return f"{variable_name} = {value}"
    elif isinstance(value, list):
        return f"{variable_name} = list[{len(value)}]"
    elif isinstance(value, dict):
        return f"{variable_name} = dict[{len(value)} keys]"
    else:
        return f"{variable_name} = {type_name}"


class SetVariable:
    """Store any data with a custom variable name - shows preview on node"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "variable_name": ("STRING", {"default": "my_var"}),
            },
            "optional": {
                "value": (ANY,),
            }
        }
    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("value",)
    FUNCTION = "set_var"
    CATEGORY = "variables"
    OUTPUT_NODE = True

    @classmethod
    def IS_CHANGED(cls, variable_name, value=None):
        # Store the value during IS_CHANGED phase (runs before all node execution)
        # This ensures GetVariable nodes can find values even without trigger connection
        _variable_storage[variable_name] = value
        return time.time()

    def set_var(self, variable_name, value=None):
        _variable_storage[variable_name] = value
        preview = get_preview_text(variable_name, value)
        return {"ui": {"text": [preview]}, "result": (value,)}


class GetVariable:
    """Retrieve data by variable name - shows preview on node"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "variable_name": ("STRING", {"default": "my_var"}),
            }
        }
    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_var"
    CATEGORY = "variables"
    OUTPUT_NODE = True

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        # Always re-execute to get latest variable value
        return time.time()

    def get_var(self, variable_name):
        if variable_name not in _variable_storage:
            available = list(_variable_storage.keys())
            preview = f"{variable_name} = NOT SET (available: {available})"
            return {"ui": {"text": [preview]}, "result": (None,)}

        value = _variable_storage[variable_name]
        preview = get_preview_text(variable_name, value)
        return {"ui": {"text": [preview]}, "result": (value,)}


class ListVariables:
    """Show all stored variables on the node"""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("variable_list",)
    FUNCTION = "list_vars"
    CATEGORY = "variables"
    OUTPUT_NODE = True

    def list_vars(self):
        if not _variable_storage:
            text = "(no variables set)"
        else:
            lines = [get_preview_text(name, value) for name, value in _variable_storage.items()]
            text = "\n".join(lines)

        return {"ui": {"text": [text]}, "result": (text,)}


class ClearVariables:
    """Clear all stored variables"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "clear": ("BOOLEAN", {"default": False}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("status",)
    FUNCTION = "clear_vars"
    CATEGORY = "variables"
    OUTPUT_NODE = True

    def clear_vars(self, clear):
        if clear:
            count = len(_variable_storage)
            _variable_storage.clear()
            status = f"Cleared {count} variable(s)"
        else:
            status = "Not cleared (set clear=True)"

        return {"ui": {"text": [status]}, "result": (status,)}


NODE_CLASS_MAPPINGS = {
    "SetVariable": SetVariable,
    "GetVariable": GetVariable,
    "ListVariables": ListVariables,
    "ClearVariables": ClearVariables,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SetVariable": "Set Variable",
    "GetVariable": "Get Variable",
    "ListVariables": "List Variables",
    "ClearVariables": "Clear Variables",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
