from typing import Any, Dict, List

import pandas as pd


class DataTransform:
    def __init__(self, endpoint_list: List[Dict[str, Any]]) -> None:
        self.dataframe = pd.DataFrame(endpoint_list)

    def data_cards_transform(self) -> pd.DataFrame:
        df_cards = self.dataframe.copy()
        df_cards['data_inicio'] = pd.to_datetime(df_cards['data_inicio'], format='%Y-%m-%dT%H:%M:%S.%fZ')
        df_cards['data_inicio'] = df_cards['data_inicio'].dt.strftime('%d/%m/%Y')
        df_cards['data_termino'] = pd.to_datetime(df_cards['data_termino'], format='%Y-%m-%dT%H:%M:%S.%fZ')
        df_cards['data_termino'] = df_cards['data_termino'].dt.strftime('%d/%m/%Y')
        df_cards = df_cards.explode('id_membro')
        return df_cards

    def data_lists_transform(self) -> pd.DataFrame:
        df_lists = self.dataframe.copy()
        return df_lists

    def data_members_transform(self) -> pd.DataFrame:
        df_members = self.dataframe.copy()
        return df_members

    def join_dataframes(self, df_cards: pd.DataFrame, df_lists: pd.DataFrame, df_members: pd.DataFrame) -> pd.DataFrame:
        joined_df = pd.merge(df_cards, df_lists, on='id_lista', how='left')
        joined_df = pd.merge(joined_df, df_members, on='id_membro', how='left')
        joined_df = joined_df.drop(columns=['id_membro'])  
        return joined_df
    



        