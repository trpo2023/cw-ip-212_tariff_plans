tariff_plans = {
"MTS_access": {"minute_limit": 5000, "message_limit": 1000,  "data_limit": 50, "operator":str("MTS"), "nonthly_cost":790},
"We_Are_MTS": {"minute_limit": 1200, "message_limit": 500,  "data_limit": 240, "operator":str("MTS"), "nonthly_cost":850},
"The_tariff_is_higher ": {"minute_limit": 600, "message_limit": 600,  "data_limit": 30, "operator":str("MTS"), "nonthly_cost":600},
"NOT_A_TARIFF": {"minute_limit": 300, "message_limit": 200,  "data_limit": 15, "operator":str("MTS"), "nonthly_cost":500},
"ULTRA": {"minute_limit": 3500, "message_limit": 2000,  "data_limit": 60, "operator":str("MTS"), "nonthly_cost":1900},
"Smart ": {"minute_limit": 250, "message_limit": 250,  "data_limit": 50, "operator":str("MTS"), "nonthly_cost":410},
"Black": {"minute_limit": 1000, "message_limit": 100,  "data_limit": 50, "operator":str("TELE2"), "nonthly_cost":800},
"Super_Online+": {"minute_limit": 600, "message_limit": 50,  "data_limit": 40, "operator":str("TELE2"), "nonthly_cost":600},
"My_Online+": {"minute_limit": 600, "message_limit": 40,  "data_limit": 30, "operator":str("TELE2"), "nonthly_cost":550},
"My_Online": {"minute_limit": 600, "message_limit": 40,  "data_limit": 20, "operator":str("TELE2"), "nonthly_cost":450},
"My_conversation": {"minute_limit": 250, "message_limit": 30,  "data_limit": 10, "operator":str("TELE2"), "nonthly_cost":380},
"Premium": {"minute_limit": 2000, "message_limit": 500,  "data_limit": 60, "operator":str("TELE2"), "nonthly_cost":1500},
"Warm_welcome_S": {"minute_limit": 250, "message_limit": 50,  "data_limit": 10, "operator":str("megafon"), "nonthly_cost":380},
"Warm_welcome_L": {"minute_limit": 650, "message_limit": 70,  "data_limit": 35, "operator":str("megafon"), "nonthly_cost":550},
"MegaTarif": {"minute_limit": 600, "message_limit": 100,  "data_limit": 35, "operator":str("megafon"), "nonthly_cost":550},
"Maximum": {"minute_limit": 900, "message_limit": 200,  "data_limit": 45, "operator":str("megafon"), "nonthly_cost":750},
"VIP": {"minute_limit": 1500, "message_limit": 300,  "data_limit": 50, "operator":str("megafon"), "nonthly_cost":1000},
"Permium": {"minute_limit": 3000, "message_limit": 400,  "data_limit": 60, "operator":str("megafon"), "nonthly_cost":2000},
"Bee_Bazya": {"minute_limit": 600, "message_limit": 100,  "data_limit": 45, "operator":str("Beeline"), "nonthly_cost":650},
"Dragon_Jung": {"minute_limit": 500, "message_limit": 50,  "data_limit": 40, "operator":str("Beeline"), "nonthly_cost":580},
"cat_pus": {"minute_limit": 900, "message_limit": 80,  "data_limit": 45, "operator":str("Beeline"), "nonthly_cost":730},
"panda_tapa": {"minute_limit": 350, "message_limit": 70,  "data_limit": 20, "operator":str("Beeline"), "nonthly_cost":470},
"robot_ping": {"minute_limit": 500, "message_limit": 60,  "data_limit": 30, "operator":str("Beeline"), "nonthly_cost":530},
"To_the_maximum!": {"minute_limit": 3000, "message_limit": 300,  "data_limit": 60, "operator":str("Beeline"), "nonthly_cost":1800}
}

# Предоставление вариантов выбора для количества минут
print("Выберите количество минут разговора:")
print("1. 100 минут")
print("2. 200 минут")
print("3. 300 минут")
minutes_choice = input("Введите номер выбранного варианта:")
while minutes_choice not in ["1", "2", "3"]:
    minutes_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

# Получение количества минут в соответствии с выбором пользователя
if minutes_choice == "1":
    minutes = 100
elif minutes_choice == "2":
    minutes = 200
elif minutes_choice == "3":
    minutes = 300

# Предоставление вариантов выбора для количества сообщений
print("Выберите количество сообщений:")
print("1. 100 сообщений")
print("2. 200 сообщений")
print("3. 300 сообщений")
messages_choice = input("Введите номер выбранного варианта:")
while messages_choice not in ["1", "2", "3"]:
    messages_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

# Получение количества сообщений в соответствии с выбором пользователя
if messages_choice == "1":
    messages = 100
elif messages_choice == "2":
    messages = 200
elif messages_choice == "3":
    messages = 300

# Предоставление вариантов выбора для объема интернет-трафика
print("Выберите объем интернет-трафика в ГБ:")
print("1. 3 ГБ")
print("2. 5 ГБ")
print("3. 10 ГБ")
data_usage_choice = input("Введите номер выбранного варианта:")
while data_usage_choice not in ["1", "2", "3"]:
    data_usage_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

# Получение объема интернет-трафика в соответствии с выбором пользователя
if data_usage_choice == "1":
    data_usage = 3
elif data_usage_choice == "2":
    data_usage = 5
elif data_usage_choice == "3":
    data_usage = 10

# Предоставление вариантов выбора для оператора
print("Выберите оператора:")
print("1. MTS")
print("2. TELE2")
print("3. megafon")
print("4. beeline")
operator_choice = input("Введите номер выбранного варианта:")
while operator_choice not in ["1", "2", "3", "4"]:
    operator_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

# Получение оператора в соответствии с выбором пользователя
if operator_choice == "1":
    operator_user = "MTS"
elif operator_choice == "2":
    operator_user = "TELE2"
elif operator_choice == "3":
    operator_user = "megafon"
elif operator_choice == "4":
    operator_user = "beeline"

for tariff_name, tariff_params in tariff_plans.items():
    if minutes <= tariff_params["minute_limit"] and messages <= tariff_params["message_limit"] and data_usage <= tariff_params["data_limit"] and operator_user <= tariff_params["operator"] :
        recommended_tariff = tariff_name
        break

import animation

# Предоставление рекомендации наиболее выгодного тарифа
print("Рекомендуем вам тарифный план:", recommended_tariff)
print("Колличество сообщений:", tariff_params["message_limit"])
print("Колличество минут:", tariff_params["minute_limit"])
print("Колличество интернета в ГБ:", tariff_params["data_limit"])

replace =input("Если вас не устраивает тарифный план, вы можете выбрать другой (y/n)")
while replace not in ["y", "n"]:
    replace = input("Я не расспознал, что вы от меня хотите, повторите снова.\n Если вас не устраивает тарифный план, вы можете выбрать другой (y/n)")
if replace == "y":
    print("Выберите другой тариф")
    print("Выберите количество минут разговора:")
    print("1. 100 минут")
    print("2. 200 минут")
    print("3. 300 минут")
    minutes_choice = input("Введите номер выбранного варианта:")
    while minutes_choice not in ["1", "2", "3"]:
        minutes_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

    # Получение количества минут в соответствии с выбором пользователя
    if minutes_choice == "1":
        minutes = 100
    elif minutes_choice == "2":
        minutes = 200
    elif minutes_choice == "3":
        minutes = 300

    # Предоставление вариантов выбора для количества сообщений
    print("Выберите количество сообщений:")
    print("1. 100 сообщений")
    print("2. 200 сообщений")
    print("3. 300 сообщений")
    messages_choice = input("Введите номер выбранного варианта:")
    while messages_choice not in ["1", "2", "3"]:
        messages_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

    # Получение количества сообщений в соответствии с выбором пользователя
    if messages_choice == "1":
        messages = 100
    elif messages_choice == "2":
        messages = 200
    elif messages_choice == "3":
        messages = 300

    # Предоставление вариантов выбора для объема интернет-трафика
    print("Выберите объем интернет-трафика в ГБ:")
    print("1. 3 ГБ")
    print("2. 5 ГБ")
    print("3. 10 ГБ")
    data_usage_choice = input("Введите номер выбранного варианта:")
    while data_usage_choice not in ["1", "2", "3"]:
        data_usage_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

    # Получение объема интернет-трафика в соответствии с выбором пользователя
    if data_usage_choice == "1":
        data_usage = 3
    elif data_usage_choice == "2":
        data_usage = 5
    elif data_usage_choice == "3":
        data_usage = 10

    # Предоставление вариантов выбора для оператора
    print("Выберите оператора:")
    print("1. MTS")
    print("2. TELE2")
    print("3. megafon")
    print("4. beeline")
    operator_choice = input("Введите номер выбранного варианта:")
    while operator_choice not in ["1", "2", "3", "4"]:
        operator_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

    # Получение оператора в соответствии с выбором пользователя
    if operator_choice == "1":
        operator_user = "MTS"
    elif operator_choice == "2":
        operator_user = "TELE2"
    elif operator_choice == "3":
        operator_user = "megafon"
    elif operator_choice == "4":
        operator_user = "beeline"

    for tariff_name, tariff_params in tariff_plans.items():
        if minutes <= tariff_params["minute_limit"] and messages <= tariff_params["message_limit"] and data_usage <= \
                tariff_params["data_limit"] and operator_user <= tariff_params["operator"]:
            recommended_tariff = tariff_name
            break
    import animation
    print("Рекомендуем вам тарифный план:", recommended_tariff)
    for tariff_name, tariff_params in tariff_plans.items():
        if tariff_name != recommended_tariff and tariff_params["nonthly_cost"] < tariff_plans[recommended_tariff]["nonthly_cost"]:
            print("Также вы можете рассмотреть тарифный план", tariff_name, "с более выгодной ценой.")
    confirm = input("Хотите подключить тарифный план " + recommended_tariff + "? (y/n)")
    if confirm == "y":

        import animation
        print("Тарифный план", recommended_tariff, "успешно подключен.")
        print("Ежемесячная плата составит:", tariff_plans[recommended_tariff]["nonthly_cost"], "rublikov.")
    else:
        print("Подключение тарифного плана отменено.")

    # Завершение работы приложения
    print("Спасибо за использование нашего приложения!")

if replace == "n":
    # Запрос подтверждения выбранного тарифа
    confirm = input("Хотите подключить тарифный план " + recommended_tariff + "? (y/n)")
    if confirm == "y":
        import animation
        print("Тарифный план", recommended_tariff, "успешно подключен.")
        print("Ежемесячная плата составит:", tariff_plans[recommended_tariff]["nonthly_cost"], "rublikov.")
    else:
        print("Подключение тарифного плана отменено.")

    # Завершение работы приложения
    print("Спасибо за использование нашего приложения!")

    # Вывод информации о выбранном тарифе и затратах пользователя










