"""
SimpleVariables - Set/Get Variable nodes for ComfyUI
JavaScript handles the actual logic (virtual nodes), Python stubs make them appear in menus.
"""


class AnyType(str):
    """Matches any type for ComfyUI type checking"""
    def __eq__(self, _):
        return True
    def __ne__(self, _):
        return False


ANY = AnyType("*")


class SimpleSet:
    """Set a variable by name"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": ""}),
            },
            "optional": {
                "value": (ANY,),
            }
        }
    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("value",)
    FUNCTION = "passthrough"
    CATEGORY = "SimpleVariables"

    def passthrough(self, name, value=None):
        return (value,)


class SimpleGet:
    """Get a variable by name"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": ""}),
            }
        }
    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("value",)
    FUNCTION = "get"
    CATEGORY = "SimpleVariables"

    def get(self, name):
        return (None,)


NODE_CLASS_MAPPINGS = {
    "SimpleSet": SimpleSet,
    "SimpleGet": SimpleGet,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleSet": "SimpleSet",
    "SimpleGet": "SimpleGet",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
