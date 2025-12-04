"""
ComfyUI Simple Variables - Set and Get nodes for storing/retrieving any data by name
"""

# Global storage for variables
_variable_storage = {}


# ============== MAIN NODES ==============
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
            }
        }
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("value",)
    FUNCTION = "set_var"
    CATEGORY = "variables"

    def set_var(self, variable_name, value=None):
        _variable_storage[variable_name] = value
        return (value,)


class GetVariable:
    """Retrieve data by variable name"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "variable_name": ("STRING", {"default": "my_var"}),
            }
        }
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_var"
    CATEGORY = "variables"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found. Available: {list(_variable_storage.keys())}")


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
        var_list = "\n".join([f"{k}: {type(v).__name__}" for k, v in _variable_storage.items()])
        return (var_list if var_list else "(no variables set)",)


# ============== DEPRECATED TYPE-SPECIFIC NODES ==============
# These still work but Set/Get Variable handles all types

class SetImageVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"image": ("IMAGE",), "variable_name": ("STRING", {"default": "my_image"})}}
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "set_var"
    CATEGORY = "variables/deprecated"
    def set_var(self, image, variable_name):
        _variable_storage[variable_name] = image
        return (image,)

class GetImageVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_image"})}}
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "get_var"
    CATEGORY = "variables/deprecated"
    def get_var(self, variable_name):
        if variable_name in _variable_storage: return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")

class SetMaskVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"mask": ("MASK",), "variable_name": ("STRING", {"default": "my_mask"})}}
    RETURN_TYPES = ("MASK",)
    FUNCTION = "set_var"
    CATEGORY = "variables/deprecated"
    def set_var(self, mask, variable_name):
        _variable_storage[variable_name] = mask
        return (mask,)

class GetMaskVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_mask"})}}
    RETURN_TYPES = ("MASK",)
    FUNCTION = "get_var"
    CATEGORY = "variables/deprecated"
    def get_var(self, variable_name):
        if variable_name in _variable_storage: return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")

class SetLatentVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"latent": ("LATENT",), "variable_name": ("STRING", {"default": "my_latent"})}}
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "set_var"
    CATEGORY = "variables/deprecated"
    def set_var(self, latent, variable_name):
        _variable_storage[variable_name] = latent
        return (latent,)

class GetLatentVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_latent"})}}
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "get_var"
    CATEGORY = "variables/deprecated"
    def get_var(self, variable_name):
        if variable_name in _variable_storage: return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")

class SetConditioningVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"conditioning": ("CONDITIONING",), "variable_name": ("STRING", {"default": "my_cond"})}}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "set_var"
    CATEGORY = "variables/deprecated"
    def set_var(self, conditioning, variable_name):
        _variable_storage[variable_name] = conditioning
        return (conditioning,)

class GetConditioningVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_cond"})}}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "get_var"
    CATEGORY = "variables/deprecated"
    def get_var(self, variable_name):
        if variable_name in _variable_storage: return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")

class SetModelVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"model": ("MODEL",), "variable_name": ("STRING", {"default": "my_model"})}}
    RETURN_TYPES = ("MODEL",)
    FUNCTION = "set_var"
    CATEGORY = "variables/deprecated"
    def set_var(self, model, variable_name):
        _variable_storage[variable_name] = model
        return (model,)

class GetModelVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_model"})}}
    RETURN_TYPES = ("MODEL",)
    FUNCTION = "get_var"
    CATEGORY = "variables/deprecated"
    def get_var(self, variable_name):
        if variable_name in _variable_storage: return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")

class SetClipVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"clip": ("CLIP",), "variable_name": ("STRING", {"default": "my_clip"})}}
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "set_var"
    CATEGORY = "variables/deprecated"
    def set_var(self, clip, variable_name):
        _variable_storage[variable_name] = clip
        return (clip,)

class GetClipVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_clip"})}}
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "get_var"
    CATEGORY = "variables/deprecated"
    def get_var(self, variable_name):
        if variable_name in _variable_storage: return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")

class SetVaeVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"vae": ("VAE",), "variable_name": ("STRING", {"default": "my_vae"})}}
    RETURN_TYPES = ("VAE",)
    FUNCTION = "set_var"
    CATEGORY = "variables/deprecated"
    def set_var(self, vae, variable_name):
        _variable_storage[variable_name] = vae
        return (vae,)

class GetVaeVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_vae"})}}
    RETURN_TYPES = ("VAE",)
    FUNCTION = "get_var"
    CATEGORY = "variables/deprecated"
    def get_var(self, variable_name):
        if variable_name in _variable_storage: return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")

class SetStringVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"string": ("STRING", {"forceInput": True}), "variable_name": ("STRING", {"default": "my_string"})}}
    RETURN_TYPES = ("STRING",)
    FUNCTION = "set_var"
    CATEGORY = "variables/deprecated"
    def set_var(self, string, variable_name):
        _variable_storage[variable_name] = string
        return (string,)

class GetStringVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_string"})}}
    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_var"
    CATEGORY = "variables/deprecated"
    def get_var(self, variable_name):
        if variable_name in _variable_storage: return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")

class SetIntVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": ("INT", {"forceInput": True}), "variable_name": ("STRING", {"default": "my_int"})}}
    RETURN_TYPES = ("INT",)
    FUNCTION = "set_var"
    CATEGORY = "variables/deprecated"
    def set_var(self, value, variable_name):
        _variable_storage[variable_name] = value
        return (value,)

class GetIntVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_int"})}}
    RETURN_TYPES = ("INT",)
    FUNCTION = "get_var"
    CATEGORY = "variables/deprecated"
    def get_var(self, variable_name):
        if variable_name in _variable_storage: return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")

class SetFloatVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": ("FLOAT", {"forceInput": True}), "variable_name": ("STRING", {"default": "my_float"})}}
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "set_var"
    CATEGORY = "variables/deprecated"
    def set_var(self, value, variable_name):
        _variable_storage[variable_name] = value
        return (value,)

class GetFloatVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_float"})}}
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_var"
    CATEGORY = "variables/deprecated"
    def get_var(self, variable_name):
        if variable_name in _variable_storage: return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== NODE MAPPINGS ==============
NODE_CLASS_MAPPINGS = {
    # Main nodes
    "SetVariable": SetVariable,
    "GetVariable": GetVariable,
    "ListVariables": ListVariables,
    # Deprecated type-specific nodes
    "SetImageVariable": SetImageVariable,
    "GetImageVariable": GetImageVariable,
    "SetMaskVariable": SetMaskVariable,
    "GetMaskVariable": GetMaskVariable,
    "SetLatentVariable": SetLatentVariable,
    "GetLatentVariable": GetLatentVariable,
    "SetConditioningVariable": SetConditioningVariable,
    "GetConditioningVariable": GetConditioningVariable,
    "SetModelVariable": SetModelVariable,
    "GetModelVariable": GetModelVariable,
    "SetClipVariable": SetClipVariable,
    "GetClipVariable": GetClipVariable,
    "SetVaeVariable": SetVaeVariable,
    "GetVaeVariable": GetVaeVariable,
    "SetStringVariable": SetStringVariable,
    "GetStringVariable": GetStringVariable,
    "SetIntVariable": SetIntVariable,
    "GetIntVariable": GetIntVariable,
    "SetFloatVariable": SetFloatVariable,
    "GetFloatVariable": GetFloatVariable,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # Main nodes
    "SetVariable": "Set Variable",
    "GetVariable": "Get Variable",
    "ListVariables": "List Variables",
    # Deprecated
    "SetImageVariable": "Set Image Variable (deprecated)",
    "GetImageVariable": "Get Image Variable (deprecated)",
    "SetMaskVariable": "Set Mask Variable (deprecated)",
    "GetMaskVariable": "Get Mask Variable (deprecated)",
    "SetLatentVariable": "Set Latent Variable (deprecated)",
    "GetLatentVariable": "Get Latent Variable (deprecated)",
    "SetConditioningVariable": "Set Conditioning Variable (deprecated)",
    "GetConditioningVariable": "Get Conditioning Variable (deprecated)",
    "SetModelVariable": "Set Model Variable (deprecated)",
    "GetModelVariable": "Get Model Variable (deprecated)",
    "SetClipVariable": "Set CLIP Variable (deprecated)",
    "GetClipVariable": "Get CLIP Variable (deprecated)",
    "SetVaeVariable": "Set VAE Variable (deprecated)",
    "GetVaeVariable": "Get VAE Variable (deprecated)",
    "SetStringVariable": "Set String Variable (deprecated)",
    "GetStringVariable": "Get String Variable (deprecated)",
    "SetIntVariable": "Set Int Variable (deprecated)",
    "GetIntVariable": "Get Int Variable (deprecated)",
    "SetFloatVariable": "Set Float Variable (deprecated)",
    "GetFloatVariable": "Get Float Variable (deprecated)",
}
