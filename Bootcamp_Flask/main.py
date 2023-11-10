from flask import Flask # Flask объект

app = Flask(__name__)

@app.route('/') #GET - по умолчанию
def main():
    return '<h1>HELLO, WORLD!</h1>'

@app.route('/info')
def inf():
    return '<h1>Ну как-то так!</h1>'

@app.route('/summa/<x>/<y>')
def summ(x, y):
    return f'<h1>{x} + {y} = {int(x) + int(y)}</h1>'

if __name__ == '__main__':
    app.run()