from rembg import remove
from PIL import Image
from tkinter import filedialog, Tk
import os

# Oculta a janela principal do Tkinter
Tk().withdraw()

# Permite selecionar qualquer imagem suportada
input_path = filedialog.askopenfilename(
    title="Selecione a imagem para remover o fundo",
    filetypes=[
        ("Imagens", "*.png *.jpg *.jpeg *.webp *.bmp *.tiff *.tif"),
        ("Todos os arquivos", "*.*")
    ]
)

if not input_path:
    print("Nenhuma imagem selecionada.")
    exit()

# Abre e processa a imagem
inp = Image.open(input_path)
output = remove(inp)

# Sugere um nome padrão e permite escolher formato de saída
default_name = os.path.splitext(os.path.basename(input_path))[0] + "_sem_fundo"

output_path = filedialog.asksaveasfilename(
    defaultextension=".png",
    initialfile=default_name,
    title="Salvar imagem sem fundo",
    filetypes=[
        ("PNG", "*.png"),
        ("JPEG", "*.jpg;*.jpeg"),
        ("WEBP", "*.webp"),
        ("TIFF", "*.tiff"),
        ("BMP", "*.bmp"),
        ("Todos os arquivos", "*.*")
    ]
)

if not output_path:
    print("Nenhum local de salvamento escolhido.")
    exit()

# Salva a imagem com fundo removido
output.save(output_path)
Image.open(output_path).show()
