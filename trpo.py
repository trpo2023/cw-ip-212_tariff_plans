import os
import json

def clear_console():
    os.system('cls')

def main_menu():
    while True:
        clear_console()
        print("======================")
        print("      ГЛАВНОЕ МЕНЮ     ")
        print("======================")
        menu_options = ["Подобрать тариф", "Просмотреть все тарифы", "Выйти из программы"]
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")
        print("======================")

        choice = input("Выберите опцию (введите номер): ")

        if choice == "1":
            clear_console()
            choice_tariff()
        elif choice == "2":
            clear_console()
            print_tariff_plans()
        elif choice == "3":
            print("Выход из программы...")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

def choice_tariff():
    def get_choice(prompt, options, user_choice):
        print(prompt)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        choice = user_choice
        while choice not in map(str, range(1, len(options) + 1)):
            choice = input("Некорректный выбор. Введите номер выбранного варианта: ")
        return options[int(choice) - 1]

def choice_tariff(*user_input, tariff_plans=None):
    with open("tariff_plans.json") as file:
        data = json.load(file)

    tariff_plans = data["tariff_plans"]

    print("Укажите ваши затраты:")
    minutes = get_choice("Выберите количество минут разговора:", ["250 минут", "300 минут", "600 минут", "1200 минут", "3000 минут", "5000 минут"], "")
    messages = get_choice("Выберите количество сообщений:", ["200 сообщений", "300 сообщений", "400 сообщений", "500 сообщений", "600 сообщений", "700 сообщений", "800 сообщений", "1000 сообщений", "3000 сообщений"], "")
    internet = get_choice("Выберите количество интернет-трафика:", ["10 ГБ", "20 ГБ", "35 ГБ", "45 ГБ", "50 ГБ", "60 ГБ"], "")

    clear_console()

    operator = get_choice("Выберите желаемого оператора:", ["MTS", "Beeline", "TELE2", "Megafon"], "")

    optimal_tariff = None
    optimal_tariff_monthly_cost = float('inf')

    while optimal_tariff is None:
        for tariff_name, tariff_details in tariff_plans.items():
            if tariff_details["operator"] == operator:
                tariff_minutes = tariff_details["minutes"]
                tariff_messages = tariff_details["messages"]
                tariff_internet = tariff_details["internet"]
                tariff_monthly_cost = tariff_minutes + tariff_messages + tariff_internet

                if tariff_minutes >= int(minutes.split()[0]) and tariff_messages >= int(messages.split()[0]) and tariff_internet >= int(internet.split()[0]) and tariff_monthly_cost < optimal_tariff_monthly_cost:
                    optimal_tariff = tariff_name
                    optimal_tariff_monthly_cost = tariff_monthly_cost

        if optimal_tariff is None:
            choice = input("Извините, для ваших затрат не найдено подходящего тарифного плана. Хотите попробовать снова? (да/нет): ")
            if choice.lower() != "да":
                break
            operator = get_choice("Выберите желаемого оператора:", ["MTS", "Beeline", "TELE2", "Megafon"], "")

    if optimal_tariff:
        minute_optimal = tariff_plans[optimal_tariff]['minutes']
        message_optimal = tariff_plans[optimal_tariff]['messages']
        internet_optimal = tariff_plans[optimal_tariff]['internet']
        tariff_monthly_cost_optimal = tariff_plans[optimal_tariff]['monthly_cost']

        print("Наиболее оптимальный для вас тарифный план:")
        print(f"Тариф: {optimal_tariff}")
        print(f"Минуты разговора: {minute_optimal}")
        print(f"Количество сообщений: {message_optimal}")
        print(f"Интернет-трафик: {internet_optimal} ГБ")
        print(f"Стоимость: {tariff_monthly_cost_optimal} рублей.")

        confirm = input("Вы хотите подключить этот тариф? (да/нет): ")
        if confirm.lower() == "да":
            # Код для подключения тарифа
            print("Тариф успешно подключен!")
        else:
            change_tariff = input("Хотите изменить выбранный тариф? (да/нет): ")
            if change_tariff.lower() == "да":
                choice_tariff()
            else:
                print("Тариф не был подключен.")

    else:
        print("Извините, для ваших затрат не найдено подходящего тарифного плана.")

    input("Нажмите Enter, чтобы вернуться в главное меню.")

def print_tariff_plans():
    with open("tariff_plans.json") as file:
        data = json.load(file)

    tariff_plans = data["tariff_plans"]

    for tariff_name, tariff_details in tariff_plans.items():
        print(f"Тариф: {tariff_name}")
        print(f"Оператор: {tariff_details['operator']}")
        print(f"Минуты разговора: {tariff_details['minutes']}")
        print(f"Количество сообщений: {tariff_details['messages']}")
        print(f"Интернет-трафик: {tariff_details['internet']}" + "ГБ")
        print(f"Стоимость: {tariff_details['monthly_cost']}" + "Рублей")
        print("======================")

    input("Нажмите Enter, чтобы вернуться в главное меню.")

if __name__ == "__main__":
    main_menu()