# ComfyUI Simple Variables

A custom node pack for ComfyUI that provides **Set/Get variable nodes** for storing and retrieving data by name across your workflow.

## Features

- Store any ComfyUI data type with a custom variable name
- Retrieve stored variables anywhere in your workflow
- Reduces wire clutter by allowing "wireless" data transfer
- Passthrough design - Set nodes output the same data they receive

## Supported Variable Types

| Type | Set Node | Get Node | Category |
|------|----------|----------|----------|
| Image | Set Image Variable | Get Image Variable | `variables/image` |
| Mask | Set Mask Variable | Get Mask Variable | `variables/mask` |
| Latent | Set Latent Variable | Get Latent Variable | `variables/latent` |
| Conditioning | Set Conditioning Variable | Get Conditioning Variable | `variables/conditioning` |
| Model | Set Model Variable | Get Model Variable | `variables/model` |
| CLIP | Set CLIP Variable | Get CLIP Variable | `variables/clip` |
| VAE | Set VAE Variable | Get VAE Variable | `variables/vae` |
| String | Set String Variable | Get String Variable | `variables/primitive` |
| Int | Set Int Variable | Get Int Variable | `variables/primitive` |
| Float | Set Float Variable | Get Float Variable | `variables/primitive` |
| Any | Set Any Variable | Get Any Variable | `variables` |

### Utility Nodes

- **List All Variables** - Shows all currently stored variables and their types

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` folder:
   ```bash
   cd ComfyUI/custom_nodes
   git clone <your-repo-url> SimpleImageVariables
   ```

2. Restart ComfyUI

3. Search for "variable" in the node menu

## Usage

### Basic Example

```
[Load Image] → [Set Image Variable] (name: "reference")
                       ↓
              (passes image through to next node)

... elsewhere in workflow ...

[Get Image Variable] (name: "reference") → [Use Image Node]
```

### How It Works

1. **Set nodes** store the input data in memory with your chosen variable name
2. **Set nodes** also pass the data through, so you can continue your workflow normally
3. **Get nodes** retrieve the stored data by variable name
4. Variables persist for the duration of the ComfyUI session

### Tips

- Use descriptive variable names like `"upscaled_image"` or `"final_mask"`
- The **Set Any Variable** node accepts any data type (useful for custom node outputs)
- Use **List All Variables** to debug and see what's currently stored
- Variables are cleared when ComfyUI restarts

## Node Details

### Set Nodes
- **Inputs**:
  - `data` - The data to store (type depends on node)
  - `variable_name` - String name for the variable
- **Outputs**: Same data that was input (passthrough)

### Get Nodes
- **Inputs**:
  - `variable_name` - String name of the variable to retrieve
- **Outputs**: The stored data

### Error Handling

If you try to Get a variable that hasn't been Set, you'll receive an error message listing all available variable names.

## License

MIT License - Free to use and modify.

## Credits

Created with assistance from Claude (Anthropic) for ComfyUI workflow optimization.
