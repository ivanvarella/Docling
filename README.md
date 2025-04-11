# Docling 📄🤖

Este repositório apresenta exemplos práticos de **extração e conversão de documentos** (HTML e PDF) utilizando a biblioteca **Docling**, com integração a **Modelos de Linguagem (LLMs)** via **LangChain** e comparações com abordagens tradicionais como `BeautifulSoup` e `requests`.

## Toda a inspiração foi retirada de: https://www.youtube.com/watch?v=IGDaXFmb1NU

## 🔍 Objetivo

Demonstrar diferentes formas de:

- Extrair conteúdo de páginas HTML (online e locais)
- Analisar e converter documentos PDF (online e locais)
- Gerar saída em Markdown
- Contar tokens dos textos com suporte a LLMs (como GPT)
- Comparar Docling com métodos tradicionais (BeautifulSoup + requests)

---

## 📁 Estrutura do Projeto
```plaintext
.
├── pdfs
│   └── International-Business-in-the-Digital-Age.pdf_MD.md
└── scratch
    ├── 2504.03277v1-with-image-refs.md
    ├── 2504.03277v1-with-image-refs_artifacts
    ├── 2504.03277v1-with-images.md
    ├── International-Business-in-the-Digital-Age-with-image-refs.md
    ├── International-Business-in-the-Digital-Age-with-image-refs_artifacts
    └── International-Business-in-the-Digital-Age-with-images.md
```

## ✅ Pré-requisitos

- Python 3.10+
- Ambiente virtual recomendado

---

## 🧪 Instalação

```bash
git clone https://github.com/ivanvarella/Docling.git
cd Docling
python -m venv .venv
source .venv/bin/activate     # Linux/macOS
# .venv\Scripts\activate.bat  # Windows

pip install -r requirements.txt
```

Renomeie o arquivo .env_exemple para .env e altere com sua chave de API da OpenAI:
OPENAI_API_KEY='Sua API Key da OpenAI'

# 🔄 Comparação: Docling vs BeautifulSoup

| Recurso | BeautifulSoup | Docling |
|---------|---------------|---------|
| Propósito principal | Análise HTML/XML | Processamento de documentos |
| Facilidade de uso | Média | Alta |
| Conversão automática para MD | ❌ | ✅ |
| Integração com LLMs | ❌ (requer implementação manual) | ✅ (via LangChain) |
| Processamento de PDF | ❌ (requer bibliotecas adicionais) | ✅ |
| Extração de tabelas | Limitada | Avançada |
| Manutenção de estrutura do documento | Parcial | Completa |
| Velocidade de processamento | Rápida | Moderada (depende do LLM) |
| Comunidade e documentação | Extensa | Em crescimento |

# 📦 Bibliotecas Utilizadas

* Docling
* LangChain
* LangChain OpenAI
* BeautifulSoup
* Requests
* python-dotenv


# 📦 Bibliotecas Utilizadas

* Docling
* LangChain
* LangChain OpenAI
* BeautifulSoup
* Requests
* python-dotenv
* TokenCount
* Pandas
