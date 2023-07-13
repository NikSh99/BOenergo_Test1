

В качестве реализации первого тестового задания реализован простой веб-сервис,
который находит корни квадратного уравнения a*x^2 + b*x + c = 0 и сохраняет их в базе данных.
Сервис реализован с использованием фреймворка Flask и базы данных SQLite. Состоит из двух модулей - основного листинга и модуля тестов.

Веб-сервис будет доступен по адресу http://localhost:5000

Чтобы решить квадратное уравнение, отправьте POST-запрос на http://localhost:5000/equations с JSON, содержащим значения a, b и c. Вот пример команды для PowerShell:
Invoke-WebRequest -Method POST -Uri "http://localhost:5000/equations" -Headers @{"Content-Type" = "application/json"} -Body '{"a": 1, "b": -3, "c": 2}'

![image](https://github.com/NikSh99/BOenergo_Test1/assets/43999726/9b35f83a-36c6-4ebe-8cae-b8f987267be8)

В результате вы получите JSON-ответ с корнями уравнения.

Чтобы получить список ранее решенных уравнений из базы данных, отправьте GET-запрос на http://localhost:5000/equations. Вот команда для PowerShell:
Invoke-WebRequest -Uri "http://localhost:5000/equations"

![image](https://github.com/NikSh99/BOenergo_Test1/assets/43999726/49063506-a0cf-48c4-aab0-9b539bb86440)


В результате вы получите JSON-ответ со списком ранее решенных уравнений.

Для запуска тестов открыть консоль из корневой папки проекта и ввести: "python test.py"
![image](https://github.com/NikSh99/BOenergo_Test1/assets/43999726/da940f54-baa7-4fd4-afd4-53d410b4e2ae)
