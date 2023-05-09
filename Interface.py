
from tariff_plans_print import print_tariff_plans
def main_menu():
    global tariff_plans
    print("Добро пожаловать в программу!\n")
    print("Выберите действие:")
    print("1. Подобрать тариф который будет вам подходить")
    print("2. Посмотреть список возможных тарифов")
    print("3. Выход")

    choice = input("Введите номер выбранного варианта:")
    if choice == "1":
        trpo.main_func()
    else choice == "2":
        print_tariff_plans()
    elif choice == "3":
        print("До свидания!")
    else:
        print("Некорректный выбор. Попробуйте снова.\n")

minutes = None
def get_minutes():
    # Предоставление вариантов выбора для количества минут
    global minutes
    print("Выберите количество минут разговора:")
    print("1. 250 минут")
    print("2. 300 минут")
    print("3. 600 минут")
    print("4. 1200 минут")
    print("5. 3000 минут")
    print("6. 5000 минут")
    minutes_choice = input("Введите номер выбранного варианта:")
    while minutes_choice not in ["1", "2", "3", "4", "5", "6"]:
        minutes_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

    # Получение количества минут в соответствии с выбором пользователя
    if minutes_choice == "1":
        minutes = 250
    elif minutes_choice == "2":
        minutes = 300
    elif minutes_choice == "3":
        minutes = 600
    elif minutes_choice == "4":
        minutes = 1200
    elif minutes_choice == "5":
        minutes = 3000
    elif minutes_choice == "6":
        minutes = 5000

    return minutes


messages = None
def choose_messages():
    global messages
    # Предоставление вариантов выбора для количества сообщений
    print("Выберите количество сообщений:")
    print("1. 200 сообщений")
    print("2. 300 сообщений")
    print("3. 400 сообщений")
    print("4. 500 сообщений")
    print("5. 600 сообщений")
    print("6. 700 сообщений")
    print("7. 800 сообщений")
    print("8. 1000 сообщений")
    print("9. 3000 сообщений")
    messages_choice = input("Введите номер выбранного варианта:")
    while messages_choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        messages_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

    # Получение количества сообщений в соответствии с выбором пользователя
    if messages_choice == "1":
        messages = 200
    elif messages_choice == "2":
        messages = 300
    elif messages_choice == "3":
        messages = 400
    elif messages_choice == "4":
        messages = 500
    elif messages_choice == "5":
        messages = 600
    elif messages_choice == "6":
        messages = 700
    elif messages_choice == "7":
        messages = 800
    elif messages_choice == "8":
        messages = 1000
    elif messages_choice == "9":
        messages = 3000

    return messages



data_usage = None
def choose_data_usage():
    # Предоставление вариантов выбора для объема интернет-трафика
    global data_usage
    print("Выберите объем интернет-трафика в ГБ:")
    print("1. 10 ГБ")
    print("2. 20 ГБ")
    print("3. 35 ГБ")
    print("4. 45 ГБ")
    print("5. 50 ГБ")
    print("6. 60 ГБ")

    # Запрос выбора пользователя и проверка его корректности
    data_usage_choice = input("Введите номер выбранного варианта:")
    while data_usage_choice not in ["1", "2", "3", "4", "5", "6"]:
        data_usage_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

    # Получение объема интернет-трафика в соответствии с выбором пользователя
    if data_usage_choice == "1":
        data_usage = 10
    elif data_usage_choice == "2":
        data_usage = 20
    elif data_usage_choice == "3":
        data_usage = 35
    elif data_usage_choice == "4":
        data_usage = 45
    elif data_usage_choice == "5":
        data_usage = 50
    elif data_usage_choice == "6":
        data_usage = 60

    return data_usage
