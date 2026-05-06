# 🧪 Projeto de Automação de Testes — API e Web

Automação de testes em Python com dois módulos independentes: testes de **API REST (Petstore)** e testes **Web E2E (SauceDemo)**, utilizando boas práticas como Page Object Model, fixtures com teardown e pipeline de CI/CD.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.11+ | Linguagem base |
| Pytest | 8.2.0 | Framework de testes |
| Requests | 2.31.0 | Requisições HTTP (testes de API) |
| Selenium | 4.21.0 | Automação de browser (testes Web) |
| pytest-html | 4.1.1 | Geração de relatórios HTML |
| GitHub Actions | — | CI/CD |

---

## 📁 Estrutura do Projeto

```
testes-automacao/
├── .github/
│   └── workflows/
│       └── ci.yml                  # Pipeline CI/CD
├── api_tests/
│   ├── utils/
│   │   ├── client.py               # Cliente HTTP reutilizável
│   │   └── helpers.py              # Factories de payloads dinâmicos
│   ├── tests/
│   │   ├── test_pet.py             # Testes do endpoint /pet
│   │   ├── test_store.py           # Testes do endpoint /store
│   │   └── test_user.py            # Testes do endpoint /user
│   ├── conftest.py                 # Fixtures compartilhadas com teardown
│   ├── pytest.ini
│   └── requirements.txt
├── web_tests/
│   ├── pages/
│   │   ├── base_page.py            # Page Object base (herança)
│   │   ├── login_page.py           # Page Object da tela de login
│   │   ├── inventory_page.py       # Page Object da listagem de produtos
│   │   ├── cart_page.py            # Page Object do carrinho
│   │   ├── checkout_page.py        # Page Object do checkout
│   │   └── product_page.py         # Page Object do detalhe do produto
│   ├── tests/
│   │   ├── test_login.py           # Cenários de autenticação
│   │   ├── test_compra.py          # Fluxo E2E de compra
│   │   ├── test_carrinho.py        # Cenários do carrinho
│   │   └── test_inventario.py      # Cenários de listagem e ordenação
│   ├── conftest.py                 # Fixtures e setup do driver
│   ├── pytest.ini
│   └── requirements.txt
├── prints/                         # Prints do funcionamento
├── Makefile                        # Atalhos de execução
└── README.md
```

---

## ▶️ Como Executar Localmente

### Pré-requisitos
- Python 3.11+
- Google Chrome instalado
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/WalterdesJunior/testes-automacao.git
cd testes-automacao
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

| Módulo | Testes |
|---|---|
| Pet | Criar, buscar por ID, atualizar, filtrar por status, deletar |
| Store | Buscar inventário, criar pedido, buscar pedido por ID, deletar pedido |
| User | Criar, buscar por username, atualizar, login, logout, deletar |

---

## 🌐 Cobertura — Web (SauceDemo)

**URL:** `https://www.saucedemo.com/`

| Teste | Descrição |
|---|---|
| `test_login_com_credenciais_validas` | Verifica acesso com usuário padrão |
| `test_login_com_senha_errada` | Valida mensagem de erro de autenticação |
| `test_login_usuario_bloqueado` | Verifica mensagem de bloqueio do usuário |
| `test_login_sem_credenciais` | Valida campos obrigatórios no login |
| `test_fluxo_completo_compra` | Fluxo E2E: Login → Adicionar → Carrinho → Checkout → Sucesso |
| `test_remover_produto_do_carrinho` | Valida remoção de itens e atualização do contador |
| `test_ordenar_produtos_por_preco_menor_para_maior` | Valida ordenação por preço crescente |

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
