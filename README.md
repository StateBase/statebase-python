<div align="center">

# StateBase Python SDK

**Official Python client for StateBase API**

[![PyPI version](https://badge.fury.io/py/statebase.svg)](https://badge.fury.io/py/statebase)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

[Documentation](https://docs.statebase.org/python) • [API Reference](https://docs.statebase.org/api) • [Examples](./examples) • [Changelog](./CHANGELOG.md)

</div>

---

## Installation

```bash
pip install statebase
```

### Requirements

- Python 3.8 or higher
- `requests` library (automatically installed)

---

## Quick Start

```python
from statebase import StateBase

# Initialize client
sb = StateBase(api_key="sb_live_xxxxxxxx")

# Create a session
session = sb.sessions.create(
    agent_id="customer-support",
    initial_state={"status": "new", "user_id": "user_123"}
)

# Update state
sb.sessions.update_state(
    session_id=session.id,
    state={"status": "in_progress"},
    reasoning="User provided ticket details"
)

# Add a conversation turn
turn = sb.sessions.add_turn(
    session_id=session.id,
    input="My order hasn't arrived",
    output="I'll help you track your order. Can you provide the order number?"
)

# Search memories
memories = sb.memory.search(
    query="user communication preferences",
    session_id=session.id
)

# Rollback if needed
sb.sessions.rollback(
    session_id=session.id,
    version=-1,
    reason="Agent made an error"
)
```

---

## Features

### ✅ Complete API Coverage

- Sessions (create, read, update, delete)
- State management with versioning
- Conversation turns
- Semantic memory (add, search)
- Decision traces
- Instant rollback

### ✅ Developer-Friendly

- Type hints for all methods
- Comprehensive error handling
- Automatic retries with exponential backoff
- Request/response logging (optional)

### ✅ Production-Ready

- Connection pooling
- Timeout configuration
- Rate limit handling
- Async support (optional)

---

## Usage

### Authentication

```python
from statebase import StateBase

# Option 1: Pass API key directly
sb = StateBase(api_key="sb_live_xxxxxxxx")

# Option 2: Use environment variable
# Set STATEBASE_API_KEY in your environment
sb = StateBase()

# Option 3: Custom base URL (for self-hosted)
sb = StateBase(
    api_key="your_key",
    base_url="https://your-instance.com"
)
```

### Sessions

```python
# Create session
session = sb.sessions.create(
    agent_id="support-bot",
    initial_state={"user": "alice"},
    ttl_seconds=86400  # 24 hours
)

# Get session
session = sb.sessions.get(session_id="sess_abc123")

# Update state
sb.sessions.update_state(
    session_id="sess_abc123",
    state={"step": "collect_info"},
    reasoning="Moved to next step"
)

# Delete session
sb.sessions.delete(session_id="sess_abc123")

# List sessions
sessions = sb.sessions.list(
    agent_id="support-bot",
    limit=10
)
```

### Conversation Turns

```python
# Add turn
turn = sb.sessions.add_turn(
    session_id="sess_abc123",
    input="What's my order status?",
    output="Your order #12345 is out for delivery",
    metadata={"model": "gpt-4", "tokens": 150}
)

# Get turn history
turns = sb.sessions.get_turns(
    session_id="sess_abc123",
    limit=20
)
```

### Memory

```python
# Add memory
memory = sb.memory.add(
    session_id="sess_abc123",
    content="User prefers email over SMS",
    type="preference",
    tags=["communication", "preference"]
)

# Search memories
results = sb.memory.search(
    query="how does user want to be contacted?",
    session_id="sess_abc123",
    top_k=5,
    threshold=0.7
)

# Get memory by ID
memory = sb.memory.get(memory_id="mem_xyz789")

# Delete memory
sb.memory.delete(memory_id="mem_xyz789")
```

### Rollback

```python
# Rollback to previous version
sb.sessions.rollback(
    session_id="sess_abc123",
    version=-1,  # or specific version number like 5
    reason="Agent hallucinated"
)

# Rollback to specific version
sb.sessions.rollback(
    session_id="sess_abc123",
    version=3,
    reason="Revert to known good state"
)
```

### Traces

```python
# List traces for a session
traces = sb.traces.list(
    session_id="sess_abc123",
    limit=100
)

# Get specific trace
trace = sb.traces.get(trace_id="trace_123")

# Filter traces by action
traces = sb.traces.list(
    session_id="sess_abc123",
    action="state_update"
)
```

---

## Advanced Usage

### Error Handling

```python
from statebase import StateBase, StateBaseException

sb = StateBase(api_key="your_key")

try:
    session = sb.sessions.create(agent_id="bot")
except StateBaseException as e:
    print(f"Error: {e.message}")
    print(f"Code: {e.error_code}")
    print(f"Details: {e.details}")
```

### Custom Configuration

```python
sb = StateBase(
    api_key="your_key",
    base_url="https://api.statebase.org",
    timeout=30,  # seconds
    max_retries=3,
    retry_delay=1.0,  # seconds
    enable_logging=True
)
```

### Async Support

```python
from statebase import AsyncStateBase

async def main():
    sb = AsyncStateBase(api_key="your_key")
    
    session = await sb.sessions.create(
        agent_id="async-bot"
    )
    
    await sb.sessions.update_state(
        session_id=session.id,
        state={"status": "processing"}
    )

# Run with asyncio
import asyncio
asyncio.run(main())
```

### Context Manager

```python
with StateBase(api_key="your_key") as sb:
    session = sb.sessions.create(agent_id="bot")
    # Automatically handles cleanup
```

---

## Integration Examples

### With LangChain

```python
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from statebase import StateBase

sb = StateBase(api_key="your_key")
llm = ChatOpenAI()

# Create session
session = sb.sessions.create(agent_id="langchain-bot")

# Your LangChain agent logic
def chat(message: str):
    # Get context from StateBase
    turns = sb.sessions.get_turns(session.id, limit=10)
    context = "\n".join([f"User: {t.input}\nBot: {t.output}" for t in turns])
    
    # Call LLM
    response = llm.predict(f"{context}\nUser: {message}\nBot:")
    
    # Save turn
    sb.sessions.add_turn(
        session_id=session.id,
        input=message,
        output=response
    )
    
    return response
```

### With OpenAI

```python
from openai import OpenAI
from statebase import StateBase

client = OpenAI()
sb = StateBase(api_key="your_key")

session = sb.sessions.create(agent_id="openai-bot")

def chat(message: str):
    # Add user message
    sb.sessions.add_turn(
        session_id=session.id,
        input=message,
        output=""  # Will update after LLM response
    )
    
    # Call OpenAI
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}]
    )
    
    output = response.choices[0].message.content
    
    # Update with response
    sb.sessions.update_state(
        session_id=session.id,
        state={"last_response": output}
    )
    
    return output
```

---

## API Reference

### Client

```python
class StateBase:
    def __init__(
        self,
        api_key: str = None,
        base_url: str = "https://api.statebase.org",
        timeout: int = 30,
        max_retries: int = 3,
        retry_delay: float = 1.0,
        enable_logging: bool = False
    )
```

### Sessions

```python
sb.sessions.create(agent_id: str, initial_state: dict = None, ttl_seconds: int = None) -> Session
sb.sessions.get(session_id: str) -> Session
sb.sessions.update_state(session_id: str, state: dict, reasoning: str = None) -> Session
sb.sessions.delete(session_id: str) -> None
sb.sessions.list(agent_id: str = None, limit: int = 10) -> List[Session]
sb.sessions.add_turn(session_id: str, input: str, output: str, metadata: dict = None) -> Turn
sb.sessions.get_turns(session_id: str, limit: int = 20) -> List[Turn]
sb.sessions.rollback(session_id: str, version: int, reason: str = None) -> Session
```

### Memory

```python
sb.memory.add(session_id: str, content: str, type: str = "general", tags: List[str] = None) -> Memory
sb.memory.search(query: str, session_id: str = None, top_k: int = 5, threshold: float = 0.7) -> List[Memory]
sb.memory.get(memory_id: str) -> Memory
sb.memory.delete(memory_id: str) -> None
```

### Traces

```python
sb.traces.list(session_id: str, limit: int = 100, action: str = None) -> List[Trace]
sb.traces.get(trace_id: str) -> Trace
```

---

## Development

### Setup

```bash
# Clone repository
git clone https://github.com/StateBase/statebase-python.git
cd statebase-python

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"
```

### Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=statebase

# Run specific test
pytest tests/test_sessions.py
```

### Code Quality

```bash
# Format code
black statebase tests

# Sort imports
isort statebase tests

# Lint
flake8 statebase tests

# Type check
mypy statebase
```

---

## Support

- **Documentation**: [docs.statebase.org/python](https://docs.statebase.org/python)
- **Issues**: [GitHub Issues](https://github.com/StateBase/statebase-python/issues)
- **Discord**: [discord.gg/statebase](https://discord.gg/statebase)
- **Email**: support@statebase.org

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

<div align="center">

**[StateBase](https://statebase.org)** • **[Documentation](https://docs.statebase.org)** • **[API Reference](https://docs.statebase.org/api)**

</div>
