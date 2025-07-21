"""

O sistema deve ter três sensores, que coletam e exibem dados em intervalos diferentes:

Sensor de temperatura: Atualiza os dados a cada 2 segundos.
Sensor de umidade: Atualiza os dados a cada 3 segundos.
Sensor de qualidade do ar: Atualiza os dados a cada 5 segundos.

"""

import asyncio
import random
import time

class GerenciadorSensores:
    def __init__(self):
        self.sensores = {
            'temperatura':{'frequencia': 2, 'atual':40, 'sigla':'°C','variacao':4},
            'umidade':{'frequencia':3, 'atual': 60, 'sigla':'%', 'variacao':5},
            'qualidade_do_ar':{'frequencia':5, 'atual':'boa', 'variacao':0,'possibilidades':['ruim','boa','perfeita']}
        }
        self.tempo = time.monotonic()

    async def criar_rotina(self, nome):
        while True:
            await asyncio.sleep(self.sensores[nome]['frequencia'])
            tempo = time.monotonic() - self.tempo

            if self.sensores[nome]['variacao'] != 0:
                self.sensores[nome]['atual'] += random.randint(-self.sensores[nome]['variacao'], self.sensores[nome]['variacao'])
                print(f'[{tempo:.0f}s]{nome}: {self.sensores[nome]['atual']}{self.sensores[nome]['sigla']}')
            else:
                self.sensores[nome]['atual'] = random.choice(self.sensores[nome]['possibilidades'])
                print(f'[{tempo:.0f}s]{nome}: {self.sensores[nome]['atual']}')



async def main():
    gerenciador = GerenciadorSensores()
    tarefas = [
        gerenciador.criar_rotina(nome)
        for nome in gerenciador.sensores
    ]
    await asyncio.gather(*tarefas)


asyncio.run(main())
