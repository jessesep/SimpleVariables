"""
Simple Variables - Set and Get nodes for storing/retrieving data by name
Supports: Image, Mask, Latent, Conditioning, Model, CLIP, VAE, String, Int, Float, Any
"""

# Global storage for variables
_variable_storage = {}


# ============== IMAGE ==============
class SetImageVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "variable_name": ("STRING", {"default": "my_image"}),
            }
        }
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "set_var"
    CATEGORY = "variables/image"

    def set_var(self, image, variable_name):
        _variable_storage[variable_name] = image
        return (image,)


class GetImageVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_image"})}}
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "get_var"
    CATEGORY = "variables/image"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== MASK ==============
class SetMaskVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK",),
                "variable_name": ("STRING", {"default": "my_mask"}),
            }
        }
    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = "set_var"
    CATEGORY = "variables/mask"

    def set_var(self, mask, variable_name):
        _variable_storage[variable_name] = mask
        return (mask,)


class GetMaskVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_mask"})}}
    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = "get_var"
    CATEGORY = "variables/mask"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== LATENT ==============
class SetLatentVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT",),
                "variable_name": ("STRING", {"default": "my_latent"}),
            }
        }
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "set_var"
    CATEGORY = "variables/latent"

    def set_var(self, latent, variable_name):
        _variable_storage[variable_name] = latent
        return (latent,)


class GetLatentVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_latent"})}}
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "get_var"
    CATEGORY = "variables/latent"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== CONDITIONING ==============
class SetConditioningVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "conditioning": ("CONDITIONING",),
                "variable_name": ("STRING", {"default": "my_cond"}),
            }
        }
    RETURN_TYPES = ("CONDITIONING",)
    RETURN_NAMES = ("conditioning",)
    FUNCTION = "set_var"
    CATEGORY = "variables/conditioning"

    def set_var(self, conditioning, variable_name):
        _variable_storage[variable_name] = conditioning
        return (conditioning,)


class GetConditioningVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_cond"})}}
    RETURN_TYPES = ("CONDITIONING",)
    RETURN_NAMES = ("conditioning",)
    FUNCTION = "get_var"
    CATEGORY = "variables/conditioning"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== MODEL ==============
class SetModelVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "variable_name": ("STRING", {"default": "my_model"}),
            }
        }
    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "set_var"
    CATEGORY = "variables/model"

    def set_var(self, model, variable_name):
        _variable_storage[variable_name] = model
        return (model,)


class GetModelVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_model"})}}
    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "get_var"
    CATEGORY = "variables/model"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== CLIP ==============
class SetClipVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "clip": ("CLIP",),
                "variable_name": ("STRING", {"default": "my_clip"}),
            }
        }
    RETURN_TYPES = ("CLIP",)
    RETURN_NAMES = ("clip",)
    FUNCTION = "set_var"
    CATEGORY = "variables/clip"

    def set_var(self, clip, variable_name):
        _variable_storage[variable_name] = clip
        return (clip,)


class GetClipVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_clip"})}}
    RETURN_TYPES = ("CLIP",)
    RETURN_NAMES = ("clip",)
    FUNCTION = "get_var"
    CATEGORY = "variables/clip"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== VAE ==============
class SetVaeVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "vae": ("VAE",),
                "variable_name": ("STRING", {"default": "my_vae"}),
            }
        }
    RETURN_TYPES = ("VAE",)
    RETURN_NAMES = ("vae",)
    FUNCTION = "set_var"
    CATEGORY = "variables/vae"

    def set_var(self, vae, variable_name):
        _variable_storage[variable_name] = vae
        return (vae,)


class GetVaeVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_vae"})}}
    RETURN_TYPES = ("VAE",)
    RETURN_NAMES = ("vae",)
    FUNCTION = "get_var"
    CATEGORY = "variables/vae"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== STRING ==============
class SetStringVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"forceInput": True}),
                "variable_name": ("STRING", {"default": "my_string"}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "set_var"
    CATEGORY = "variables/primitive"

    def set_var(self, string, variable_name):
        _variable_storage[variable_name] = string
        return (string,)


class GetStringVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_string"})}}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "get_var"
    CATEGORY = "variables/primitive"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== INT ==============
class SetIntVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {"forceInput": True}),
                "variable_name": ("STRING", {"default": "my_int"}),
            }
        }
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("value",)
    FUNCTION = "set_var"
    CATEGORY = "variables/primitive"

    def set_var(self, value, variable_name):
        _variable_storage[variable_name] = value
        return (value,)


class GetIntVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_int"})}}
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_var"
    CATEGORY = "variables/primitive"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== FLOAT ==============
class SetFloatVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"forceInput": True}),
                "variable_name": ("STRING", {"default": "my_float"}),
            }
        }
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("value",)
    FUNCTION = "set_var"
    CATEGORY = "variables/primitive"

    def set_var(self, value, variable_name):
        _variable_storage[variable_name] = value
        return (value,)


class GetFloatVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_float"})}}
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_var"
    CATEGORY = "variables/primitive"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found")


# ============== ANY (Universal) ==============
class SetAnyVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "variable_name": ("STRING", {"default": "my_var"}),
            },
            "optional": {
                "any": ("*",),
            }
        }
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("any",)
    FUNCTION = "set_var"
    CATEGORY = "variables"

    def set_var(self, variable_name, any=None):
        _variable_storage[variable_name] = any
        return (any,)


class GetAnyVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"variable_name": ("STRING", {"default": "my_var"})}}
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("any",)
    FUNCTION = "get_var"
    CATEGORY = "variables"

    def get_var(self, variable_name):
        if variable_name in _variable_storage:
            return (_variable_storage[variable_name],)
        raise ValueError(f"Variable '{variable_name}' not found. Available: {list(_variable_storage.keys())}")


# ============== LIST VARIABLES ==============
class ListVariables:
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


NODE_CLASS_MAPPINGS = {
    # Image
    "SetImageVariable": SetImageVariable,
    "GetImageVariable": GetImageVariable,
    # Mask
    "SetMaskVariable": SetMaskVariable,
    "GetMaskVariable": GetMaskVariable,
    # Latent
    "SetLatentVariable": SetLatentVariable,
    "GetLatentVariable": GetLatentVariable,
    # Conditioning
    "SetConditioningVariable": SetConditioningVariable,
    "GetConditioningVariable": GetConditioningVariable,
    # Model
    "SetModelVariable": SetModelVariable,
    "GetModelVariable": GetModelVariable,
    # CLIP
    "SetClipVariable": SetClipVariable,
    "GetClipVariable": GetClipVariable,
    # VAE
    "SetVaeVariable": SetVaeVariable,
    "GetVaeVariable": GetVaeVariable,
    # String
    "SetStringVariable": SetStringVariable,
    "GetStringVariable": GetStringVariable,
    # Int
    "SetIntVariable": SetIntVariable,
    "GetIntVariable": GetIntVariable,
    # Float
    "SetFloatVariable": SetFloatVariable,
    "GetFloatVariable": GetFloatVariable,
    # Any
    "SetAnyVariable": SetAnyVariable,
    "GetAnyVariable": GetAnyVariable,
    # Utility
    "ListVariables": ListVariables,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # Image
    "SetImageVariable": "Set Image Variable",
    "GetImageVariable": "Get Image Variable",
    # Mask
    "SetMaskVariable": "Set Mask Variable",
    "GetMaskVariable": "Get Mask Variable",
    # Latent
    "SetLatentVariable": "Set Latent Variable",
    "GetLatentVariable": "Get Latent Variable",
    # Conditioning
    "SetConditioningVariable": "Set Conditioning Variable",
    "GetConditioningVariable": "Get Conditioning Variable",
    # Model
    "SetModelVariable": "Set Model Variable",
    "GetModelVariable": "Get Model Variable",
    # CLIP
    "SetClipVariable": "Set CLIP Variable",
    "GetClipVariable": "Get CLIP Variable",
    # VAE
    "SetVaeVariable": "Set VAE Variable",
    "GetVaeVariable": "Get VAE Variable",
    # String
    "SetStringVariable": "Set String Variable",
    "GetStringVariable": "Get String Variable",
    # Int
    "SetIntVariable": "Set Int Variable",
    "GetIntVariable": "Get Int Variable",
    # Float
    "SetFloatVariable": "Set Float Variable",
    "GetFloatVariable": "Get Float Variable",
    # Any
    "SetAnyVariable": "Set Any Variable",
    "GetAnyVariable": "Get Any Variable",
    # Utility
    "ListVariables": "List All Variables",
}
