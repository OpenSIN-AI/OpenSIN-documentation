# SIN Image Handling — Image Validation & Resizing

> **OpenSIN's Image Handling** — Geklont aus Claude Code's imageValidation.ts, imageResizer.ts. Bildvalidierung und -skalierung.

## Image Validation

```python
from opensin.images import ImageValidator

validator = ImageValidator(
    max_width=4096,
    max_height=4096,
    max_file_size=10 * 1024 * 1024,
    supported_formats=["png", "jpg", "gif", "webp"]
)

try:
    await validator.validate(image_path)
except ImageSizeError as e:
    print(f"Image too large: {e}")
except ImageFormatError as e:
    print(f"Unsupported format: {e}")
```

## Image Resizing

```python
from opensin.images import ImageResizer

resizer = ImageResizer(
    max_width=1024,
    max_height=1024,
    quality=85
)

# Resize image
resized = await resizer.resize(image_path)
```

## Error Types

| Error | Description |
|-------|-------------|
| `ImageSizeError` | Image exceeds size limits |
| `ImageResizeError` | Resize operation failed |
| `ImageFormatError` | Unsupported format |

## Best Practices

1. **Validate early** — Bilder vor Verarbeitung validieren
2. **Resize large images** — Große Bilder verkleinern
3. **Support common formats** — PNG, JPG, GIF, WebP
4. **Handle errors gracefully** — Fehler behandeln
5. **Track usage** — Bild-Usage tracken

## Next Steps

- [SIN Attachment System](/guide/sin-attachment-system)
- [SIN Tool System](/guide/sin-tool-system)
