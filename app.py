from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, CI/CD! Welcome to our App, We have successfully deployed our app on Azure Platform and integerated with GitHub Actions!!"

if __name__ == '__main__':
    app.run(debug=True)
