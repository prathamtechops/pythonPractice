import random

chars = 'qwertyuiopasdfghjklzxcvbnmAQZWSXCDERFVBGTYHNMNJUKOLP1234567890!@'

while True:
    password_len = int(input('How many letters should your password be: '))
    password_count = int(input('How many password do you want: '))
    for x in range(0,password_count):
        password = ''
        for x in range(0,password_len):
            password = "".join(random.sample(chars, password_len))
        print(password)
        

