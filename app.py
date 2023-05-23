from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  "id": 1,
  "title": "Data Analyst",
  "locality": "Abidjan",
  "salary": "100,000 Fcfa"
}, {
  "id": 2,
  "title": "Data Scientist",
  "locality": "Abidjan",
  "salary": "100,000 Fcfa"
}, {
  "id": 3,
  "title": "Monitoring and Evaluation",
  "locality": "Maroua"
}]


@app.route("/")
def hello_issa():
  return render_template("home.html", jobs=JOBS, company_name="Abidjan")

@app.route("/api/jobs")
def list_json():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
