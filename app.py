from flask import Flask
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="YOUR-RDS-ENDPOINT",
    user="admin",
    password="YOUR_PASSWORD",
    database="webappdb"
)

@app.route("/")
def home():
    return "AWS 3-Tier Web Application Running"

@app.route("/users")
def users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    result = "<h1>Users List</h1>"
    for user in data:
        result += f"<p>ID: {user[0]} | Name: {user[1]} | Email: {user[2]}</p>"

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)