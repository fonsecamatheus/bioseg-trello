import pandas as pd

from src.envs import LIST_ID


class DataLoad:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.df = dataframe
        self.dest = r'C:\Users\matheus.rabelo\BioSeg Segurança do Trabalho\Indicadores de Gestão - DataWarehouse - DATA WAREHOUSE\TRELLO\INDICADORES DE GESTÃO.xlsx'
        self.completed_dest = r'C:\Users\matheus.rabelo\BioSeg Segurança do Trabalho\Indicadores de Gestão - DataWarehouse - DATA WAREHOUSE\TRELLO\INDICADORES DE GESTÃO CONCLUÍDOS.xlsx'

    def upload_data_excel(self) -> None:
        #DATAFRAME CARTÕES CONCLUÍDOS 
        df_completed = self.df[self.df['id_lista'] == f'{LIST_ID}']
   
        historical_excel = pd.read_excel(self.completed_dest)
        df_historical = pd.DataFrame(historical_excel)

        '''
        Aplicar logica sobre a quantidade de linhas.
        Se for menor que self.completed_dest, ele aplica o rollback, caso contrario autoriza a concatenacao dos dataframes.
        '''
        total_lines = df_completed.shape[0] + df_historical.shape[0]
        if df_historical.shape[0] > total_lines:
            # Lógica para rollback
            print("Rollback: A operação foi cancelada devido a um problema na quantidade de linhas.")
        else:
            # Lógica para concatenação
            df_concatenated = pd.concat([df_historical, df_completed], ignore_index=True)
            df_concatenated.to_excel(self.completed_dest, index=False)
            print("Concatenação: Os dados foram concatenados e salvos com sucesso.")

        #DATAFRAME CARTÕES EM ABERTO
        df_n_completed = self.df.loc[self.df['id_lista'] != f'{LIST_ID}']
        df1_concatened = pd.concat([df_n_completed, df_concatenated])
        df1_concatened.to_excel(self.dest, index=False)

