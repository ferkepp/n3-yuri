
from flask import Flask, jsonify, request
from bd import listar_carros, obter_carro_por_id, adicionar_carro, atualizar_carro, deletar_carro

app = Flask(__name__)

@app.route("/carros", methods=["GET"])
def listar_todos_os_carros():
    carros = listar_carros()
    return jsonify(carros), 200


@app.route("/carros/<int:carro_id>", methods=["GET"])
def buscar_carro_por_id(carro_id):
    carro = obter_carro_por_id(carro_id)
    if carro:
        return jsonify(carro), 200
    return jsonify({"erro": "Carro não encontrado"}), 404


@app.route("/carros", methods=["POST"])
def adicionar_novo_carro():
    dados = request.get_json()
    if not dados.get("marca") or not dados.get("modelo"):
        return jsonify({"erro": "Os campos 'marca' e 'modelo' são obrigatórios"}), 400

    novo_carro = adicionar_carro(dados)
    return jsonify(novo_carro), 201


@app.route("/carros/<int:carro_id>", methods=["PUT"])
def atualizar_carro_existente(carro_id):
    dados = request.get_json()
    carro_atualizado = atualizar_carro(carro_id, dados)
    if carro_atualizado:
        return jsonify(carro_atualizado), 200
    return jsonify({"erro": "Carro não encontrado"}), 404

@app.route("/carros/<int:carro_id>", methods=["DELETE"])
def deletar_carro_por_id(carro_id):
    if deletar_carro(carro_id):
        return jsonify({"mensagem": "Carro deletado com sucesso"}), 200
    return jsonify({"erro": "Carro não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
