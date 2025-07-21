import asyncio
import random

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = {}

    async def criar_tarefa(self, id):
        tempo = random.randint(1,7)
        self.tarefas[id] = {'status': 'ESPERA', 'tempo_restante':tempo, 'tempo_total':tempo}
    
    async def rodar_tarefa(self, id):
        if self.tarefas[id]['status'] != 'FINALIZADA':
            if self.tarefas[id]['status'] == 'ESPERA':
                self.tarefas[id]['status'] = 'PROCESSANDO'
            if self.tarefas[id]['tempo_restante'] > 0:
                self.tarefas[id]['tempo_restante'] -= 1
            if self.tarefas[id]['tempo_restante'] == 0:
                self.tarefas[id]['status'] = 'FINALIZADA'


async def main():
    ids = [123, 456, 888, 923, 173]
    gerenciador = GerenciadorDeTarefas()

    for i in ids:
        await gerenciador.criar_tarefa(i)
    
    while True:

        printstr = '['
        for tarefa, info in gerenciador.tarefas.items():
            printstr += f'[{info['status']}]'
        printstr += ']'
        print(printstr)

        tarefas = [
            gerenciador.rodar_tarefa(id)
            for id in gerenciador.tarefas
        ]
        await asyncio.gather(*tarefas)
        await asyncio.sleep(1)
        


asyncio.run(main())