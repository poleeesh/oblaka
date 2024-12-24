from flask import Flask, request, jsonify
import redis
import os

HOST = os.getenv("REDIS_HOST")

HELM_VARIABLE = os.environ.get("HELM_VARIABLE") or "default"

app = Flask(__name__)

# Подключение к Redis
redis_client = redis.StrictRedis(host=HOST, port=6379, db=0, decode_responses=True)

@app.route('/', methods=['GET'])
def get_list_1():
    # Получение значений из списка в Redis
    return f"Hello {HELM_VARIABLE}"

@app.route('/add', methods=['POST'])
def add_to_list():
    # Получение данных из запроса
    data = request.json

    # Проверка на наличие ключа `value`
    if 'value' not in data:
        return jsonify({'error': 'Missing value'}), 400

    # Добавление значения в список в Redis
    redis_client.rpush('my_list', data['value'])

    return jsonify({'message': 'Value added successfully'}), 201

@app.route('/list', methods=['GET'])
def get_list():
    # Получение значений из списка в Redis
    my_list = redis_client.lrange('my_list', 0, -1)
    return jsonify(my_list), 200

if __name__ == '__main__':
    app.run(debug=True)