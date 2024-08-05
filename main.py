import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma pasta para ser organizada')

lista_arq = os.listdir(caminho)

locais = {
    'imagens': ['.png', '.jpg', '.jpeg'],
    'videos': ['.mp4', '.mov'],
    'planilhas': ['.xlsx'],
    'pdfs': ['.pdf'],
    'csv': ['.csv'],
    'docx': ['.docx'],
    'txt': ['.txt'],
    'exe': ['.exe'],
    'zip': ['.zip']
}

for arquivo in lista_arq:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')