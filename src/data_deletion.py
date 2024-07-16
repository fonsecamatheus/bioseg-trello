from typing import Any, Dict, List

import requests

from src.envs import API_KEY, API_TOKEN, LIST_ID


class DataDeletion:
    def __init__(self, card_ids: List[Dict[str, Any]]) -> None:
        self.cards = card_ids

    def deletion_cards(self) -> None:
        for card in self.cards:
            if card['id_lista'] == f'{LIST_ID}':
                url = f"https://api.trello.com/1/cards/{card['id']}"
                params = {
                    'key': API_KEY, 
                    'token': API_TOKEN, 
                }
                try:
                    response = requests.delete(url, params=params)
                    response.raise_for_status()
                    print(f"Cartão ({card['nome']}) foi excluído com sucesso")
                except requests.exceptions.RequestException as e:
                    print(f"Erro ao excluir o cartão ({card['nome']}): {e}")
                except Exception as e:
                    print(f"Erro ao excluir o cartão ({card['nome']}): {e}")
            else:
                pass  