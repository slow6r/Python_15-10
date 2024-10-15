def load_phonebook():
    '''
    Функция загрузки телефонного справочника из формата JSON
    '''   
    with open('phone_book.json', 'r',encoding='utf-8') as openfile:
        json_object = json.load(openfile)
    return json_object
