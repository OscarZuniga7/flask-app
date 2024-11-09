from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenido a la aplicación web!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
