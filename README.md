Microsserviços Colégio Porto — Instruções objetivas

Integrantes: Anna Julia Higa Farincho, Evelyn Mercês, Leticia Macedo - SI3A
### Sistema de Gerenciamento Escolar

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.0.5-red.svg)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)]()

Propósito
Construir 3 microsserviços em Flask que, juntos, permitam gerenciar Professores, Turmas, Alunos, Reservas de sala, Atividades e Notas. Regras principais:
- Serviço Gerenciamento (api-colegio): cadastra e gerencia Professores, Turmas e Alunos. NÃO gerencia Reservas nem Atividades; apenas fornece IDs.
- Serviço Reservas: gerencia reservas de salas; precisa apenas do `turma_id` para criar reservas.
- Serviço Atividades: gerencia atividades e notas; precisa de `professor_id` e `turma_id` para criar atividades/registrar notas.

Requisitos técnicos (implementados)
- Cada serviço com estrutura MVC (models, controllers, swagger).
- Persistência local por serviço com SQLite + SQLAlchemy.
- Rotas CRUD usando GET/POST/PUT/DELETE.
- Documentação Swagger exposta em `/docs` para cada serviço.
- Comunicação síncrona entre serviços usando `requests` e a variável de ambiente `GERENCIAMENTO_API_URL`.
- Orquestração com `docker-compose.yml` na raiz (levanta os 3 serviços e cria rede/volumes).

Portas (padrão)
- Gerenciamento (api-colegio): 5000
- Reservas (reservas): 5001
- Atividades/Notas (atividades): 5002

Como rodar (rápido e direto)
Pré-requisito: Docker Desktop rodando.

1) Abra um terminal na pasta do projeto (onde está `docker-compose.yml`):

```powershell
cd "C:\Users\<seu_usuario>\OneDrive\Desktop\AP2- API & Microserviços\AP2-DAM"
docker compose up --build
```

2) Verifique acessos (após subir):

- Gerenciamento (Swagger):  http://localhost:5000/docs
- Reservas   (Swagger):     http://localhost:5001/docs
- Atividades (Swagger):     http://localhost:5002/docs

Rotas base (exemplos)
- GET/POST/PUT/DELETE http://localhost:5000/api/professores
- GET/POST/PUT/DELETE http://localhost:5000/api/turmas
- GET/POST/PUT/DELETE http://localhost:5000/api/alunos
- GET/POST/PUT/DELETE http://localhost:5001/api/reservas
- GET/POST/PUT/DELETE http://localhost:5002/api/atividades
- GET/POST/PUT/DELETE http://localhost:5002/api/notas

Sequência mínima de teste (para mostrar integração)
1. Criar um professor (POST /api/professores) → guardar `professor_id`.
2. Criar uma turma vinculada (POST /api/turmas com `professor_id`) → guardar `turma_id`.
3. Criar reserva (POST /api/reservas com `turma_id`) → deve retornar 201.
4. Criar atividade (POST /api/atividades com `turma_id` e `professor_id`) → deve retornar 201.
5. Criar nota (POST /api/notas com `aluno_id`, `atividade_id`, `nota`) → deve retornar 201.

Observações importantes (para avaliador)
- O serviço de Gerenciamento é independente: ele NÃO chama nem conhece lógica de Reservas/Atividades. Os outros serviços fazem validações consultando o Gerenciamento via HTTP.
- Cada serviço persiste seus dados em SQLite local (arquivos dentro das pastas dos serviços / volumes Docker).
- Para rodar sem Docker: abra 3 terminais, instale dependências (`pip install -r requirements.txt`) em cada serviço e rode `python run.py`. Configure `GERENCIAMENTO_API_URL` para `http://localhost:5000/api` antes de iniciar `reservas` e `atividades`.

