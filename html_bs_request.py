from bs4 import BeautifulSoup
import requests
from token_count import TokenCount


def extract_text_from_url(url):
    # Todo o HTML da página
    response = requests.get(url)

    # Contar o número de tokens
    tc = TokenCount(model_name="gpt-3.5-turbo")
    num_tokens_response = tc.num_tokens_from_string(response.text)
    print("-" * 50)
    print(f"\nNúmero de Tokens no Response: {num_tokens_response}\n")

    # Instancia o BeautifulSoup com o conteúdo HTML já convertido em string
    # e faz o parser HTML
    soup = BeautifulSoup(response.text, "html.parser")
    tc_text = TokenCount(model_name="gpt-3.5-turbo")
    num_tokens_bs_text = tc_text.num_tokens_from_string(soup.get_text())
    print(f"Número de Tokens no BeautifulSoup: {num_tokens_bs_text}\n")
    print(f"diferença de tokens: {num_tokens_response - num_tokens_bs_text}\n")
    print("-" * 50)

    # Encontra a div com a classe específica
    div_content = soup.find("div", class_="html-article-content")

    if div_content:
        return div_content.get_text()

    else:
        return "Conteúdo não encontrado."


# Exemplo de uso
url = "https://www.mdpi.com/2076-3417/8/11/2181"
texto = extract_text_from_url(url)

print(texto)
