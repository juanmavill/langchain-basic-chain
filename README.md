# langchain-basic-chain

Implementación del laboratorio basada en el tutorial base de LangChain para construir una **cadena LLM** con componentes explícitos.

Autor: **Juan Manuel Villegas Medina**

## Objetivo

Construir una cadena simple de traducción siguiendo el flujo recomendado:

1. `ChatPromptTemplate`
2. `ChatOpenAI`
3. `StrOutputParser`
4. Composición con LCEL (`prompt | model | parser`)

## Arquitectura y componentes

```text
Input(text, target_language)
        |
        v
ChatPromptTemplate
        |
        v
ChatOpenAI (gpt-4o-mini)
        |
        v
StrOutputParser
        |
        v
Output (translated text)
```

### Componentes usados

- `langchain_core.prompts.ChatPromptTemplate`: define los mensajes del sistema y usuario.
- `langchain_openai.ChatOpenAI`: ejecuta la inferencia del modelo.
- `langchain_core.output_parsers.StrOutputParser`: convierte la salida del modelo a texto plano.
- `python-dotenv`: carga variables de entorno desde `.env`.

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Editar `.env` y asignar:

```env
OPENAI_API_KEY=tu_api_key
```

## Ejecución

```bash
python main.py
```

## Ejemplo de salida (evidencia)

```text
=== Translation Result ===
Artificial intelligence is transforming education.
```

## Estructura

```text
langchain-basic-chain/
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```