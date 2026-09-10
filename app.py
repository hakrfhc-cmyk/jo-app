from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/grades")
def grades():
  return render_template("grades.html")


@app.route("/subjects")
def subjects():
  return render_template("subjects.html")


@app.route("/quiz")
def quiz():
  return render_template("quiz.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)

