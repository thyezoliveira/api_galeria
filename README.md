# API Galeria

API FastAPI para integração com Google Drive, exibindo galerias de imagens categorizadas.

## Pré-requisitos

* [uv](https://github.com/astral-sh/uv) instalado para gerenciamento de ambiente e pacotes Python.
* Conta de serviço do Google Cloud (com permissão de acesso à pasta do Drive).

## Configuração

1.  Clone o repositório.
2.  Copie o arquivo `.env.example` para `.env`:
    ```bash
    cp .env.example .env
    ```
3.  Preencha as variáveis de ambiente no arquivo `.env`:
    *   `GOOGLE_DRIVE_FOLDER_ID`: ID da pasta raiz no Google Drive.
    *   `GOOGLE_APPLICATION_CREDENTIALS`: Caminho para o seu arquivo `service-account.json`.

## Como Rodar Localmente

Utilize o `uv` para instalar as dependências e rodar a aplicação:

```bash
uv sync
uv run main.py
```

## Deploy no Render

Para rodar no Render, configure o `Start Command` como:
```bash
python main.py
```
Certifique-se de configurar as variáveis de ambiente (`GOOGLE_DRIVE_FOLDER_ID` e o conteúdo da `GOOGLE_APPLICATION_CREDENTIALS` como uma variável de ambiente do tipo texto ou arquivo, dependendo da configuração do Render).
Certifique-se também de que o ambiente do Render esteja configurado para instalar dependências usando o `uv` se necessário, ou apenas garantir que o Python esteja instalado e que as dependências sejam instaladas via `pip` ou `uv` durante o build.
