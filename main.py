"""Basic LLM Chain tutorial implementation using LangChain.

This script follows the tutorial-style flow:
1) Prompt template
2) Chat model
3) Output parser
4) LCEL chain composition
5) Invoke with example input
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def build_translation_chain() -> ChatPromptTemplate:
    """Build a basic translation chain with LCEL."""
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a professional translator. Translate to {target_language}. "
                "Return only the translated text.",
            ),
            ("human", "{text}"),
        ]
    )
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    parser = StrOutputParser()
    return prompt | model | parser


def main() -> None:
    """Run a basic chain example."""
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is not set. Configure it in .env")

    chain = build_translation_chain()
    result = chain.invoke(
        {
            "text": "La inteligencia artificial está transformando la educación.",
            "target_language": "English",
        }
    )
    print("=== Translation Result ===")
    print(result)


if __name__ == "__main__":
    main()