from flask import  Blueprint, render_template, request, redirect
import psycopg2


lab5 = Blueprint('lab5', __name__)


def dbConnect():
   conn = psycopg2.connect(
      host = "127.0.0.1",
      database = "knowledge_base_for_artem",
      user = "artem_knowledge_base",
      password = "123")
   return conn;

def dbClose (cursor, connecttion):
   cursor.close()
   connecttion.close()

@lab5.route("/lab5/")
def main():
   visibleUser = "Anon"
   
   return render_template("lab5.html", username=visibleUser);

@lab5.route("/lab5/users")
def users():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_artem",
        user="artem_knowledge_base",
        password="123"
    )

    cur = conn.cursor()

    cur.execute("SELECT username FROM users;")

    result = cur.fetchall()

    cur.close()
    conn.close()

    
    return render_template("users.html", users=result);