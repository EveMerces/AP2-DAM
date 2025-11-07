from app import create_app

app = create_app()

if __name__ == '__main__':
    print("=" * 60)
    print("📝 API Atividades/Notas - Servidor Iniciado!")
    print("=" * 60)
    print("📚 Swagger:      http://localhost:5002/docs")
    print("🔗 Endpoints:")
    print("   Atividades:  http://localhost:5002/api/atividades")
    print("   Notas:       http://localhost:5002/api/notas")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5002)
