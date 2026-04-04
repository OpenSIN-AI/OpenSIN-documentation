# Multi-Modal Agents

Build agents that work with text, images, audio, and video.

## Overview

Multi-modal agents can process and generate multiple types of content:

| Modality | Input | Output | Models |
|----------|-------|--------|--------|
| Text | Text | Text | GPT-4, Claude, Gemini |
| Vision | Images | Text | GPT-4V, Gemini Pro |
| Audio | Audio | Text | Whisper |
| Speech | Text | Audio | TTS models |
| Video | Video | Text | Gemini Pro, GPT-4V |

## Vision Agent

```python
from opensin import Agent

vision_agent = Agent(
    name="vision-analyst",
    model="gpt-4-vision",
    system_prompt="You analyze images and describe what you see.",
    tools=["image_analysis", "ocr", "object_detection"]
)

# Analyze an image
response = await vision_agent.send(
    "What's in this image?",
    attachments=["screenshot.png"]
)
```

## Audio Agent

```python
audio_agent = Agent(
    name="audio-processor",
    model="whisper-1",
    system_prompt="You transcribe and analyze audio.",
    tools=["transcription", "sentiment_analysis"]
)

# Transcribe audio
transcript = await audio_agent.process("meeting_recording.mp3")
```

## Multi-Modal Pipeline

```python
from opensin import Pipeline

pipeline = Pipeline([
    VisionAgent(),      # Analyze screenshot
    TextAgent(),        # Generate description
    AudioAgent(),       # Create voice narration
    VideoAgent(),       # Combine into video
])

result = await pipeline.execute({
    "input": "screenshot.png",
    "output_format": "video"
})
```

## Best Practices

1. **Right model for modality** — Use specialized models
2. **Compress media** — Reduce file sizes before processing
3. **Cache results** — Same image = same analysis
4. **Handle failures** — Media processing can fail
5. **Monitor costs** — Media processing is expensive

## Next Steps

- [Agent Configuration](/guide/agent-configuration)
- [LLM Provider Setup](/guide/llm-provider-setup)
