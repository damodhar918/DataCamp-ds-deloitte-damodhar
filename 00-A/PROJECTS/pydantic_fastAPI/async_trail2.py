import asyncio

async def my_coroutine(name):
    print(f"{name} started")
    await asyncio.sleep(.01)
    print(f"{name} finished")

async def main():
    # Schedule multiple coroutines to run concurrently
    await asyncio.gather(
        my_coroutine("Coroutine 1"),
        my_coroutine("Coroutine 2"),
        my_coroutine("Coroutine 3")
    )

# Run the main coroutine
asyncio.run(main())
