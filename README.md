# 🧪 Projeto de Automação de Testes

Automação de testes para **API REST (Petstore)** e **Web E2E (SauceDemo)** utilizando Python, pytest e Selenium, com pipeline de CI via GitHub Actions.

---

## 📁 Estrutura do Projeto

```
projeto-testes/
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline CI/CD
├── api_tests/
│   ├── tests/
│   │   ├── test_pet.py         # Testes do endpoint /pet
│   │   ├── test_store.py       # Testes do endpoint /store
│   │   └── test_user.py        # Testes do endpoint /user
│   ├── utils/
│   │   ├── client.py           # Cliente HTTP reutilizável
│   │   └── helpers.py          # Factories de payloads
│   ├── conftest.py             # Fixtures compartilhadas
│   ├── pytest.ini
│   └── requirements.txt
├── web_tests/
│   ├── pages/
│   │   ├── base_page.py        # Page Object base (herança)
│   │   ├── login_page.py       # Page Object da tela de login
│   │   ├── inventory_page.py   # Page Object da listagem de produtos
│   │   ├── cart_page.py        # Page Object do carrinho
│   │   └── checkout_page.py    # Page Object do checkout
│   ├── tests/
│   │   ├── test_login.py       # Cenários de autenticação
│   │   └── test_compra.py      # Fluxo E2E de compra
│   ├── conftest.py             # Fixtures e setup do driver
│   ├── pytest.ini
│   └── requirements.txt
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.11 | Linguagem principal |
| pytest | Framework de testes |
| requests | Requisições HTTP (API) |
| Selenium 4 | Automação Web |
| pytest-html | Geração de relatórios HTML |
| GitHub Actions | Pipeline de CI/CD |

---

## ▶️ Como Executar Localmente

### Pré-requisitos
- Python 3.11+
- Google Chrome instalado
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd projeto-testes
```

### 2. Testes de API

```bash
cd api_tests
pip install -r requirements.txt
pytest
```

### 3. Testes Web

```bash
cd web_tests
pip install -r requirements.txt
pytest
```

O relatório HTML é gerado automaticamente em `report.html` dentro de cada pasta.

---

## 🔌 Cobertura — API (Petstore)

**Base URL:** `https://petstore.swagger.io/v2`

| Endpoint | Método | Cenário |
|---|---|---|
| `/pet` | POST | Criar pet |
| `/pet` | PUT | Atualizar pet |
| `/pet/{id}` | GET | Buscar por ID |
| `/pet/{id}` | DELETE | Deletar pet |
| `/pet/findByStatus` | GET | Filtrar por status |
| `/user` | POST | Criar usuário |
| `/user/{username}` | GET | Buscar usuário |
| `/user/{username}` | PUT | Atualizar usuário |
| `/user/{username}` | DELETE | Deletar usuário |
| `/user/login` | GET | Login |
| `/user/logout` | GET | Logout |
| `/store/inventory` | GET | Consultar estoque |
| `/store/order` | POST | Criar pedido |
| `/store/order/{id}` | GET | Buscar pedido |
| `/store/order/{id}` | DELETE | Cancelar pedido |

---

## 🌐 Cobertura — Web (SauceDemo)

**URL:** `https://www.saucedemo.com/`

| Cenário | Descrição |
|---|---|
| Login válido | Acesso com `standard_user` |
| Login inválido | Erro com senha errada |
| Usuário bloqueado | Mensagem de bloqueio |
| Login sem dados | Validação de campos obrigatórios |
| Fluxo E2E | Login → Produtos → Carrinho → Checkout → Confirmação |
| Produto único | Adicionar 1 produto ao carrinho |
| Múltiplos produtos | Contagem correta no carrinho |

---

## ⚙️ Pipeline CI/CD

A pipeline é executada automaticamente em todo **push** e **pull request**.

**Jobs:**
- `api-tests` — instala dependências e roda `pytest` na pasta `api_tests/`
- `web-tests` — instala Chrome + dependências e roda `pytest` na pasta `web_tests/`

Os relatórios HTML são publicados como **Artifacts** no GitHub Actions após cada execução.

---

## 🏗️ Design Patterns Utilizados

- **Page Object Model (POM):** cada tela do SauceDemo possui sua própria classe em `pages/`, separando a lógica de navegação dos testes.
- **Base Page:** herança elimina duplicação dos métodos `find`, `click` e `type`.
- **Fixtures com teardown:** os testes de API criam e limpam seus próprios dados via fixtures do pytest.
- **Factory functions:** `helpers.py` gera payloads dinâmicos para evitar colisão de dados entre testes.
