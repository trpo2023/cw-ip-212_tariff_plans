import subprocess

def run_app_test():
    # Запуск приложения и ввод команды для выбора опции 1 в главном меню
    process = subprocess.Popen(['python', 'main.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    process.stdin.write('1\n')
    process.stdin.flush()

    # Ввод необходимых данных для выбора тарифа
    process.stdin.write('6\n')
    process.stdin.write('10\n')
    process.stdin.write('15\n')
    process.stdin.write('20\n')
    process.stdin.write('21\n')
    process.stdin.write('non\n')
    process.stdin.flush()

    # Ожидание завершения выполнения приложения
    process.wait()

    # Получение вывода приложения
    output = process.stdout.read()

    # Проверка вывода на наличие ожидаемых результатов
    if 'Рекомендуем вам тарифный план' in output:
        print('Тест не пройден!')
    else:
        print('Тест пройден!')

run_app_test()
