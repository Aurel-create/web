from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Connexion à PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="web_Table",
        user="<postgres>",
        password="<Aurel229i>",
        host="localhost",
        port="5432"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM taches;')
    taches = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', taches=taches)

@app.route('/ajouter', methods=['POST'])
def ajouter():
    titre = request.form['titre']
    description = request.form['description']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO taches (titre, description) VALUES (%s, %s);', (titre, description))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
