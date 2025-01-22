from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to AWS App Runner! Your Python application is running successfully."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
