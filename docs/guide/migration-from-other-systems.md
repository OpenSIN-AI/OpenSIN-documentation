# Migration Guide from Other Agent Systems

Move from LangChain, AutoGen, CrewAI, or other frameworks to OpenSIN.

## Why Migrate to OpenSIN?

| Feature | OpenSIN | LangChain | AutoGen | CrewAI |
|---------|---------|-----------|---------|--------|
| Multi-Agent Teams | ✅ Native | ⚠️ Manual | ✅ Yes | ✅ Yes |
| A2A Protocol | ✅ Built-in | ❌ No | ⚠️ Basic | ❌ No |
| Platform Integrations | ✅ 27+ | ❌ None | ❌ None | ❌ None |
| Production Ready | ✅ Yes | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial |
| Fleet Management | ✅ Yes | ❌ No | ❌ No | ❌ No |
| Monitoring | ✅ Built-in | ❌ External | ❌ External | ❌ External |
| Open Source | ✅ Apache 2.0 | ✅ MIT | ✅ MIT | ✅ MIT |

## Migration from LangChain

### Before (LangChain)

```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4")
prompt = PromptTemplate.from_template("Answer: {question}")
chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(question="What is AI?")
```

### After (OpenSIN)

```python
from opensin import Agent

agent = Agent(
    name="assistant",
    model="gpt-4",
    system_prompt="Answer questions concisely."
)
result = await agent.send("What is AI?")
```

### Migration Steps

1. Replace `LLMChain` with `Agent`
2. Replace `PromptTemplate` with `system_prompt`
3. Replace `chain.run()` with `agent.send()`
4. Use `Team` for multi-agent workflows instead of manual chains

## Migration from AutoGen

### Before (AutoGen)

```python
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent("assistant", llm_config={"model": "gpt-4"})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

user_proxy.initiate_chat(assistant, message="Write a Python script")
```

### After (OpenSIN)

```python
from opensin import Agent, Team

assistant = Agent(
    name="assistant",
    model="gpt-4",
    tools=["code_interpreter"]
)

team = Team(name="coding-team", agents=[assistant])
result = await team.execute("Write a Python script")
```

### Migration Steps

1. Replace `AssistantAgent` with `Agent`
2. Replace `UserProxyAgent` with `Team` or direct `agent.send()`
3. Replace `initiate_chat()` with `team.execute()` or `agent.send()`
4. Use OpenSIN's built-in tool registry instead of manual code execution config

## Migration from CrewAI

### Before (CrewAI)

```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role="Researcher",
    goal="Research topics thoroughly",
    backstory="Expert researcher",
    llm=ChatOpenAI(model="gpt-4")
)

task = Task(description="Research AI trends", agent=researcher)
crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()
```

### After (OpenSIN)

```python
from opensin import Agent, Team

researcher = Agent(
    name="researcher",
    model="gpt-4",
    system_prompt="You are an expert researcher. Research topics thoroughly."
)

team = Team(name="research-crew", agents=[researcher])
result = await team.execute("Research AI trends")
```

### Migration Steps

1. Replace CrewAI `Agent` with OpenSIN `Agent`
2. Replace `Task` + `Crew` with `Team`
3. Replace `crew.kickoff()` with `team.execute()`
4. Use OpenSIN's built-in A2A protocol for agent communication

## Migration from Semantic Kernel

### Before (Semantic Kernel)

```python
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

kernel = Kernel()
kernel.add_service(OpenAIChatCompletion(service_id="default", ai_model_id="gpt-4"))
result = await kernel.invoke(prompt="Hello")
```

### After (OpenSIN)

```python
from opensin import Agent

agent = Agent(name="assistant", model="gpt-4")
result = await agent.send("Hello")
```

## Migration from LlamaIndex

### Before (LlamaIndex)

```python
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
result = query_engine.query("What does the document say about AI?")
```

### After (OpenSIN)

```python
from opensin import Agent

agent = Agent(
    name="researcher",
    model="gpt-4",
    tools=["vector_search"],
    knowledge_base="data"
)
result = await agent.send("What does the document say about AI?")
```

## Common Migration Patterns

### 1. Single Agent → Single Agent

Direct replacement. OpenSIN's Agent API is simpler and more intuitive.

### 2. Chain → Pipeline

Replace LangChain chains with OpenSIN's Pipeline pattern.

### 3. Multi-Agent Chat → Team

Replace manual multi-agent setups with OpenSIN Teams.

### 4. Custom Tools → Tool Registry

Register tools in OpenSIN's built-in tool registry.

### 5. Custom Memory → Memory Manager

Use OpenSIN's built-in memory management system.

## Post-Migration Checklist

- [ ] All agents migrated
- [ ] All tools registered
- [ ] Teams configured
- [ ] A2A communication working
- [ ] Tests passing
- [ ] Performance benchmarks met
- [ ] Monitoring enabled
- [ ] Documentation updated

## Next Steps

- [Getting Started](/guide/getting-started)
- [Agent Basics](/guide/agent-basics)
- [Team Orchestration](/guide/team-orchestration)
- [A2A Protocol](/guide/a2a-protocol)
