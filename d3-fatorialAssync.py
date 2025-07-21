import asyncio

async def criar_corrotina_fatorial(numero):
    print(f"Calculo do {numero} iniciado")
    vt = 1
    for value in range(numero):
        vt = vt * (value+1)
    await asyncio.sleep(numero)
    print(f"O numero {numero} resulto = {vt}")

async def main():
    await asyncio.gather(

        criar_corrotina_fatorial(5),
        criar_corrotina_fatorial(3),
        criar_corrotina_fatorial(2),
        criar_corrotina_fatorial(4),
        criar_corrotina_fatorial(1)

    )

asyncio.run(main())
