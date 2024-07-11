from src.data_archive import DataArchive
from src.data_extract import DataExtract
from src.data_load import DataLoad
from src.data_transform import DataTransform
from src.http_requester import CardsApi, ListsApi, MembersApi


def main():
    cards_api = CardsApi()
    response_cards_api = cards_api.http_response()
    data_cards = DataExtract(response_cards_api)
    cards_list = data_cards.data_cards_extract()
    df_cards = DataTransform(cards_list).data_cards_transform()

    lists_api = ListsApi()
    response_lists_api = lists_api.http_response()
    data_list = DataExtract(response_lists_api)
    lists_list = data_list.data_lists_extract()
    df_lists = DataTransform(lists_list).data_lists_transform()

    members_api = MembersApi()
    response_members_api = members_api.http_response()
    data_members = DataExtract(response_members_api)
    members_list = data_members.data_members_extract()
    df_members = DataTransform(members_list).data_members_transform()

    transformer = DataTransform([])
    df = transformer.join_dataframes(df_cards, df_lists, df_members)
    
    excel = DataLoad(df)
    excel.upload_data_excel()
    
    completeds = DataArchive(cards_list)
    completeds.archive_cards()

    '''
        Implementar classe e seu respectivo metodo que executa a exclusao de cartoes ja arquivados
    '''

    
if __name__ == "__main__":
    main()
    

