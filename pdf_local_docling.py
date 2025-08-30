from docling.document_converter import DocumentConverter
import os
import unicodedata
import pandas as pd


# Normalizar nomes para evitar problemas com caracteres
def normalize_filename(filename):
    return unicodedata.normalize("NFC", filename)


# Caminho base
base_path = os.path.join(os.getcwd(), "pdfs")
target_name = "L13709compilado.pdf"
normalized_target = normalize_filename(target_name)

# Procurar o arquivo na pasta
for filename in os.listdir(base_path):
    normalized_filename = normalize_filename(filename)
    if normalized_filename == normalized_target:
        pdf_path = os.path.join(base_path, filename)
        print(f"Arquivo encontrado: {pdf_path}\n\n")
        break
else:
    raise FileNotFoundError(f"Arquivo '{target_name}' não encontrado em {base_path}")


# Convertendo para Markdown e texto puro
converter = DocumentConverter()
result = converter.convert(pdf_path)
markdown_text = result.document.export_to_markdown()
text = result.document.export_to_text()

# Salvando o arquivo Markdown
markdown_filename = target_name + "_MD.md"
text_filename = target_name + "_TEXT.txt"
markdown_path = os.path.join(base_path, markdown_filename)
text_path = os.path.join(base_path, text_filename)
try:
    with open(markdown_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)
    print(f"Arquivo Markdown salvo em: {markdown_path}\n")
except Exception as e:
    print(f"Erro ao salvar o arquivo Markdown: {e}\n")

try:
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Arquivo de texto salvo em: {text_path}\n")
except Exception as e:
    print(f"Erro ao salvar o arquivo de texto: {e}\n")


tables = result.document.tables
if tables:
    print("-" * 50)
    print(f"Número de tabelas encontradas: {len(tables)}\n")
    print("-" * 50)
    for idx, table in enumerate(tables):
        df = table.export_to_dataframe()
        print(f"Tabela {idx + 1}:\n")
        print(df)
        print("-" * 50)
        break  # Mostrar somente a primeira tabela
else:
    print("Nenhuma tabela encontrada.\n")
