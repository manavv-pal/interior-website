from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- SERVICES ----------------
@app.route("/services")
def services():
    return render_template("services.html")


# ---------------- PROJECTS ----------------
@app.route("/projects")
def projects():
    return render_template("projects.html")


# ---------------- CONTACT PAGE ----------------
@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------------- FORM SUBMIT ----------------
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    phone = request.form["phone"]
    message = request.form["message"]

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, phone, message) VALUES (?, ?, ?)",
        (name, phone, message),
    )

    conn.commit()
    conn.close()

    return "Form Submitted Successfully!"


@app.route("/admin")
def admin():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()

    return render_template("admin.html", data=data)


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
