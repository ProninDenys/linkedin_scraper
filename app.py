from flask import Flask, render_template, request
from scraper import get_job_listings  

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    jobs = []
    search_query = ""
    
    if request.method == "POST":
        search_query = request.form.get("search")
        jobs = get_job_listings(search_query)  

    return render_template("index.html", jobs=jobs, search_query=search_query)

if __name__ == "__main__":
    app.run(debug=True)
