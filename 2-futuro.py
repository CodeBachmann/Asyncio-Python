import asyncio
import time


# para pegar o resultado do future é necessário utilizar o .result()
async def criar_corrotina(futuro, numero):
    print(f"Iniciada a {numero}°")
    await asyncio.sleep(2)
    futuro.set_result(3)
    print(f"Finalizada a {numero}°, com o valor de futuro {futuro.result()}")   

async def criar_corrotina_2(futuro, numero):
    print(f"Iniciada a {numero}°")
    await futuro
    print(f"Finalizada a {numero}°, futuro * numero = {futuro.result() * numero}")

async def main():
    futuro = asyncio.Future()
    t1 = asyncio.create_task(criar_corrotina(futuro, 1))
    t2 = asyncio.create_task(criar_corrotina_2(futuro, 2))
    await t1
    await t2

asyncio.run(main())