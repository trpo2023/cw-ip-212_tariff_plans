import os
import json

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tariff_plans():
    try:
        with open("tariff_plans.json") as file:
            data = json.load(file)
            return data["tariff_plans"]
    except FileNotFoundError:
        print("Файл 'tariff_plans.json' не найден.")
        return {}
    except json.JSONDecodeError:
        print("Ошибка при чтении файла 'tariff_plans.json'. Проверьте структуру файла.")
        return {}

def print_tariff_details(tariff_name, tariff_details):
    print("======================")
    print(f"Тариф: {tariff_name}")
    print(f"Минуты: {tariff_details['minutes']}")
    print(f"Сообщения: {tariff_details['messages']}")
    print(f"Интернет: {tariff_details['internet']} ГБ")
    print(f"Оператор: {tariff_details['operator']}")

def print_tariff_plans(tariff_plans):
    print("Доступные тарифы:")
    for tariff_name, tariff_details in tariff_plans.items():
        print_tariff_details(tariff_name, tariff_details)

def get_user_choice(options):
    choice = input("Выберите опцию (введите номер): ")
    while choice not in options:
        print("Некорректный выбор. Попробуйте еще раз.")
        choice = input("Выберите опцию (введите номер): ")
    return choice

def choose_from_options(message, options):
    print(message)
    for index, option in enumerate(options, 1):
        print(f"{index}. {option}")
    choice = get_user_choice([str(index) for index in range(1, len(options) + 1)])
    return options[int(choice) - 1]

def choice_tariff(tariff_plans):
    def get_minutes():
        minutes_options = ["250 минут", "300 минут", "600 минут", "1200 минут", "3000 минут", "5000 минут"]
        return int(choose_from_options("Выберите количество минут разговора:", minutes_options).split()[0])

    def choose_messages():
        messages_options = ["200 сообщений", "300 сообщений", "400 сообщений", "500 сообщений", "600 сообщений", "700 сообщений", "800 сообщений", "1000 сообщений", "3000 сообщений"]
        return int(choose_from_options("Выберите количество сообщений:", messages_options).split()[0])

    def choose_internet():
        internet_options = ["10 ГБ", "20 ГБ", "35 ГБ", "45 ГБ", "50 ГБ", "60 ГБ"]
        return int(choose_from_options("Выберите количество интернет-трафика:", internet_options).split()[0])

    def choose_operator():
        operators = ["MTS", "Beeline", "TELE2", "Megafon"]
        return choose_from_options("Выберите желаемого оператора:", operators)

    print("Укажите ваши затраты:")
    minutes = get_minutes()
    messages = choose_messages()
    internet = choose_internet()
    operator = choose_operator()

    optimal_tariff = None
    optimal_tariff_cost = float('inf')

    for tariff_name, tariff_details in tariff_plans.items():
        if tariff_details["operator"] == operator:
            tariff_minutes = tariff_details["minutes"]
            tariff_messages = tariff_details["messages"]
            tariff_internet = tariff_details["internet"]
            tariff_cost = tariff_minutes + tariff_messages + tariff_internet

            if tariff_minutes >= minutes and tariff_messages >= messages and tariff_internet >= internet and tariff_cost < optimal_tariff_cost:
                optimal_tariff = tariff_name
                optimal_tariff_cost = tariff_cost

    if optimal_tariff is not None:
        optimal_tariff_operator = tariff_plans[optimal_tariff]["operator"]

        print_tariff_details(optimal_tariff, tariff_plans[optimal_tariff])
        confirmation = input("Вы хотите подключить данный тариф? (Да/Нет): ")
        if confirmation.lower() == "да":
            clear_console()
            print(f"Тариф успешно подключен! Ежемесячная плата составит: {tariff_plans[optimal_tariff]['monthly_cost']} рублей.")
            print("Выход в главное меню...")
        else:
            change_tariff = input("Хотите выбрать другой тариф? (Да/Нет): ")
            if change_tariff.lower() == "да":
                clear_console()
                choice_tariff(tariff_plans)
            else:
                clear_console()
                print("Подключение тарифа отменено.")
                print("Спасибо за использование нашего приложения!!!")
    else:
        print("К сожалению, не удалось найти подходящий тариф.")

def main_menu(tariff_plans):
    while True:
        print("======================")
        print("      ГЛАВНОЕ МЕНЮ     ")
        print("======================")
        print("1. Подобрать тариф")
        print("2. Просмотреть все тарифы")
        print("3. Выйти из программы")
        print("======================")

        choice = get_user_choice(["1", "2", "3"])

        if choice == "1":
            choice_tariff(tariff_plans)
        elif choice == "2":
            print_tariff_plans(tariff_plans)
        elif choice == "3":
            print("Выход из программы...")
            break

# Запуск программы
clear_console()
tariff_plans = load_tariff_plans()
main_menu(tariff_plans)
