import os
import asyncio
from statebase import StateBase, AsyncStateBase
from dotenv import load_dotenv

load_dotenv("../statebase-test/.env")

API_KEY = os.getenv("STATEBASE_API_KEY")
BASE_URL = os.getenv("STATEBASE_API_URL", "https://api.statebase.org")

def test_sync_fork():
    print("--- Testing Sync Fork ---")
    sb = StateBase(api_key=API_KEY, base_url=BASE_URL)
    
    # 1. Create source session
    source = sb.sessions.create(agent_id="py-sync-fork-test", initial_state={"count": 1})
    print(f"[+] Source: {source.id}")
    
    # 2. Fork it
    forked = sb.sessions.fork(source.id)
    print(f"[+] Forked: {forked.id}")
    
    assert forked.id != source.id
    assert forked.state["count"] == 1
    assert forked.metadata.get("forked_from") == source.id
    
    print("[+] Sync Fork Passed")
    sb.close()

async def test_async_fork():
    print("\n--- Testing Async Fork ---")
    async with AsyncStateBase(api_key=API_KEY, base_url=BASE_URL) as asb:
        # 1. Create source
        source = await asb.sessions.create(agent_id="py-async-fork-test", initial_state={"step": "ready"})
        print(f"[+] Source: {source.id}")
        
        # 2. Update state to version 1
        await asb.sessions.update_state(source.id, state={"step": "in_progress"}, reasoning="Advancing step")
        
        # 3. Fork latest
        forked = await asb.sessions.fork(source.id)
        print(f"[+] Forked: {forked.id}")
        
        assert forked.state["step"] == "in_progress"
        
        print("[+] Async Fork Passed")

if __name__ == "__main__":
    if not API_KEY:
        print("Error: STATEBASE_API_KEY not set")
    else:
        test_sync_fork()
        asyncio.run(test_async_fork())
