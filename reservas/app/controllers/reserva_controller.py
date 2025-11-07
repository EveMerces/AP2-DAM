from flask import Blueprint, request, jsonify
from app.models.reserva import Reserva
from app.database import db
import requests
import os

# Prefixa as rotas com /api/reservas para manter consistencia com os outros serviços
reserva_bp = Blueprint('reservas', __name__, url_prefix='/api/reservas')

# Usa a variável de ambiente (definida em docker-compose). Ex.: http://api-colegio:5000/api
GERENCIAMENTO_API_URL = os.environ.get('GERENCIAMENTO_API_URL', 'http://api-colegio:5000/api')


@reserva_bp.route('/', methods=['POST'])
def criar_reserva():
    data = request.json
    turma_id = data.get('turma_id')

    if not turma_id:
        return jsonify({"erro": "turma_id e obrigatorio"}), 400

    # Valida turma no microsserviço de gerenciamento
    try:
        response = requests.get(f"{GERENCIAMENTO_API_URL}/turmas/{turma_id}")
    except requests.exceptions.RequestException:
        return jsonify({"erro": "Nao foi possivel conectar ao servico de gerenciamento"}), 503

    if response.status_code != 200:
        return jsonify({"erro": "Turma inválida"}), 400

    reserva = Reserva(
        num_sala=data['num_sala'],
        lab=data.get('lab', False),
        data=data.get('data'),
        turma_id=turma_id
    )
    db.session.add(reserva)
    db.session.commit()
    return jsonify(reserva.to_dict()), 201


@reserva_bp.route('/', methods=['GET'])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([r.to_dict() for r in reservas])


@reserva_bp.route('/<int:id>', methods=['GET'])
def obter_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    return jsonify(reserva.to_dict())


@reserva_bp.route('/<int:id>', methods=['PUT'])
def atualizar_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    data = request.json
    reserva.num_sala = data.get('num_sala', reserva.num_sala)
    reserva.lab = data.get('lab', reserva.lab)
    reserva.data = data.get('data', reserva.data)
    db.session.commit()
    return jsonify(reserva.to_dict())


@reserva_bp.route('/<int:id>', methods=['DELETE'])
def deletar_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    db.session.delete(reserva)
    db.session.commit()
    return jsonify({"mensagem": "Reserva deletada com sucesso!"})
