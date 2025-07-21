"""

Primeiro, verificar se o pagamento foi aprovado;
Se o pagamento for aprovado, verificar se há estoque disponível;
Somente se houver estoque disponível, confirmar o pedido e enviá-lo para entrega;
Se o pagamento falhar ou não houver estoque, o pedido deve ser cancelado.

"""

import asyncio

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

async def criar_ordem_de_pedido(id, situacao_pagamento, situacao_estoque):
    print(f"\nPedido {id} em processamento!")
    if situacao_pagamento:
        print(f"Pagamento Aprovado para o Pedido {id}")
        if situacao_estoque:
            print(f"Estoque Disponível para o Pedido {id}")
            print(f"\nPedido {id} Confirmado para Entrega!")
        else:
            print(f"Pedido {id} cancelado devido a falta de estoque!")
    else:
        print(f"Pedido {id} cancelado devido a não confirmação do pagamento!")


async def main():

    tarefas = [
        criar_ordem_de_pedido(info["id"], info["pagamento_aprovado"], info["estoque_disponivel"])
        for info in pedidos
    ]

    await asyncio.gather(*tarefas)

asyncio.run(main())