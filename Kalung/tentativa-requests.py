import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL da página que você quer acessar
base_url = "https://www.kalunga.com.br/marca/plascony/47882618/0001"

# Prefixo para as URLs de download
download_url_prefix = "https://img.kalunga.com.br/fotosdeprodutos/"

# Pasta de destino para salvar as imagens
destination_folder = r"C:\Users\internet07\Downloads\python"

# Criar a pasta de destino se ela não existir
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Fazer a solicitação HTTP
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar todas as tags de imagem com URLs que contêm o prefixo de download
image_tags = soup.find_all("img", src=lambda src: src and src.startswith(download_url_prefix))

# Fazer o download e salvar as imagens
for img_tag in image_tags:
    image_url = img_tag["src"]
    full_image_url = urljoin(base_url, image_url)
    image_name = os.path.basename(image_url)
    image_path = os.path.join(destination_folder, image_name)

    response = requests.get(full_image_url)
    with open(image_path, "wb") as image_file:
        image_file.write(response.content)
        print(f"Imagem '{image_name}' baixada e salva em '{image_path}'")
