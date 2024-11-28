carros = [
    {
        "id": 1,
        "marca": "Toyota",
        "modelo": "Corolla",
        "ano": 2022,
        "preco": 120000,
        "cor": "Branco",
        "disponivel": True
    },
    {
        "id": 2,
        "marca": "Honda",
        "modelo": "Civic",
        "ano": 2023,
        "preco": 130000,
        "cor": "Preto",
        "disponivel": True
    },
    {
        "id": 3,
        "marca": "Chevrolet",
        "modelo": "Onix",
        "ano": 2021,
        "preco": 80000,
        "cor": "Vermelho",
        "disponivel": False
    },
    {
        "id": 4,
        "marca": "Ford",
        "modelo": "Fiesta",
        "ano": 2019,
        "preco": 75000,
        "cor": "Azul",
        "disponivel": True
    },
    {
        "id": 5,
        "marca": "Volkswagen",
        "modelo": "Gol",
        "ano": 2020,
        "preco": 70000,
        "cor": "Prata",
        "disponivel": True
    }
]


def listar_carros():
    return carros


def obter_carro_por_id(carro_id):
    for carro in carros:
        if carro['id'] == carro_id:
            return carro
    return None


def adicionar_carro(novo_carro):
    novo_carro['id'] = len(carros) + 1
    carros.append(novo_carro)
    return novo_carro


def atualizar_carro(carro_id, dados_atualizados):
    carro = obter_carro_por_id(carro_id)
    if carro:
        carro.update(dados_atualizados)
        return carro
    return None


def deletar_carro(carro_id):
    carro = obter_carro_por_id(carro_id)
    if carro:
        carros.remove(carro)
        return True
    return False
