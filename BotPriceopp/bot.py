import telebot
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from transliterate import slugify
from selenium.common.exceptions import NoSuchElementException
from fake_useragent import UserAgent
from proxy_auth import login, password
from seleniumwire import webdriver
from token_auth_data import tok
import time

bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}. Введи запрос для поиска!</b>.'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.chat.id, "Привет. Введи запрос для поиска и я найду это!")
    else:
        bot.send_message(message.chat.id, "Поиск начался. Может занять до 3-х минут....")
        options = webdriver.ChromeOptions()
        options.headless = True
    
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        ua = UserAgent()
        user_agent = ua.random
        options.add_argument(f'user-agent={user_agent}')     
        options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        options_wire = {
        'proxy': {
                'https': f'socks5://{login}:{password}@196.17.64.72:8000',
                'http': f'socks5://{login}:{password}@196.17.64.72:8000',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }
        driver = webdriver.Chrome(seleniumwire_options=options_wire)
    
        # driver = webdriver.Chrome(options=options)
        print('Start Search, we need 10 sec.....')
        url = 'https://duckduckgo.com/'
        driver.get(url)
    
        time.sleep(10)
        search = driver.find_element(By.ID, 'search_form_input_homepage')
        search.send_keys(message.text)
        button = driver.find_element(By.ID, 'search_button_homepage')
        button = driver.find_element(By.ID, 'search_button_homepage')
        button.click()
        time.sleep(2)
        try:
            button = driver.find_element(By.ID, 'rld-1')
            button.click()
        except NoSuchElementException:
            pass
        time.sleep(2)
        try:
            button = driver.find_element(By.ID, 'rld-1')
            button.click()
        except NoSuchElementException:
            pass

        try:
            res1 = driver.find_element(By.ID, 'r1-1').text
            res1 = res1.replace(' › ', '/')
        except NoSuchElementException:
            res1 = None
        time.sleep(2)
        try:
            res2 = driver.find_element(By.ID, 'r1-2').text
            res2 = res2.replace(' › ', '/')
        except NoSuchElementException:
            res2 = None
        time.sleep(2)
        try:
            res3 = driver.find_element(By.ID, 'r1-3').text
            res3 = res3.replace(' › ', '/')
        except NoSuchElementException:
            res3 = None
        time.sleep(2)
        bot.send_message(message.chat.id, res1)
        bot.send_message(message.chat.id, res2)
        bot.send_message(message.chat.id, res3)
        bot.send_message(message.chat.id, "Готово! Введите следующий запрос")
        

bot.polling(none_stop=True)
