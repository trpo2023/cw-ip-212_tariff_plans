from tariff_plans import tariff_plans
def print_tariff_plans():
    for plan_name, tariff_params in tariff_plans.items():
        print(f"Тариф {plan_name}:")
        print(f"\t- количество минут: {tariff_params['minute_limit']}")
        print(f"\t- количество сообщений: {tariff_params['message_limit']}")
        print(f"\t- количество интернет трафика: {tariff_params['data_limit']} Гб")
        print(f"\t- оператор: {tariff_params['operator']}")
        print(f"\t- стоимость: {tariff_params['nonthly_cost']} руб.")
