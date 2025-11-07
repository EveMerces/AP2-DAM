from app import create_app

app = create_app()

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 API Colégio Porto - Servidor Iniciado!")
    print("=" * 60)
    print("� Swagger:      http://localhost:5000/docs")
    print("� Endpoints:")
    print("   Alunos:      http://localhost:5000/api/alunos")
    print("   Professores: http://localhost:5000/api/professores")
    print("   Turmas:      http://localhost:5000/api/turmas")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)