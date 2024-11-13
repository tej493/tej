from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Data to pass to the HTML template
    projects = [
        {"title": "Project 1", "description": "Description of project 1", "image": "project1.jpg"},
        {"title": "Project 2", "description": "Description of project 2", "image": "project2.jpg"},
        # Add more projects as needed
    ]
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
