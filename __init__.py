"""
SimpleVariables - Set and Get nodes for storing/retrieving any data by name in ComfyUI
"""

# Global storage for variables
_variable_storage = {}


class SetVariable:
    """Store any data with a custom variable name"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "variable_name": ("STRING", {"default": "my_var"}),
            },
            "optional": {
                "value": ("*",),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
            }
        }
    RETURN_TYPES = ("*", "STRING",)
    RETURN_NAMES = ("value", "preview",)
    FUNCTION = "set_var"
    CATEGORY = "variables"
    OUTPUT_NODE = True

    def set_var(self, variable_name, unique_id=None, value=None):
        _variable_storage[variable_name] = value

        # Create preview string
        if value is None:
            preview = f"[{variable_name}] = None"
        else:
            type_name = type(value).__name__
            if hasattr(value, 'shape'):
                preview = f"[{variable_name}] = {type_name} {list(value.shape)}"
            elif isinstance(value, (str, int, float, bool)):
                val_str = str(value)[:50] + "..." if len(str(value)) > 50 else str(value)
                preview = f"[{variable_name}] = {val_str}"
            else:
                preview = f"[{variable_name}] = {type_name}"

        return (value, preview,)


class GetVariable:
    """Retrieve data by variable name"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "variable_name": ("STRING", {"default": "my_var"}),
            }
        }
    RETURN_TYPES = ("*", "STRING",)
    RETURN_NAMES = ("value", "preview",)
    FUNCTION = "get_var"
    CATEGORY = "variables"

    def get_var(self, variable_name):
        if variable_name not in _variable_storage:
            available = list(_variable_storage.keys())
            raise ValueError(f"Variable '{variable_name}' not found. Available: {available}")

        value = _variable_storage[variable_name]

        # Create preview string
        if value is None:
            preview = f"[{variable_name}] = None"
        else:
            type_name = type(value).__name__
            if hasattr(value, 'shape'):
                preview = f"[{variable_name}] = {type_name} {list(value.shape)}"
            elif isinstance(value, (str, int, float, bool)):
                val_str = str(value)[:50] + "..." if len(str(value)) > 50 else str(value)
                preview = f"[{variable_name}] = {val_str}"
            else:
                preview = f"[{variable_name}] = {type_name}"

        return (value, preview,)


class ListVariables:
    """Show all stored variables"""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("variable_list",)
    FUNCTION = "list_vars"
    CATEGORY = "variables"

    def list_vars(self):
        if not _variable_storage:
            return ("(no variables set)",)

        lines = []
        for name, value in _variable_storage.items():
            if value is None:
                lines.append(f"{name}: None")
            elif hasattr(value, 'shape'):
                lines.append(f"{name}: {type(value).__name__} {list(value.shape)}")
            elif isinstance(value, (str, int, float, bool)):
                val_str = str(value)[:30] + "..." if len(str(value)) > 30 else str(value)
                lines.append(f"{name}: {val_str}")
            else:
                lines.append(f"{name}: {type(value).__name__}")

        return ("\n".join(lines),)


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

    def clear_vars(self, clear):
        if clear:
            count = len(_variable_storage)
            _variable_storage.clear()
            return (f"Cleared {count} variable(s)",)
        return ("Not cleared (set clear=True)",)


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
