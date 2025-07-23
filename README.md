# BechdelTestAI

Um MVP para analisar roteiros e transcrições com base no **Teste de Bechdel** e métricas de representatividade de gênero.

---

## **O que este projeto faz (MVP inicial)**
- Estrutura organizada para evoluir a lógica de:
  - Teste de Bechdel: verificar se há duas personagens femininas que conversam entre si sobre algo que não seja um homem.
  - Distribuição de gênero:
    - Por número de personagens.
    - Por quantidade de falas.
- Interface com **Streamlit** para fácil interação.

> **Nota:** Este primeiro commit contém apenas a estrutura inicial e funções retornando valores nulos (`TODO: implementar`).

---

## **Requisitos**
- [Python 3.10+](https://www.python.org/downloads/)
- Ambiente virtual (recomendado)
- Dependências:
  ```bash
  pip install -r requirements.txt

## Como rodar o projeto?
### 1. Ativar ambiente virtual (se estiver usando)
### Windows:
```bash 
  .venv\Scripts\activate
```
### Linux/Mac:
```bash 
  source .venv/bin/activate
```
### 2. Rodar a aplicação com Streamlit
```bash 
  streamlit run app.py
```
### 3. Abrir no navegador
 Geralmente: http://localhost:8501

# Configuração da API do Gemini

Para usar os recursos de Inteligência Artificial (IA) baseados no **Google Gemini**, é necessário configurar uma **chave de API** no arquivo `.env` do projeto.

## Passo 1: Obter a API Key do Gemini
1. Acesse o site oficial do [Google AI Studio](https://makersuite.google.com/app/apikey).
2. Gere uma nova **chave de API** (caso ainda não possua uma).
3. Copie o valor da chave gerada.

## Passo 2: Criar o arquivo `.env`
Na raiz do seu projeto, crie um arquivo chamado `.env` (se ainda não existir) e adicione a seguinte linha:

```bash
  GEMINI_API_KEY="SUA_CHAVE_DE_API_AQUI"
