from docling.document_converter import DocumentConverter

url = "https://arxiv.org/pdf/2504.03277"

converter = DocumentConverter()
result = converter.convert(url)
markdown_text = result.document.export_to_markdown()
print(markdown_text)
