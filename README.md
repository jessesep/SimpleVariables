# ComfyUI Simple Variables

A lightweight custom node pack for ComfyUI that provides **Set/Get variable nodes** for storing and retrieving any data by name across your workflow.

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jessesep/ComfyUI-SimpleVariables.git
```

Restart ComfyUI and search for **"variable"** in the node menu.

## Nodes

| Node | Description | Category |
|------|-------------|----------|
| **Set Variable** | Store any data with a custom name | `variables` |
| **Get Variable** | Retrieve stored data by name | `variables` |
| **List Variables** | Show all stored variables | `variables` |

## Usage

### Basic Example

```
[Load Image] → [Set Variable] (name: "reference")
                     ↓
            (passes through)

... elsewhere in workflow ...

[Get Variable] (name: "reference") → [Any Node]
```

### How It Works

1. **Set Variable** stores any input data with your chosen variable name
2. Data passes through, so you can continue your workflow normally
3. **Get Variable** retrieves stored data anywhere by name
4. Works with ALL ComfyUI data types: Image, Mask, Latent, Model, CLIP, VAE, Conditioning, String, Int, Float, and custom types

### Tips

- Use descriptive names like `"upscaled_image"` or `"final_mask"`
- **List Variables** helps debug what's currently stored
- Variables persist for the ComfyUI session (cleared on restart)
- If a variable doesn't exist, you'll see available variable names in the error

## Why Use This?

- **Reduce wire clutter** - "Wireless" data transfer across your workflow
- **Reuse outputs** - Store once, use multiple times
- **Simplify complex workflows** - No more spaghetti connections
- **Universal** - One node handles all data types

## Deprecated Nodes

Type-specific nodes (Set Image Variable, Set Mask Variable, etc.) are available under `variables/deprecated` for backward compatibility, but **Set/Get Variable handles all types** so they're no longer needed.

## License

MIT License - Free to use and modify.

## Credits

Created by jessesep with assistance from Claude (Anthropic).
