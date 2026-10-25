
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CCA 2 - CI/CD Pipeline - Version 2</h1>
    <p>My Flask application is running successfully!</p>
    <p>Deployed using Jenkins, Docker and Kubernetes.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
