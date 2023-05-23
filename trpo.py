import os
import json

def clear_console():
    os.system('cls')

def main_menu():
    while True:
        print("======================")
        print("      ГЛАВНОЕ МЕНЮ     ")
        print("======================")
        print("1. Подобрать тариф")
        print("2. Просмотреть все тарифы")
        print("3. Выйти из программы")
        print("======================")

        choice = input("Выберите опцию (введите номер): ")

        if choice == "1":
            choice_tariff()
        elif choice == "2":
            print_tariff_plans()
        elif choice == "3":
            print("Выход из программы...")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

def choice_tariff():
    def get_minutes():
        print("Выберите количество минут разговора:")
        print("1. 250 минут")
        print("2. 300 минут")
        print("3. 600 минут")
        print("4. 1200 минут")
        print("5. 3000 минут")
        print("6. 5000 минут")
        minutes_choice = input("Введите номер выбранного варианта: ")
        while minutes_choice not in ["1", "2", "3", "4", "5", "6"]:
            minutes_choice = input("Некорректный выбор. Введите номер выбранного варианта: ")

        if minutes_choice == "1":
            return 250
        elif minutes_choice == "2":
            return 300
        elif minutes_choice == "3":
            return 600
        elif minutes_choice == "4":
            return 1200
        elif minutes_choice == "5":
            return 3000
        elif minutes_choice == "6":
            return 5000

    def choose_messages():
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
        messages_choice = input("Введите номер выбранного варианта: ")
        while messages_choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            messages_choice = input("Некорректный выбор. Введите номер выбранного варианта: ")

        if messages_choice == "1":
            return 200
        elif messages_choice == "2":
            return 300
        elif messages_choice == "3":
            return 400
        elif messages_choice == "4":
            return 500
        elif messages_choice == "5":
            return 600
        elif messages_choice == "6":
            return 700
        elif messages_choice == "7":
            return 800
        elif messages_choice == "8":
            return 1000
        elif messages_choice == "9":
            return 3000

    def choose_internet():
        print("Выберите количество интернет-трафика:")
        print("1. 1 ГБ")
        print("2. 3 ГБ")
        print("3. 5 ГБ")
        print("4. 10 ГБ")
        print("5. 15 ГБ")
        print("6. 20 ГБ")
        print("7. 30 ГБ")
        print("8. 40 ГБ")
        print("9. 50 ГБ")
        internet_choice = input("Введите номер выбранного варианта: ")
        while internet_choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            internet_choice = input("Некорректный выбор. Введите номер выбранного варианта: ")

        if internet_choice == "1":
            return 1
        elif internet_choice == "2":
            return 3
        elif internet_choice == "3":
            return 5
        elif internet_choice == "4":
            return 10
        elif internet_choice == "5":
            return 15
        elif internet_choice == "6":
            return 20
        elif internet_choice == "7":
            return 30
        elif internet_choice == "8":
            return 40
        elif internet_choice == "9":
            return 50

    with open("tariff_plans.json") as file:
        data = json.load(file)
        
    tariff_plans = data["tariff_plans"]

    print("Укажите ваши затраты:")
    minutes = get_minutes()
    messages = choose_messages()
    internet = choose_internet()

    optimal_tariff = None
    optimal_tariff_cost = float('inf')

    for tariff_name, tariff_details in tariff_plans.items():
        tariff_minutes = tariff_details["minutes"]
        tariff_messages = tariff_details["messages"]
        tariff_internet = tariff_details["internet"]
        tariff_cost = tariff_minutes + tariff_messages + tariff_internet

        if tariff_minutes >= minutes and tariff_messages >= messages and tariff_internet >= internet and tariff_cost < optimal_tariff_cost:
            optimal_tariff = tariff_name
            optimal_tariff_cost = tariff_cost

    if optimal_tariff is not None:
        optimal_tariff_operator = tariff_plans[optimal_tariff]["operator"]

        print("======================")
        print("Рекомендуемый тариф:")
        print(f"Тариф: {optimal_tariff}")
        print(f"Оператор: {optimal_tariff_operator}")
        print(f"Минуты: {minutes}")
        print(f"Сообщения: {messages}")
        print(f"Интернет: {internet} ГБ")
        print("======================")

        confirmation = input("Вы хотите подключить данный тариф? (Да/Нет): ")
        if confirmation.lower() == "да":
            print("Тариф успешно подключен!")
        else:
            change_tariff = input("Хотите выбрать другой тариф? (Да/Нет): ")
            if change_tariff.lower() == "да":
                choice_tariff()
            else:
                print("Подключение тарифа отменено.")
                print("Спасибо за использование нашего приложения!!!")
    else:
        print("К сожалению, не удалось найти подходящий тариф.")

def print_tariff_plans():
    with open("tariff_plans.json") as file:
        data = json.load(file)

    tariff_plans = data["tariff_plans"]

    print("Доступные тарифы:")
    for tariff_name, tariff_details in tariff_plans.items():
        print("======================")
        print(f"Тариф: {tariff_name}")
        print(f"Минуты: {tariff_details['minutes']}")
        print(f"Сообщения: {tariff_details['messages']}")
        print(f"Интернет: {tariff_details['internet']} ГБ")
        print(f"Оператор: {tariff_details['operator']}")

# Запуск программы
clear_console()
main_menu()