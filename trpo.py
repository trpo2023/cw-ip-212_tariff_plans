# -*- coding: cp1251 -*-
# для очищения консоли
import os
def clear_console():
    os.system('cls')

from interface import main_menu
from interface import get_minutes
from interface import choose_messages
from interface import choose_data_usage
from tariff_plans import tariff_plans


#Вызов функции для выбора минут
minutes = get_minutes()
print(f"Вы выбрали {minutes} минут")

# для очищения консоли
print("Some output...")
clear_console()


#Вызов функции для выбора СМС
messages = choose_messages()
print(f"Вы выбрали {messages} сообщений")

# для очищения консоли
print("Some output...")
clear_console()


#Вызов функции для выбора ГБ
data_usage = choose_data_usage()
print("Вы выбрали", data_usage, "ГБ интернет-трафика.")


# для очищения консоли
print("Some output...")
clear_console()




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

operator = select_operator()
print("Выбран оператор:", operator_user)

    # для очищения консоли
print("Some output...")
clear_console()


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

    # для очищения консоли
    print("Some output...")
    clear_console()
 


    #Вызов функции для выбора минут
    minutes = get_minutes()
    print(f"Вы выбрали {minutes} минут")

    # для очищения консоли
    print("Some output...")
    clear_console()

    #Вызов функции для выбора СМС
    messages = choose_messages()
    print(f"Вы выбрали {messages} сообщений")

    # для очищения консоли
    print("Some output...")
    clear_console()    

    #Вызов функции для выбора ГБ
    data_usage = choose_data_usage()
    print("Вы выбрали", data_usage, "ГБ интернет-трафика.")

    # для очищения консоли
    print("Some output...")
    clear_console()

    # Предоставление вариантов выбора для оператора
    print("Выберите оператора:")
    print("1. MTS")
    print("2. TELE2")
    print("3. megafon")
    print("4. beeline")
    operator_choice = input("Введите номер выбранного варианта:")
    while operator_choice not in ["1", "2", "3", "4"]:
        operator_choice = input("Некорректный выбор. Введите номер выбранного варианта:")

        # для очищения консоли
    print("Some output...")
    clear_console()

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


        # для очищения консоли
        print("Some output...")
        clear_console()

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
        import animation
        print("Тарифный план", recommended_tariff, "успешно подключен.")
        print("Ежемесячная плата составит:", tariff_plans[recommended_tariff]["nonthly_cost"], "rublikov.")
    else:
        print("Подключение тарифного плана отменено.")
            # для очищения консоли
    print("Some output...")
    clear_console()

    # Завершение работы приложения
    print("Спасибо за использование нашего приложения!")

    # Вывод информации о выбранном тарифе и затратах пользователя
