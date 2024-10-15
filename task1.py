'''
ТЗ - создать телефонный справочник с внешним хранилищем информации.
Надо хранить имя контакта, его номера телефонов, и возможно день рождения
'''
import json



def save_phonebook(our_contacts: dict):
    '''
    Функция сохранения телефонного справочника в формат JSON
    '''
    with open("phone_book.json", "w",encoding='utf-8') as outfile:
        json.dump(our_contacts, outfile)
    print('Ваша телефонная книга успешно сохранена!')
