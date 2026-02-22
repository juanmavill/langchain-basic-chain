# langchain-basic-chain

Proyecto de cadena básica de traducción usando LangChain.

## Arquitectura

```text
Input -> ChatPromptTemplate -> ChatOpenAI(gpt-4o-mini) -> StrOutputParser -> Output
```

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

## Ejecución

```bash
python main.py
```

## Autor

Juan Manuel Villegas Medina
