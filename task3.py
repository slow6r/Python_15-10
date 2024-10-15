while True:
    print(text_info)
    command = input("Введите номер команды ")
    if command not in ('1','2','3'):
        print('Введите номер существующего действия')
        continue
    if command == '3':
        save_phonebook(phone_book)
        break

print("Спасибо, что воспользовались нашим приложением!")
