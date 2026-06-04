import csv
import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/tecnologia' # Definindo a URL do site

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
} # Cabeçalho para simular acesso de um usuário comum

print('Iniciando extração de dados... Aguarde.')

try: 
    response = requests.get(url, headers=headers) # Fazendo requisição para o site

    if response.status_code == 200: # Verificando se a conexão foi bem sucedida 
        soup = BeautifulSoup(response.text, 'html.parser') # Passando o HTML para o Soup
        noticias = soup.find_all('a', class_='feed-post-link') # Manchetes principais usam "feed-post-link" no G1, em tags <a>
        lista_noticias = []

        for noticia in noticias: # Vai percorrer os elementos da lista e passar a limpo
            titulo = noticia.get_text(strip=True)
            link = noticia.get('href')

            lista_noticias.append([titulo, link])
            print(f'Sucesso: {titulo[:50]}...')

        with open("noticias_g1.csv", "w", newline="", encoding="utf-8") as arquivo: # Armazenando os dados que foram extraídos num ficheiro CSV
            escritor = csv.writer(arquivo)
            escritor.writerow(["Titulo da Noticia", "Link da Materia"]) # Escrever cabeçalho
            escritor.writerows(lista_noticias)  # Escrever as listas
            print(f"\nTudo certo! {len(lista_noticias)} notícias foram guardadas com êxito em 'noticias_g1.csv'.")
    else:
        print(f'Erro no aceso ao site, status = {response.status_code}')
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")