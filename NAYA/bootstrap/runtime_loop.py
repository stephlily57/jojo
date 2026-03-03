# bootstrap/runtime_loop.py

import asyncio


async def start_runtime():

    print("[BOOT] Runtime loop started")

    while True:
        await asyncio.sleep(1)
