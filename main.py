"""Cadena básica de traducción con LangChain."""

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def build_chain():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Translate the user text to {language}. Return only the translation."),
            ("human", "{text}"),
        ]
    )
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    parser = StrOutputParser()
    return prompt | model | parser


def main() -> None:
    chain = build_chain()
    result = chain.invoke({
        "text": "La inteligencia artificial mejora la productividad.",
        "language": "English",
    })
    print(result)


if __name__ == "__main__":
    main()
