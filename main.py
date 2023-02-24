phoneBook = {}
exitRequested = False


def AddContact():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    phoneBook[name] = phone
    print(f"Контакт {name} успешно добавлен в справочник.")


def EditContact():
    name = input("Введите имя контакта, который хотите отредактировать: ")
    if name in phoneBook:
        phone = input("Введите новый номер телефона: ")
        phoneBook[name] = phone
        print(f"Контакт {name} успешно изменен.")
    else:
        print(f"Контакт {name} не найден в справочнике.")


def DeleteContact():
    name = input("Введите имя контакта, который хотите удалить: ")
    if name in phoneBook:
        del phoneBook[name]
        print(f"Контакт {name} успешно удален.")
    else:
        print(f"Контакт {name} не найден в справочнике.")


def PrintContacts():
    if phoneBook:
        print("Список контактов:")
        for name, phone in phoneBook.items():
            print(f"{name}: {phone}")
    else:
        print("Справочник пуст.")


def LoadPhonebook():
    f = open('phonebook.txt')
    for line in f:
        entries = line.split(';')
        phoneBook[entries[0]] = entries[1]
    f.close()

def SavePhonebook():
    f = open('phonebook.txt', 'w')
    for name, phone in phoneBook.items():
        f.write(f"{name};{phone};\n")
    print("Saved as phonebook.txt")
    f.close()


def RequestExit():
    print("Exit")


def main():
    actions = [["1. Добавить контакт", AddContact],
               ["2. Редактировать контакт", EditContact],
               ["3. Удалить контакт", DeleteContact],
               ["4. Показать все контакты", PrintContacts],
               ["5. Сохранить", SavePhonebook],
               ["6. Выйти", RequestExit]]
    LoadPhonebook()

    choice = 0
    while choice != 6:
        print("Меню:")
        for action in actions:
            print(action[0])
        choice = int(input("Введите номер действия: "))

        actions[choice - 1][1]()


if __name__ == '__main__':
    main()
