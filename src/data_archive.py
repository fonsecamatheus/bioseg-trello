from typing import Any, Dict, List

import requests

from src.envs import API_KEY, API_TOKEN, LIST_ID


class DataArchive:
    def __init__(self, card_ids: List[Dict[str, Any]]) -> None:
        self.cards = card_ids
 
    def archive_cards(self) -> None:
        for card in self.cards:
            if card['id_lista'] == f'{LIST_ID}':
                url = f"https://api.trello.com/1/cards/{card['id']}/closed"
                params = {
                    'key': API_KEY, 
                    'token': API_TOKEN, 
                    'value': 'true' #'true' para arquivar o cartão
                }   
                try:
                    response = requests.put(url, params=params)
                    response.raise_for_status()
                    print(f"Cartão {card['url']} arquivado com sucesso")
                except requests.exceptions.RequestException as e:
                    print(f"Erro ao arquivar o cartão {card['url']}: {e}")
                except Exception as e:
                    print(f"Erro ao arquivar o cartão {card['url']}: {e}")
            else:
                pass