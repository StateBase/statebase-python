# StateBase SDKs

This repository contains the official SDKs for StateBase API.

## 📦 Python SDK

### Installation
```bash
cd state-base-api-client
pip install -e .
```

### Usage
```python
from state_base_api_client import Client
from state_base_api_client.api.sessions import create_session_v1_sessions_post
from state_base_api_client.models import SessionCreateRequest

# Initialize client
client = Client(base_url="https://api.statebase.org")
client = client.with_headers({"X-API-Key": "your-api-key"})

# Create a session
request = SessionCreateRequest(
    agent_id="my-agent",
    initial_state={"user_name": "Alice"}
)
session = create_session_v1_sessions_post.sync(client=client, body=request)

print(f"Created session: {session.id}")
```

**Features:**
- ✅ Auto-generated from OpenAPI spec (always in sync)
- ✅ Full type hints with Pydantic
- ✅ Sync and async support
- ✅ Complete API coverage

## 📦 TypeScript SDK

### Installation
```bash
cd ../statebase-ts-sdk
npm install
npm run build
```

### Usage
```typescript
import StateBase from './src/index';

// Initialize client
const client = new StateBase('your-api-key', 'http://api.statebase.org');

// Create a session
const session = await client.createSession({
  agent_id: 'my-agent',
  initial_state: { user_name: 'Alice' }
});

console.log(`Created session: ${session.id}`);
```

**Features:**
- ✅ Auto-generated TypeScript types from OpenAPI
- ✅ Clean, intuitive API
- ✅ Full type safety
- ✅ Promise-based async

## 🔄 Regenerating SDKs

When the API changes, regenerate the SDKs:

### TypeScript Types
```bash
cd statebase-ts-sdk
npx openapi-typescript ../statebase/openapi.json -o src/schema.ts
```

### Python Client
```bash
cd statebase-py-sdk
python -m openapi_python_client generate --path ../statebase/openapi.json
```

## 📚 Documentation

- API Docs: http://api.statebase.org/docs
- Full Documentation: https://docs.statebase.org

## License

MIT
