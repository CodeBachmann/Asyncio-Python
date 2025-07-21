import asyncio

async def criar_corrotina(nome):
    print(f"Corrotina {nome} Executada!")
    await asyncio.sleep(2) 
    print(f"Corrotina {nome} Finalizada!")

async def main():
    await asyncio.gather(

        criar_corrotina("download"),
        criar_corrotina("analise")

    )

asyncio.run(main())