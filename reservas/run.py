from app import create_app
from app.database import db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    print("=" * 60)
    print("🏨 API Reservas - Servidor Iniciado!")
    print("=" * 60)
    print("📚 Swagger:      http://localhost:5001/docs")
    print("🔗 Endpoints:")
    print("   Reservas:    http://localhost:5001/api/reservas")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5001, debug=True)
