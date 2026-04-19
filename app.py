from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    result = ""

    if request.method == "POST":

        email = request.form.get("email")

        if "@" in email:
            result = "Email to‘g‘ri"
        else:
            result = "Email noto‘g‘ri"

    return render_template("index.html", result=result)

app.run(debug=True)
