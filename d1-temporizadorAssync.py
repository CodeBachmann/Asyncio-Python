import asyncio
import random


async def criar_corrotina_de_tempo(numero_da_tarefa):
    print(f"Tarefa numero {numero_da_tarefa} executada!")
    tempo = random.randint(1, 5)
    await asyncio.sleep(tempo)
    print(f"Tarefa numero {numero_da_tarefa} finalizada! \nTempo decorrido {tempo}s")

async def main():
    await asyncio.gather(

        criar_corrotina_de_tempo(1),
        criar_corrotina_de_tempo(2),
        criar_corrotina_de_tempo(3)

    )

asyncio.run(main())