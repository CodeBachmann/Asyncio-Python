import asyncio

class Notificador:
    def __init__(self):
        self.vips_em_execucao = 0

    async def criarNotificacao(self, vip, status, notificacao, nome):
        if vip and status:
            self.vips_em_execucao += 1
            await asyncio.sleep(2)
            print(f"Notificacao {notificacao} para VIP {nome} enviada!")
            self.vips_em_execucao -= 1
        elif status:
            await asyncio.sleep(1)
            while self.vips_em_execucao != 0:
                print("aguardando o envio de todas as notificações VIP")
                await asyncio.sleep(1)

            print(f"Notificao {notificacao} para {nome} enviada!")
        else:
            print(f"Notificao {notificacao} não enviáda pois {nome} desativou")


async def main():
    notificador = Notificador()
    clientes = {
        "Carla": {"VIP": True, "STATUS": True},
        "Roberto": {"VIP": False, "STATUS": True},
        "Anderson": {"VIP": True, "STATUS": False},
        "Maria": {"VIP": False, "STATUS": False},
    }

    tarefas = [
        notificador.criarNotificacao(info["VIP"], info["STATUS"], "TIM", nome)
        for nome, info in clientes.items()
    ]

    await asyncio.gather(*tarefas)
    print("Todos os pedidos foram processados!")

asyncio.run(main())