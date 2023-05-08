# -*- coding: cp1251 -*-



#Минуты
def get_minutes():
    # Предоставление вариантов выбора для количества минут
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


#СМС
def choose_messages():
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


#ГБ
def choose_data_usage():
    # Предоставление вариантов выбора для объема интернет-трафика
    print("Выберите объем интернет-трафика в ГБ:")
    print("1. 10 ГБ")
    print("2. 20 ГБ")
    print("3. 35 ГБ")
    print("4. 45 ГБ")
    print("5. 50 ГБ")
    print("6. 60 ГБ")
    
    # Запрос выбора пользователя и проверка его корректности
    data_usage_choice = input("Введите номер выбранного варианта:")
    while data_usage_choice not in ["1", "2", "3","4", "5", "6"]:
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



#Операторы

#def select_operator():
#    # Предоставление вариантов выбора для оператора
#    print("Выберите оператора:")
#    print("1. MTS")
#    print("2. TELE2")
#    print("3. megafon")
#    print("4. beeline")
#    operator_choice = input("Введите номер выбранного варианта:")
    
#    # Проверка на корректность ввода и получение оператора в соответствии с выбором пользователя
#    while operator_choice not in ["1", "2", "3", "4"]:
#        operator_choice = input("Некорректный выбор. Введите номер выбранного варианта:")
    
#    if operator_choice == "1":
#        operator_user = "MTS"
#    elif operator_choice == "2":
#        operator_user = "TELE2"
#    elif operator_choice == "3":
#        operator_user = "megafon"
#    elif operator_choice == "4":
#        operator_user = "beeline"
    
#    return operator_user







tariff_plans = {
"My_Online+": {"minute_limit": 600, "message_limit": 400,  "data_limit": 35, "operator":str("TELE2"), "nonthly_cost":550}, 
"Black": {"minute_limit": 1000, "message_limit": 1000,  "data_limit": 50, "operator":str("TELE2"), "nonthly_cost":800},
"Super_Online+": {"minute_limit": 600, "message_limit": 500,  "data_limit": 45, "operator":str("TELE2"), "nonthly_cost":600},
"My_Online": {"minute_limit": 600, "message_limit": 400,  "data_limit": 20, "operator":str("TELE2"), "nonthly_cost":450},
"My_conversation": {"minute_limit": 250, "message_limit": 300,  "data_limit": 10, "operator":str("TELE2"), "nonthly_cost":380},
"Premium": {"minute_limit": 2000, "message_limit": 500,  "data_limit": 60, "operator":str("TELE2"), "nonthly_cost":1500},
"Warm_welcome_S": {"minute_limit": 250, "message_limit": 500,  "data_limit": 10, "operator":str("megafon"), "nonthly_cost":380},
"Warm_welcome_L": {"minute_limit": 600, "message_limit": 700,  "data_limit": 35, "operator":str("megafon"), "nonthly_cost":550},
"MegaTarif": {"minute_limit": 600, "message_limit": 500,  "data_limit": 35, "operator":str("megafon"), "nonthly_cost":550},
"Maximum": {"minute_limit": 900, "message_limit": 200,  "data_limit": 45, "operator":str("megafon"), "nonthly_cost":750},
"VIP": {"minute_limit": 1200, "message_limit": 300,  "data_limit": 50, "operator":str("megafon"), "nonthly_cost":1000},
"Permium": {"minute_limit": 3000, "message_limit": 3000,  "data_limit": 60, "operator":str("megafon"), "nonthly_cost":2000},
"Bee_Bazya": {"minute_limit": 600, "message_limit": 100,  "data_limit": 45, "operator":str("Beeline"), "nonthly_cost":650},
"Dragon_Jung": {"minute_limit": 500, "message_limit": 500,  "data_limit": 45, "operator":str("Beeline"), "nonthly_cost":580},
"cat_pus": {"minute_limit": 900, "message_limit": 800,  "data_limit": 45, "operator":str("Beeline"), "nonthly_cost":730},
"panda_tapa": {"minute_limit": 300, "message_limit": 700,  "data_limit": 20, "operator":str("Beeline"), "nonthly_cost":470},
"robot_ping": {"minute_limit": 500, "message_limit": 600,  "data_limit": 35, "operator":str("Beeline"), "nonthly_cost":530},
"To_the_maximum!": {"minute_limit": 3000, "message_limit": 3000,  "data_limit": 60, "operator":str("Beeline"), "nonthly_cost":1800}
}

#Вызов функции для выбора минут
minutes = get_minutes()
print(f"Вы выбрали {minutes} минут")

#Вызов функции для выбора СМС
messages = choose_messages()
print(f"Вы выбрали {messages} сообщений")

#Вызов функции для выбора ГБ
data_usage = choose_data_usage()
print("Вы выбрали", data_usage, "ГБ интернет-трафика.")



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

#operator = select_operator()
#print("Выбран оператор:", operator_user)


for tariff_name, tariff_params in tariff_plans.items():
    if minutes <= tariff_params["minute_limit"] and messages <= tariff_params["message_limit"] and data_usage <= tariff_params["data_limit"] and operator_user <= tariff_params["operator"] :
        recommended_tariff = tariff_name
        break

#import animation

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
 


    #Вызов функции для выбора минут
    minutes = get_minutes()
    print(f"Вы выбрали {minutes} минут")

    #Вызов функции для выбора СМС
    messages = choose_messages()
    print(f"Вы выбрали {messages} сообщений")

    #Вызов функции для выбора ГБ
    data_usage = choose_data_usage()
    print("Вы выбрали", data_usage, "ГБ интернет-трафика.")

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

    #import animation

    print("Рекомендуем вам тарифный план:", recommended_tariff)
    for tariff_name, tariff_params in tariff_plans.items():
        if tariff_name != recommended_tariff and tariff_params["nonthly_cost"] < tariff_plans[recommended_tariff]["nonthly_cost"]:
            print("Также вы можете рассмотреть тарифный план", tariff_name, "с более выгодной ценой.")
    confirm = input("Хотите подключить тарифный план " + recommended_tariff + "? (y/n)")
    if confirm == "y":

        #import animation
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
        #import animation
        print("Тарифный план", recommended_tariff, "успешно подключен.")
        print("Ежемесячная плата составит:", tariff_plans[recommended_tariff]["nonthly_cost"], "rublikov.")
    else:
        print("Подключение тарифного плана отменено.")

    # Завершение работы приложения
    print("Спасибо за использование нашего приложения!")

    # Вывод информации о выбранном тарифе и затратах пользователя