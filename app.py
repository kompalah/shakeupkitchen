from flask import *
app =Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/aboutus")
def aboutus_ourservices():
    return render_template("aboutus_ourservices.html")
app.run(debug=True)