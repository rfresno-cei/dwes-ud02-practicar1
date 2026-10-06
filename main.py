# Exercise 1
import math


a = 12
b = 30
sum = a + b
subtraction = a - b
product = a * b
division = a / b
print(f'The result of the sum is {sum}')
print(f'The result of the subtraction is {subtraction}')
print(f'The result of the product is {product}')
print(f'The result of the division is {division}')

# Exercise 2
celsius = 20
fahrenheit = celsius * 1.8 + 32
print(f'{celsius} ºC is equivalent to {fahrenheit} ºF')
km = 100
feet = km * 3280.84
miles = km * 0.621371
print(f'{km} km is equivalent to {feet} ft')
print(f'{km} km is equivalent to {miles} mi')
euros = 1280
pounds = euros * 0.85
dollars = euros * 1.12
print(f'{euros} € is equivalent to {pounds} GBP')
print(f'{euros} € is equivalent to {dollars} $')

# Exercise 3
grade1 = 3
grade2 = 8
grade3 = 6.2
grade4 = 10
avg = (grade1 + grade2 + grade3 + grade4) / 4
passed = avg >= 5
print(f'The average grade is {avg}. The student has passed the subject: {passed}')

# Exercise 4
number = 4
even = number % 2 == 0
print(f'The number {number} is even: {even}')

# Exercise 5
number_range = 7
lower_bound = 0
upper_bound = 10
in_range = number_range > lower_bound and number_range < upper_bound
print(f'The number {number_range} is between {lower_bound} and {upper_bound}: {in_range}')

# Exercise 6
number_mult = 10
mult3 = number_mult % 3 == 0
mult5 = number_mult % 5 == 0
mult7 = number_mult % 7 == 0
print(f'The number {number_mult} is a multiple of 3: {mult3}')
print(f'The number {number_mult} is a multiple of 5: {mult5}')
print(f'The number {number_mult} is a multiple of 7: {mult7}')

# Exercise 7
side = 4
perimeter_sq = side * 4
area_sq = side ** 2
print(f'The perimeter of the square is {perimeter_sq}')
print(f'The area of the square is {area_sq}')
base = 5
height = 7
area_tr = base * height / 2
print(f'The area of the triangle is {area_tr}')
radius = 11
perimeter_ci = math.pi * radius * 2
area_ci = math.pi * radius ** 2
print(f'The perimeter of the circle is {perimeter_ci}')
print(f'The area of the circle is {area_ci}')
cat1 = 4
cat2 = 7
hyp = math.sqrt(cat1 ** 2 + cat2 **2)
print(f'The hypotenuse is {hyp}')

# Exercise 8
name = 'Brandoor'
price = 20
units = 3
tax = 20
print(f'Product: {name}')
print(f'Unit price: {price}')
print(f'Units: {units}')
print(f'Subtotal: {price * units} €')
print(f'Tax: {tax}%')
print(f'Total: {(price * units) + (price * units) * tax / 100 }')

# Exercise 9
total_seconds = 3672
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f'{hours} hours, {minutes} minutes and {seconds} seconds')