
import asyncio, json, websockets

async def main():
    async with websockets.connect("ws://127.0.0.1:8765") as ws:
        async for msg in ws:
            data = json.loads(msg)
            print(f"[{data['view']}] {data['event']}")

if __name__ == "__main__":
    asyncio.run(main())
