import flask
from flask import render_template


create_app = flask.Flask(__name__)


@create_app.route('/', methods=['GET', 'POST'])
def index():
    number1 = flask.request.form.get('number1')
    number2 = flask.request.form.get('number2')

    if not number1 or not number2:
        return render_template('index.html')

    return render_template(
        'index.html',
        result=int(number1) + int(number2),
    )


if __name__ == '__main__':
    create_app.run(host='localhost', port=5000, debug=True)
