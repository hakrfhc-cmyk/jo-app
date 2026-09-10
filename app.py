
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


# مسارات تفاعلية لكل صف دراسي على حدة (من الأول للتوجيهي)
@app.route("/grade/1")
def grade_1():
  return render_template("subjects.html")


@app.route("/grade/2")
def grade_2():
  return render_template("subjects.html")


@app.route("/grade/3")
def grade_3():
  return render_template("subjects.html")


@app.route("/grade/4")
def grade_4():
  return render_template("subjects.html")


@app.route("/grade/5")
def grade_5():
  return render_template("subjects.html")


@app.route("/grade/6")
def grade_6():
  return render_template("subjects.html")


@app.route("/grade/7")
def grade_7():
  return render_template("subjects.html")


@app.route("/grade/8")
def grade_8():
  return render_template("subjects.html")


@app.route("/grade/9")
def grade_9():
  return render_template("subjects.html")


@app.route("/grade/10")
def grade_10():
  return render_template("subjects.html")


@app.route("/field/health")
def field_health():
  return render_template("subjects.html")


@app.route("/field/engineering")
def field_engineering():
  return render_template("subjects.html")


@app.route("/field/business")
def field_business():
  return render_template("subjects.html")


@app.route("/field/humanities")
def field_humanities():
  return render_template("subjects.html")


@app.route("/field/btec")
def field_btec():
  return render_template("subjects.html")


@app.route("/quiz")
def quiz():
  return render_template("quiz.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)

