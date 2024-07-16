import pandas as pd

from src.envs import LIST_ID, DEST, DEST_EXCL


class DataLoad:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.df = dataframe
        self.dest = rf'{DEST}'
        self.completed_dest = rf'{DEST_EXCL}'

    def upload_data_excel(self) -> None:
        #DATAFRAME CARTÕES CONCLUÍDOS 
        df_completed = self.df[self.df['id_lista'] == f'{LIST_ID}']
   
        #DATAFRAME HISTÓRICO (dataframe que contem os dados de cartoes que foram concluidos, arquivados e excluidos)
        historical_excel = pd.read_excel(self.completed_dest)
        df_historical = pd.DataFrame(historical_excel)

        '''
        Logica que permite a concatenação dos dataframes historico com os concluidos.
        Caso o numero de linhas do dataframe historico seja maior do que a soma do numero de linhas do dataframe historico
        com o dataframe de concluidos, a operaçao é cancelada para evitar perda de dados ou inconsistencias.
        Caso contrario, os dataframes sao concatenados e o resultado é salvo no destino especificado.
        '''
        total_lines = df_completed.shape[0] + df_historical.shape[0]
        if df_historical.shape[0] > total_lines:
            #Logica para rollback
            print("A operação foi cancelada devido a um problema na quantidade de linhas!")
        else:
            #Logica para concatenaçao
            df_concatenated = pd.concat([df_historical, df_completed], ignore_index=True)
            df_concatenated.to_excel(self.completed_dest, index=False)
            print("Os dados foram concatenados e salvos com sucesso!")

        #Concatenando o df de valores historicos/cartoes concluidos com o df de cartoes abertos
        df_n_completed = self.df.loc[self.df['id_lista'] != f'{LIST_ID}']
        df_concatenated1 = pd.concat([df_n_completed, df_concatenated])
        df_concatenated1.to_excel(self.dest, index=False)

