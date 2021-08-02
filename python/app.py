from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello SGERBOTHe uses flux and dockerpw feature_branch trigger pullrequest!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
