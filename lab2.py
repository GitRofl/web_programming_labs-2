from flask import  Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route("/lab2/exemple")
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


@lab2.route("/lab2/")
def lab():
   return render_template('lab2.html')


@lab2.route("/lab2/scenery")
def lab2_2():
   return render_template('lab2_2.html')