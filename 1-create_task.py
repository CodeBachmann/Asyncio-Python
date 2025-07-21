import asyncio
import time

async def criar_corrotina(numero):
    print(f"Iniciada a {numero}°")
    await asyncio.sleep(2)
    print(f"Finalizada a {numero}°")

async def main():

    t1 = asyncio.create_task(criar_corrotina(1))
    t2 = asyncio.create_task(criar_corrotina(2))
    await t1
    await t2

asyncio.run(main())