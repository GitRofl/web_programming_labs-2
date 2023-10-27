from flask import  Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')
 
 
@lab3.route('/lab3/forml')
def forml():
   
   errors = {}
   user = request.args.get('user')
   if user == '':
      errors['user'] = 'Заполните поле!'
      
   age = request.args.get('age')
   if age == '':
      errors['age'] = 'Заполните поле!'
  
   type = request.args.get('type')
   
   place = request.args.get('place')
   
   baggage = request.args.get('baggage')
   
   point = request.args.get('point')
   if point == '':
      errors['point'] = 'Заполните поле!'
   
   point2 = request.args.get('point2')
   if point2 == '':
      errors['point2'] = 'Заполните поле!'
   
   date = request.args.get('date')
 
   
   sex = request.args.get('sex')

      
   return render_template('forml.html', date=date, point=point, point2=point2, user=user, age=age, baggage=baggage, sex=sex, errors=errors, type=type, place=place)


@lab3.route('/lab3/order')
def order():
   return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
   price = 0
   drink = request.args.get('drink')
   if drink == 'cofee':
      price = 120
   elif drink == 'black-tea':
      price = 80
   else:
      price = 70
      
      
   if request.args.get('milk') == 'on':
      price +=30
   if request.args.get('sugar') == 'on':
      price += 10
   return render_template('pay.html', price=price)

@lab3.route('/lab3/success')
def success():
   return render_template('success.html')

@lab3.route('/lab3/ticket')
def ticket():
   errors = {}
   place = request.args.get('place')
   
   type = request.args.get('type')
   
   name_1 = request.args.get('name_1')
   if name_1 == '':
      errors['name_1'] = 'Заполните поле!'
      
   name_2 = request.args.get('name_2')
   if name_2 == '':
      errors['name_2'] = 'Заполните поле!'
   
   baggage = request.args.get('baggage')
   
   point = request.args.get('point')
   if point == '':
      errors['point'] = 'Заполните поле!'
   
   point2 = request.args.get('point2')
   if point2 == '':
      errors['point2'] = 'Заполните поле!'
   
   date = request.args.get('date')
   
   user = request.args.get('user')
   if user == '':
      errors['user'] = 'Заполните поле!'
      
   age = request.args.get('age')
   
   return render_template('ticket.html', user=user, age=age, errors=errors, place=place, type=type, name_1=name_1, name_2=name_2, baggage=baggage, point=point, point2=point2, date=date)
