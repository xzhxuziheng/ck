"""
coder: xuziheng
date: 2022/9/20 15:02
"""
import flask
from flask import jsonify


app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({"code": 1, "msg": "hello python"})


if __name__ == '__main__':
    app.run(debug=True)