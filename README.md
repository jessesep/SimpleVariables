# SimpleVariables

A lightweight ComfyUI node pack for storing and retrieving any data by name across your workflow.

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jessesep/SimpleVariables.git
```

Restart ComfyUI and search for **"variable"**.

## Nodes

| Node | Description |
|------|-------------|
| **Set Variable** | Store any data with a name, outputs preview |
| **Get Variable** | Retrieve data by name, outputs preview |
| **List Variables** | Show all stored variables |
| **Clear Variables** | Clear all stored variables |

## Usage

```
[Load Image] → [Set Variable] (name: "ref")
                     ↓
              value (passthrough)
              preview → [Show Text] → "[ref] = Tensor [1, 512, 512, 3]"

... elsewhere ...

[Get Variable] (name: "ref") → value → [Any Node]
                             → preview → "[ref] = Tensor [1, 512, 512, 3]"
```

## Features

- **Universal** - Works with all data types (Image, Mask, Latent, Model, etc.)
- **Preview output** - See what's stored (type + shape/value)
- **Passthrough** - Set Variable passes data through
- **Debug** - List Variables shows all stored data

## Preview Examples

| Data Type | Preview Output |
|-----------|----------------|
| Image | `[my_image] = Tensor [1, 512, 512, 3]` |
| String | `[prompt] = "a beautiful sunset..."` |
| Int | `[steps] = 20` |
| Model | `[my_model] = BaseModel` |

## License

MIT License

## Credits

Created by jessesep with Claude (Anthropic).
