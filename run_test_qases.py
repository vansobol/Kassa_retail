import pytest

# Список тестов для запуска
tests = [
    "emulator_connect_test.py",
    "sale_and_return_test.py",
    "correction.py",
    "markirovka_test.py"
]

for test in tests:
    print(f"Запуск теста: {test}")

    # Запуск теста с использованием pytest
    result = pytest.main([test])

    # Вывод результатов
    if result == 0:
        print(f"Тест {test} успешно выполнен.")
    else:
        print(f"Тест {test} завершился с ошибкой.")
# Запуск первого теста
# subprocess.call(["pytest", "-s", "authorization_test.py::test_authorization_android"])
# # Запуск второго теста
# subprocess.call(["pytest", "-s", "emulator_connect_test.py::test_emulator"])
# # Запуск третьего теста
# subprocess.call(["pytest", "-s", "neva_connect_test.py::test_neva"])
# # Запуск четвертого теста
# subprocess.call(["pytest", "-s", "sale_and_return_test.py::test_sale_and_return"])
# tests_to_run = [
#     # "authorization_test.py::test_authorization_android",
#     "emulator_connect_test.py::test_emulator"
#     # "neva_connect_test.py::test_neva",
#     # "sale_and_return_test.py::test_sale_and_return"
# ]
#
# # файл для записи результатов
# with open("test_results.txt", "w") as output_file:
#     for test in tests_to_run:
#         # Запуск теста с перенаправлением вывода в файл
#         process = subprocess.Popen(["pytest", test], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
#         stdout, _ = process.communicate()
#
#         # Запись вывода (stdout) в файл
#         output_file.write(stdout)
#
#         # Оценить результат выполнения теста и записать его в файл
#         if process.returncode == 0:
#             output_file.write(f"Test '{test}' PASSED\n")
#         else:
#             output_file.write(f"Test '{test}' FAILED or  EXCEPTION\n")