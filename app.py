from flask import  Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/lab2/example")
def example():
   name= 'Артём Басман'
   lab_number= 'Лабораторная работа 2'
   group= 'ФБИ-12' 
   n_class= '3 курс'
   fruits= [
      {'name': 'яблоки', 'price':100},
      {'name': 'груши', 'price':120},
      {'name': 'апельсины', 'price':80},
      {'name': 'мандарины', 'price':95},
      {'name': 'манго', 'price':321},
      ]
   book= [
      {'name':'"Мастер и Маргарита"', 'name_b': 'Михаил Булгаков', 'genre': 'фантастика, магический реализм', 'pages': 'около 400 страниц'},
      {'name':'"100 лет одиночества"', 'name_b': 'Габриэль Гарсиа Маркес', 'genre': 'магический реализм', 'pages': 'около 400 страниц'},
      {'name':'"Убить пересмешника"', 'name_b': 'Харпер Ли', 'genre': 'драма, социальная критика', 'pages': 'около 300 страниц'},
      {'name':'"1984"', 'name_b': 'Джордж Оруэлл', 'genre': 'дистопия', 'pages': 'около 300 страниц'},
      {'name':'"Война и мир"', 'name_b': 'Лев Толстой', 'genre': 'историческая проза', 'pages': 'более 1 000 страниц'},
      {'name':'"Мастер Гарденер"', 'name_b': 'Рабиндранат Тагор', 'genre': 'поэзия, религиозная литература', 'pages': 'около 200 страниц'},
      {'name':'"Анна Каренина"', 'name_b': 'Лев Толстой', 'genre': 'роман', 'pages': 'около 800 страниц'},
      {'name':'"Гордость и предубеждение"', 'name_b': 'Джейн Остин', 'genre': 'роман', 'pages': 'около 300 страниц'},
      {'name':'"Над пропастью во ржи"', 'name_b': 'Джером Д. Сэлинджер', 'genre': 'современная классика', 'pages': 'около 200 страниц'},
      {'name':'"Преступление и наказание"', 'name_b': 'Федор Достоевский', 'genre': 'Роман', 'pages': 'около 600'}
   ]
   # return render_template('example.html')
   return render_template('example.html', name=name, lab_number=lab_number, group=group, n_class=n_class, fruits=fruits, book=book )

@app.route("/lab2/")
def lab2():
   return render_template('lab2.html')

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