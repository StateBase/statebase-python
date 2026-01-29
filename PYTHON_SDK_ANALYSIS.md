# StateBase Python SDK: Technical Architecture

The StateBase Python SDK is the primary reference implementation for integrating high-performance agent state and memory. It is designed for both high-concurrency production servers and rapid developer prototyping.

---

## 🏗️ 1. Dual-Runtime Architecture

The SDK provides two distinct entry points to support different Python concurrency models:

### **Synchronous Client (`StateBase`)**
- **Library**: `httpx.Client`
- **Use Case**: Simple scripts, notebooks (Jupyter/Colab), and legacy synchronous web frameworks.
- **Design**: Thread-safe connection pooling for basic multi-threaded environments.

### **Asynchronous Client (`AsyncStateBase`)**
- **Library**: `httpx.AsyncClient`
- **Use Case**: FastAPI, Sanic, and high-performance AI agent loops.
- **Context Management**: Implements `async with` protocols for automatic socket cleanup, preventing resource leaks in high-scale production.

---

## 🧠 2. Schema Enforcement (Pydantic v2)

The Python SDK utilizes **Pydantic** (`models.py`) for all data transitions:
- **Strict Validation**: Every API response is parsed and validated against strictly defined schemas (`SessionResponse`, `TurnResponse`, `MemoryResponse`). This provides the developer with rich IDE autocomplete and runtime type-safety.
- **Polymorphic Convenience**: Methods like `add_turn` automatically detect if the input is a raw `str` and wrap it into the required JSON structure (`{"type": "text", "content": "..."}`) before transmission.

---

## ⚙️ 3. CORE FEATURES & NAMESPACING

To maintain a clean API surface as the platform grows, the Python SDK uses a **Namespaced Interface**:

| Namespace | Methods | Description |
| :--- | :--- | :--- |
| `client.sessions` | `create`, `get`, `list`, `add_turn` | Complete management of the agent conversation loop. |
| `client.memory` | `add`, `search`, `delete` | Direct access to semantic memory and vector search. |
| `client.state` | `update_state`, `get_context` | Advanced state manipulation and context retrieval for LLMs. |

### **Special Highlight: `get_context`**
This high-level helper allows a single call to fetch the agent's current state, relevant semantic memories (via vector search), and recent conversation turns in one optimized packet.

---

## 📊 4. Technical Performance Audit

- **HTTP/2 Support**: Inherits `httpx` support for HTTP/2, reducing handshake latency when communicating with the StateBase cluster.
- **Serialization**: Efficient JSON serialization using `pydantic`'s native optimizations.
- **Timeout Management**: Global defaults are set to 30.0s, but can be overridden per-request or per-client instance.

---

## 🏁 5. Production Readiness
- **Python Compatibility**: `>= 3.9`
- **Dependency Footprint**: Minimal (only `httpx`, `pydantic`, and `typing-extensions`).
- **Update Cycle**: Aligned with StateBase v1 API specifications.

**Analysis Date**: 2026-01-29  
**Version**: 0.1.1
