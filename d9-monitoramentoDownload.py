"""

Baixar cinco arquivos diferentes, cada um com um tamanho aleatório entre 10MB e 50MB;
A velocidade de download de cada arquivo é de 5MB por segundo;
Exibir mensagens de progresso a cada segundo, mostrando quanto já foi baixado de cada arquivo;
Exibir uma mensagem quando cada download for concluído;
Aguarde todos os downloads antes de encerrar o programa.

"""

import asyncio

class GerenciadorDownloads:
    def __init__(self):
        self.downloads = {
            'arq1.txt':50,
            'arq2.txt':45,
            'arq3.txt':25,
            'arq4.txt':10,
            'arq5.txt':40
        }

    async def criar_download(self, arquivo):
        baixado = 0
        print(f"Download do {arquivo} Iniciado!")
        while baixado+5 < self.downloads[arquivo]:
            baixado += 5
            await asyncio.sleep(1)
            print(f'Download do {arquivo} {baixado}/{self.downloads[arquivo]}MB')

        await asyncio.sleep(1)
        print(f"Download do {arquivo} Finalizado!")


async def main():

    gerenciador = GerenciadorDownloads()
    tarefas =[
        gerenciador.criar_download(arquivo)
        for arquivo in gerenciador.downloads
    ]
    await asyncio.gather(*tarefas)

asyncio.run(main())