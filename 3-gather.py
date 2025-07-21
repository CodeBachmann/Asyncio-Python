import asyncio
import time

async def criar_corrotina(numero, tempo):
    print(f"Iniciada a {numero}°")
    await asyncio.sleep(tempo)
    print(f"Finalizada a {numero}°")

async def main():
    await asyncio.gather(
        criar_corrotina(1, 2),
        criar_corrotina(2, 3),
        criar_corrotina(3, 1)

    )

asyncio.run(main())