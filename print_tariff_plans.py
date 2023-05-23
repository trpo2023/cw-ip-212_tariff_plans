
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
