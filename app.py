from flask import Flask, render_template

app = Flask("index.html")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return '<h2>Это главная страница</h2><p>Добро пожаловать на главную страницу!</p>'

@app.route('/buy')
def buy():
    return '<h2>Купить</h2><p>Здесь вы можете купить наши товары.</p>'

@app.route('/info')
def info():
    return '<h2>Информация</h2><p>Здесь представлена информация о нашем сайте и услугах.</p>'

if __name__ == '__main__':
    app.run(debug=True)
