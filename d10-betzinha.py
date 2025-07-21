"""

Criar um sistema onde cada aposta é armazenada em um asyncio.Future() e só é definida após um tempo determinado;
Simular três jogos diferentes, nos quais os apostadores fizeram suas apostas;
O resultado de cada jogo será "Vitória do Time A", "Vitória do Time B" ou "Empate", escolhido aleatoriamente;
Cada jogo levará entre 2 e 8 segundos para ter seu resultado definido;
O programa não deve esperar cada aposta individualmente, ele deve registrar todas e continuar rodando;
Assim que um resultado for definido, ele deve ser exibido imediatamente;
Quando todos os jogos forem finalizados, o programa exibe a mensagem "Todos os resultados foram revelados!".

"""

import asyncio
import random

class Bet:
    def __init__(self):
        self.resultados = ["Vitória do Time A", "Vitória do Time B", "Empate"]
        self.jogos= [
            {"id": 1, "times": "Flamengo vs Palmeiras", 'resultado': asyncio.Future()},
            {"id": 2, "times": "São Paulo vs Corinthians", 'resultado': asyncio.Future()},
            {"id": 3, "times": "Grêmio vs Internacional", 'resultado': asyncio.Future()},
        ]

    async def apostar(self, jogo, escolha):
        print(f'Jogo {self.jogos[jogo]['times']} Iniciado!')
        await self.jogos[jogo]['resultado']
        resultado = int(self.jogos[jogo]['resultado'].result())
        if self.resultados[resultado] == self.resultados[escolha]:
            print(f'Parabéns você acertou o resultado do jogo {self.jogos[jogo]['times']}! {self.resultados[resultado]}')
        else:
            print(f'Infelizmente o resultado do jogo {self.jogos[jogo]['times']} foi {self.resultados[resultado]}')

    async def sortear_jogo(self, jogo):
        tempo = random.randint(2,8)
        await asyncio.sleep(tempo)
        escolhaAleatoria = random.randint(0,2)
        self.jogos[jogo]['resultado'].set_result(escolhaAleatoria)


async def main():
    bet = Bet()
    apostas = {
        0:0,
        1:1,
        2:0
    }
    tarefas_apostas = [
        bet.apostar(jogo, escolha)
        for jogo, escolha in apostas.items()
    ]
    tarefas_jogos = [
        bet.sortear_jogo(jogo['id']-1)
        for jogo in bet.jogos
    ]
    await asyncio.gather(*tarefas_apostas, *tarefas_jogos)

asyncio.run(main())