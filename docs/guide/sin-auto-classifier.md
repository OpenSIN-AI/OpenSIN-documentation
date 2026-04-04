# SIN Auto-Mode Classifier — AI-Based Permission Decisions

> **OpenSIN's Auto Classifier** — Geklont aus Claude Code's yoloClassifier.ts. KI entscheidet ob Tools erlaubt oder verweigert werden.

## Architektur

```
Tool Request → Fast Path Check → Safe? → ALLOW
                        ↓ No
                Full AI Classifier → ALLOW/DENY
```

## Fast Paths

```python
class AutoClassifier:
    async def classify(self, tool_name: str, tool_input: dict, context: dict) -> Decision:
        # Fast Path 1: acceptEdits Check
        if self.is_safe_file_edit(tool_name, tool_input):
            return Decision.ALLOW  # Skip classifier
        
        # Fast Path 2: Safe Allowlist
        if tool_name in self.safe_tools:
            return Decision.ALLOW  # Skip classifier
        
        # Full Classifier: LLM entscheidet
        return await self.full_classify(tool_name, tool_input, context)
```

## Safe Tools Allowlist

```python
SAFE_TOOLS = [
    "ls", "cat", "git status", "git log",
    "pwd", "echo", "head", "tail",
    "grep", "find", "wc"
]

# Diese Tools skippen den Classifier komplett
# Spart Zeit und Token
```

## Full AI Classifier

```python
async def full_classify(self, tool_name: str, tool_input: dict, context: dict) -> Decision:
    # Baue Transcript für den Classifier
    transcript = self.build_classifier_transcript(
        tool_name=tool_name,
        tool_input=tool_input,
        context=context
    )
    
    # Schnelles Modell für Classification
    response = await self.classifier_model.generate(
        system_prompt=CLASSIFIER_SYSTEM_PROMPT,
        prompt=transcript
    )
    
    return Decision.ALLOW if response == "allow" else Decision.DENY
```

## Denial Tracking mit Fallback

```python
from opensin.permissions import DenialTracker

tracker = DenialTracker(
    max_consecutive_denials=5,
    max_total_denials=20
)

# Tracke Denials
tracker.record_denial(tool_name, tool_input)

# Wenn Limits erreicht → Fallback zu Manual Prompting
if tracker.has_hit_limit():
    # Verhindert dass Classifier in Endlos-Deny-Loop steckt
    await manual_prompt_user()
    tracker.reset()
```

## Best Practices

1. **Fast Paths zuerst** — Bekannte safe Tools skippen Classifier
2. **Schnelles Modell** — GPT-3.5 für Classification reicht
3. **Denial Tracking** — Verhindert Endlos-Loops
4. **Manual Fallback** — User kann immer override
5. **Monitor Accuracy** — Tracke Classifier Entscheidungen

## Next Steps

- [SIN Permissions](/guide/sin-permission-system)
- [SIN Hooks](/guide/sin-hook-system)
