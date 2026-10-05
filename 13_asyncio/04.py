import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking stock for {item}")
    time.sleep(2)  # Simulate a blocking I/O operation
    print(f"Stock check for {item} is done")
    return f"{item} is in stock"

async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, check_stock, "NVidia")
        print(result)

asyncio.run(main())