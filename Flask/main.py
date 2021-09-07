from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "This is the about page which is empty"

if __name__ == '__main__':
    app.run(debug=True)