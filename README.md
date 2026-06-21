# 🚀 PROJETO-B2BFLOW

Este repositório contém a solução para o desafio técnico do processo seletivo para a vaga de **Estágio em Desenvolvimento Python** na **b2bflow**.

O objetivo do projeto é desenvolver uma automação em Python capaz de:

- Consultar contatos armazenados no Supabase;
- Gerar mensagens personalizadas;
- Enviar mensagens automaticamente utilizando a Z-API.

---

## 🛠️ Tecnologias e Dependências

- **Python 3.10+**
- **Supabase** — Integração com o banco de dados PostgreSQL do Supabase.
- **Requests** — Realização de chamadas HTTP para a Z-API.
- **Python-dotenv** — Gerenciamento seguro de variáveis de ambiente.

---

## 📁 Estrutura do Projeto

```text
PROJETO-B2BFLOW/
├── services/
│   ├── supabase_service.py   # Gerencia a conexão e as consultas ao Supabase
│   └── zapi_service.py       # Gerencia as requisições HTTP para a Z-API
├── .env                      # Variáveis de ambiente (ignorado pelo Git)
├── .gitignore                # Proteção de arquivos locais e credenciais
├── main.py                   # Ponto de entrada da aplicação
├── README.md                 # Documentação do projeto
└── requirements.txt          # Dependências do projeto
```

---

## 🗄️ Configuração do Banco de Dados (Supabase)

Crie uma tabela chamada `contatos` no Supabase executando o script abaixo no **SQL Editor**:

```sql
CREATE TABLE contatos (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now()) NOT NULL
);
```

Utilize no máximo **3 registros**, conforme as regras do desafio.

```sql
INSERT INTO contatos (nome, telefone) VALUES
('Teste1', '5511999999999'),
('Teste2', '5511988888888'),
('Teste3', '5511977777777');
```

---

## ⚙️ Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

```env
SUPABASE_URL=sua_url_supabase
SUPABASE_KEY=sua_chave_supabase

ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
```

> ⚠️ Nunca compartilhe suas credenciais e não envie o arquivo `.env` para o GitHub.

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone <https://github.com/Lucastkx/projeto-b2bflow.git>
cd PROJETO-B2BFLOW
```


### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação

```bash
python main.py
```

---

## 🔄 Fluxo de Execução

1. A aplicação estabelece conexão com o banco de dados Supabase.
2. Os contatos cadastrados são consultados.
3. Uma mensagem personalizada é gerada para cada contato.
4. A Z-API recebe a solicitação de envio da mensagem.
5. O resultado de cada envio é exibido no terminal.

---

## 📌 Requisitos do Projeto

- Consultar contatos diretamente do Supabase.
- Personalizar mensagens com o nome do contato.
- Integrar com a Z-API para envio das mensagens.
- Utilizar variáveis de ambiente para proteger credenciais.
- Organizar o código de forma modular e reutilizável.

---

## 👨‍💻 Autor

Desenvolvido por **Lucas** como parte do desafio técnico para a vaga de **Estágio em Desenvolvimento Python** na **b2bflow**.

- GitHub: https://github.com/Lucastkx
