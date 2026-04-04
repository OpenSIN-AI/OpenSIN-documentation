# SIN Attachment System — Images, Files, Memory

> **OpenSIN's Attachment System** — Geklont aus Claude Code's attachments.ts. Bild-, Datei- und Memory-Attachments.

## Attachment Types

| Type | Description | Max Size |
|------|-------------|----------|
| Image | Bilder (PNG, JPG, GIF) | 10MB |
| File | Dateien (PDF, TXT, CSV) | 25MB |
| Memory | Memory-Einträge | 25KB |
| Clipboard | Clipboard-Inhalte | 1MB |

## Image Processing

```python
from opensin.attachments import ImageProcessor

processor = ImageProcessor(
    max_size=10 * 1024 * 1024,  # 10MB
    supported_formats=["png", "jpg", "gif", "webp"],
    resize_threshold=1024  # Max 1024px
)

# Verarbeite Bild
processed = await processor.process(image_path)

# Resize wenn nötig
if processed.width > processor.resize_threshold:
    processed = await processor.resize(processed)
```

## Image Validation

```python
from opensin.attachments import ImageValidator

validator = ImageValidator(
    max_width=4096,
    max_height=4096,
    max_file_size=10 * 1024 * 1024
)

# Validiere Bild
try:
    await validator.validate(image_path)
except ImageSizeError:
    print("Bild zu groß")
except ImageFormatError:
    print("Nicht unterstütztes Format")
```

## Relevant Memory Prefetch

```python
from opensin.attachments import MemoryPrefetcher

prefetcher = MemoryPrefetcher(
    memory_index=memory_index,
    max_results=5,
    relevance_threshold=0.7
)

# Prefetch relevante Memory-Einträge
async def prefetch_relevant_memory(user_input: str):
    results = await prefetcher.search(user_input)
    return [r.content for r in results]
```

## Duplicate Memory Filtering

```python
from opensin.attachments import MemoryDeduplicator

deduplicator = MemoryDeduplicator(
    similarity_threshold=0.9
)

# Filtere duplizierte Memory-Einträge
filtered = await deduplicator.filter(memory_entries)
```

## Attachment Message Building

```python
async def get_attachment_messages(
    attachments: list[Attachment]
) -> list[Message]:
    """Buildet Nachrichten für Attachments."""
    messages = []
    
    for attachment in attachments:
        if attachment.type == "image":
            messages.append(create_image_message(attachment))
        elif attachment.type == "file":
            messages.append(create_file_message(attachment))
        elif attachment.type == "memory":
            messages.append(create_memory_message(attachment))
    
    return messages
```

## Best Practices

1. **Validate early** — Attachments vor Verarbeitung validieren
2. **Resize images** — Große Bilder verkleinern
3. **Prefetch memory** — Relevante Memory-Einträge vorladen
4. **Filter duplicates** — Duplizierte Memory-Einträge entfernen
5. **Handle errors** — Graceful degradation bei fehlerhaften Attachments

## Next Steps

- [SIN File Memory](/guide/sin-file-memory)
- [SIN ReAct Loop](/guide/sin-react-loop)
