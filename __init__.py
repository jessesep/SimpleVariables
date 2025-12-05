"""
SimpleVariables - Set/Get Variable nodes for ComfyUI
"""
import time


class AnyType(str):
    """Matches any type for ComfyUI type checking"""
    def __eq__(self, _):
        return True
    def __ne__(self, _):
        return False


ANY = AnyType("*")

# Global storage
_variables = {}


class SimpleSet:
    """Set a variable by name - stores value and passes through"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": "var"}),
            },
            "optional": {
                "value": (ANY,),
            }
        }
    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("value",)
    FUNCTION = "set_var"
    CATEGORY = "SimpleVariables"
    OUTPUT_NODE = True

    @classmethod
    def IS_CHANGED(cls, name, value=None):
        return time.time()

    def set_var(self, name, value=None):
        _variables[name] = value

        # Generate preview
        if value is None:
            preview = f"{name} = None"
        elif hasattr(value, 'shape'):
            preview = f"{name} = {type(value).__name__} {list(value.shape)}"
        elif isinstance(value, (int, float, bool)):
            preview = f"{name} = {value}"
        elif isinstance(value, str):
            preview = f'{name} = "{value[:30]}..."' if len(value) > 30 else f'{name} = "{value}"'
        else:
            preview = f"{name} = {type(value).__name__}"

        return {"ui": {"text": [preview]}, "result": (value,)}


class SimpleGet:
    """Get a variable by name"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": "var"}),
            },
            "optional": {
                "trigger": (ANY,),  # Connect to SimpleSet output for execution order
            }
        }
    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_var"
    CATEGORY = "SimpleVariables"
    OUTPUT_NODE = True

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return time.time()

    def get_var(self, name, trigger=None):
        value = _variables.get(name)

        # Generate preview
        if name not in _variables:
            preview = f"{name} = NOT SET"
        elif value is None:
            preview = f"{name} = None"
        elif hasattr(value, 'shape'):
            preview = f"{name} = {type(value).__name__} {list(value.shape)}"
        elif isinstance(value, (int, float, bool)):
            preview = f"{name} = {value}"
        elif isinstance(value, str):
            preview = f'{name} = "{value[:30]}..."' if len(value) > 30 else f'{name} = "{value}"'
        else:
            preview = f"{name} = {type(value).__name__}"

        return {"ui": {"text": [preview]}, "result": (value,)}


class SimpleList:
    """List all stored variables"""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("list",)
    FUNCTION = "list_vars"
    CATEGORY = "SimpleVariables"
    OUTPUT_NODE = True

    @classmethod
    def IS_CHANGED(cls):
        return time.time()

    def list_vars(self):
        if not _variables:
            text = "(no variables)"
        else:
            lines = [f"{k} = {type(v).__name__}" for k, v in _variables.items()]
            text = "\n".join(lines)
        return {"ui": {"text": [text]}, "result": (text,)}


class SimpleClear:
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
    CATEGORY = "SimpleVariables"
    OUTPUT_NODE = True

    def clear_vars(self, clear):
        if clear:
            count = len(_variables)
            _variables.clear()
            status = f"Cleared {count} variable(s)"
        else:
            status = "Set clear=True to clear"
        return {"ui": {"text": [status]}, "result": (status,)}


NODE_CLASS_MAPPINGS = {
    "SimpleSet": SimpleSet,
    "SimpleGet": SimpleGet,
    "SimpleList": SimpleList,
    "SimpleClear": SimpleClear,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleSet": "SimpleSet",
    "SimpleGet": "SimpleGet",
    "SimpleList": "SimpleList",
    "SimpleClear": "SimpleClear",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
