from flask import  Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
   return """
   <!DOCTYPE html>
      <html lang="ru">
      <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>НГТУ, ФБ, Лабораторные работы</title>
         <link rel="stylesheet" href=" """ + url_for('static', filename='lab1.css') +  """" ">
      </head>
      <body>
         <header class="xd">
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
         </header>
         
         <a href="/lab1">Первая лабораторная</a>
         
         <footer class="xd">
            &copy; Басман Артём, ФБИ-12, 3 курс, 2023
         </footer>

      </body>
   </html>
 """
 
@app.route("/lab1")
def lab1():
   return """
      <!DOCTYPE html>
      <html lang="ru">
      <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Basman Artem. lab 1.</title>
         <link rel="stylesheet" href=" """ + url_for('static', filename='lab1.css') +  """" ">
      </head>
      <body>
         <header class="xd">
            НГТУ, ФБ, Лабораторная работа № 1
         </header>

         <h1>web-сервер на flask</h1>
         <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
         </div>
         <a href="/menu">Меню</a>
         
         <h2>Реализованные роуты</h2>
         <ul>
            <li> <a href="/lab1/oak">Дуб</a> </li>
            <li> <a href="/lab1/student">Студент</a> </li>
            <li> <a href="/lab1/python">Питон</a> </li>
            <li> <a href="/lab1/ogr">Шрек</a> </li>
         </ul>
         
         <footer class="xd">
            &copy; Басман Артём, ФБИ-12, 3 курс, 2023
         </footer>

      </body>
      </html>
   """
   
@app.route("/lab1/oak")
def oak():
   return '''
   <!DOCTYPE html>
   <html lang="ru">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>DUB</title>
      <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +  '''">
   </head>
   <body>
   
      <a href="/lab1">Назад</a>
   
      <h1>Дуб</h1>
     
      <img src="''' + url_for('static', filename='oak.jpg') + '''">
   </body>
   </html>
'''
@app.route("/lab1/student")
def student():
   return '''
   <!DOCTYPE html>
   <html lang="ru">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Student</title>
      <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +  '''">
   </head>
   <body>
      <a href="/lab1">Назад</a>
      <h1>Басман Артем Игоревич</h1>
      <img class="log" src="''' + url_for('static', filename='nstu.jpg') + '''">
   </body>
   </html>
'''

@app.route("/lab1/python")
def python():
   return '''
   <!DOCTYPE html>
   <html lang="ru">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Python</title>
      <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +  '''">
   </head>
   <body>
      <a href="/lab1">Назад</a>
      <h1>Python</h1>
      <div class="p"> Python — это язык программирования, который широко используется в интернет-приложениях,
      разработке программного обеспечения, науке о данных и машинном обучении (ML). Разработчики используют Python,
      потому что он эффективен, прост в изучении и работает на разных платформах. Программы на языке
      Python можно скачать бесплатно, они совместимы со всеми типами систем и повышают скорость разработки. </div>
      <img src="''' + url_for('static', filename='pyt.jpg') + '''">
   </body>
   </html>
'''

@app.route("/lab1/ogr")
def ogr():
   return '''
   <!DOCTYPE html>
   <html lang="ru">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Shrek</title>
      <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +  '''">
   </head>
   <body>
      <a href="/lab1">Назад</a>
      <h1>Шрек</h1>
      <div class="p">
         Жил да был в сказочном государстве большой зеленый великан по имени Шрэк.
         Жил он в гордом одиночестве в лесу, на болоте, которое считал своим.
         Но однажды злобный коротышка — лорд Фаркуад, правитель волшебного королевства,
         безжалостно согнал на Шрэково болото всех сказочных обитателей.
      </div>
      <div class="p">
         И беспечной жизни зеленого великана пришел конец. Но лорд Фаркуад пообещал вернуть
         Шрэку болото, если великан добудет ему прекрасную принцессу Фиону, которая томится
         в неприступной башне, охраняемой огнедышащим драконом.
      </div>
      <img class="sh" src="''' + url_for('static', filename='org.jpg') + '''">
   </body>
   </html>
'''