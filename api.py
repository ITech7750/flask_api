from flask import Flask, request, jsonify
from flasgger import Swagger
from regression_service import *
from mixing_service import *

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/regression', methods=['POST'])
def process_data_regression():
    """
    Обрабатывает данные для регрессии.

    ---
    parameters:
      - name: regression_data
        in: body
        required: true
        schema:
          properties:
            regression_la:
              type: array
              items:
                type: number
            regression_kip:
              type: array
              items:
                type: number
    responses:
      200:
        description: Результат регрессии.
    """
    # Получаем данные из запроса
    data = request.get_json()

    # Получаем regression_la и regression_kip из данных
    regression_la = data.get('regression_la', [])
    regression_kip = data.get('regression_kip', [])
    result = RegressionImplementation.implement_regression(regression_la, regression_kip)

    # Возвращаем результат в формате JSON
    return jsonify(result)


@app.route('/api/mixing', methods=['POST'])
def process_data_mixing():
    """
    Обрабатывает данные для смешивания.

    ---
    parameters:
      - name: mixing_data
        in: body
        required: true
        schema:
          properties:
            mixing:
              type: array
              items:
                type: number
            L:
              type: array
              items:
                type: number
            d:
              type: array
              items:
                type: number
            D:
              type: array
              items:
                type: number
    responses:
      200:
        description: Результат смешивания.
    """

    # Получаем данные из запроса
    data = request.get_json()

    # Получаем массив mixing из данных
    mixing = data.get('mixing', [])
    L = data.get('L', [])
    d = data.get('d', [])
    D = data.get('D', [])
    result = МixingService.mixing_implementation(mixing,L,d,D)
    # Возвращаем результат в формате JSON
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
