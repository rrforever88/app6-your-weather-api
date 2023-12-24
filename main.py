from flask import Flask, render_template

# Create a website object
app = Flask(__name__)


# Referred to HTML pages (pages need to be in "templates" folder inside root directory)
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
