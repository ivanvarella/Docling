from token_count import TokenCount
from docling.document_converter import DocumentConverter
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Exemplo de uso
url = "https://www.mdpi.com/2076-3417/8/11/2181"

converter = DocumentConverter()
result = converter.convert(url)

markdown_text = result.document.export_to_markdown()

# Contar o número de tokens
tc = TokenCount(model_name="gpt-3.5-turbo")
num_tokens = tc.num_tokens_from_string(markdown_text)
print("-" * 50)
print(f"\nNúmero de Tokens markdown: {num_tokens}\n")
print("-" * 50)

# print(markdown_text)

# Instancia o modelo de linguagem
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0, max_tokens=100)
# Cria o Prompt
prompt = """
Resuma este site para mim:
{text}
"""

restult_llm = llm.invoke(prompt.format(text=markdown_text)).content

print(restult_llm)
