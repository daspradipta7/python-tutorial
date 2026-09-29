import asyncio

async def brew_chai(name, sleep):
    print(f"Brewing {name}")
    await asyncio.sleep(sleep)
    print(f"Brewing {name} is done")

async def main():
   await asyncio.gather(
        brew_chai("Masala Chai", 1),
        brew_chai("Elachi Chai", 3),
        brew_chai("Irani Chai", 2),
    )

asyncio.run(main())