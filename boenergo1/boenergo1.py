from flask import Flask, request, jsonify
import sqlite3
import math
import threading

app = Flask(__name__)

# Создаем базу данных
conn = sqlite3.connect('equations.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS equations (id INTEGER PRIMARY KEY AUTOINCREMENT, a REAL, b REAL, c REAL)')
conn.commit()

# Создаем объект блокировки
lock = threading.Lock()

@app.route('/equations', methods=['POST'])
def solve_equation():
    # Получаем значения a, b, c из запроса
    data = request.json
    a = data.get('a')
    b = data.get('b')
    c = data.get('c')

    # Рассчитываем дискриминант
    discriminant = b**2 - 4*a*c

    # Проверяем значения дискриминанта и рассчитываем корни уравнения
    if discriminant < 0:
        result = {'message': 'No real roots'}
    elif discriminant == 0:
        root = -b / (2*a)
        result = {'roots': [root]}
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        result = {'roots': [root1, root2]}

    # Сохраняем данные в базу данных
    with lock:
        cursor.execute('INSERT INTO equations (a, b, c) VALUES (?, ?, ?)', (a, b, c))
        conn.commit()

    return jsonify(result)

@app.route('/equations', methods=['GET'])
def get_equations():
    # Извлекаем все уравнения из базы данных
    with lock:
        cursor.execute('SELECT * FROM equations')
        equations = cursor.fetchall()

    result = []
    for equation in equations:
        equation_data = {
            'id': equation[0],
            'a': equation[1],
            'b': equation[2],
            'c': equation[3]
        }
        result.append(equation_data)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
