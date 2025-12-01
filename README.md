# siscadv

Sistema de Cadastramento de Visitantes

## Requisitos confirmados
- Disponibilizar uma API HTTP capaz de registrar visitantes e listar os registros abertos nesta instância.
- Endpoints mínimos: `GET /health` para verificação de disponibilidade, `POST /visitors` para cadastro e `GET /visitors` para listagem.
- O cadastro de visitante deve validar nome, documento e motivo da visita como textos não vazios, retornando a data/hora de registro atribuída pelo servidor.
- Testes automatizados devem cobrir o fluxo de cadastro e listagem.

## Configuração do ambiente
1. Crie e ative um ambiente virtual Python 3.11+ (opcional):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução da aplicação
Execute o servidor de desenvolvimento com Uvicorn:
```bash
uvicorn siscadv.main:app --reload --port 8000
```
A aplicação ficará disponível em `http://localhost:8000`. A interface interativa da API pode ser acessada em `http://localhost:8000/docs`.

## Testes
Rode a suíte de testes com pytest:
```bash
pytest
```

## Estrutura do projeto
```
.
├── requirements.txt
├── src/
│   └── siscadv/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_visitors.py
└── README.md
```
