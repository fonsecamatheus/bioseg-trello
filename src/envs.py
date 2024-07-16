import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://api.trello.com/1/boards/' 
API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')

asking = '''1. INDICADORES DE GESTÃO\n2. GESTÃO TÉCNICA\nSelecione o n° do quadro que você quer extrair e arquivar os dados: '''
choice = int(input(asking))

while choice not in (1, 2):
    print("Escolha inválida. Tente novamente.")
    choice = int(input(asking))
if choice == 1:
    BOARD_ID = os.getenv('BOARD_INDICADORES')
    LIST_ID = os.getenv('LIST_INDICADORES')
    DEST = os.getenv('DEST_INDICADORES')
    DEST_EXCL = os.getenv('DEST_EXCL_INDICADORES')
elif choice == 2:
    BOARD_ID = os.getenv('BOARD_GESTAO')
    LIST_ID = os.getenv('LIST_GESTAO')
    DEST = os.getenv('DEST_GESTAO')
    DEST_EXCL = os.getenv('DEST_EXCL_GESTAO')
