# Написать программу, которая открывает URL в браузере с использованием декоратора

import webbrowser

def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Неверно введенное URL")
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)
    
open_url("http://yandex.ru")