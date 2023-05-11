from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from transliterate import slugify
from selenium.common.exceptions import NoSuchElementException
from fpdf import FPDF
import cleantext
import re
import time

# def try_repeat(func):
#     def wrapper(*args, **kwargs):
#         count = 10
#         while count:
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 print('Error:', e)
#                 count -= 1
#     return wrapper

# @try_repeat
def search(request):
    alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
            "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
    name = request.POST.get("name")
    if name is None or len(name) == 0:
        name = 'I Love this site'
        
    options = webdriver.ChromeOptions()
    options.headless = True
 
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')       
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)
    print('Start Search, we need 10 sec.....')
    url = 'https://duckduckgo.com/'
    driver.get(url)
   
    time.sleep(5)
    search = driver.find_element(By.ID, 'search_form_input_homepage')
    search.send_keys(name)
    button = driver.find_element(By.ID, 'search_button_homepage')
    button = driver.find_element(By.ID, 'search_button_homepage')
    button.click()
    time.sleep(5)
    try:
        button = driver.find_element(By.ID, 'rld-1')
        button.click()
    except NoSuchElementException:
        pass
    time.sleep(5)
    try:
        button = driver.find_element(By.ID, 'rld-1')
        button.click()
    except NoSuchElementException:
        pass

    try:
        res1 = driver.find_element(By.ID, 'r1-1').text
        res1 = res1.replace(' › ', '/')
    except NoSuchElementException:
        res1 = "None"
    time.sleep(2)
    try:
        res2 = driver.find_element(By.ID, 'r1-2').text
        res2 = res2.replace(' › ', '/')
    except NoSuchElementException:
        res2 = "None"
    time.sleep(2)
    try:
        res3 = driver.find_element(By.ID, 'r1-3').text
        res3 = res3.replace(' › ', '/')
    except NoSuchElementException:
        res3 = "None"
    time.sleep(2)
    try:
        res4 = driver.find_element(By.ID, 'r1-4').text
        res4 = res4.replace(' › ', '/')
    except NoSuchElementException:
        res4 = "None"
    time.sleep(2)
    try:
        res5 = driver.find_element(By.ID, 'r1-5').text
        res5 = res5.replace(' › ', '/')
    except NoSuchElementException:
        res5 = "None"
    time.sleep(2)
    try:
        res6 = driver.find_element(By.ID, 'r1-6').text
        res6 = res6.replace(' › ', '/')
    except NoSuchElementException:
        res6 = "None"
    time.sleep(2)
    try:
        res7 = driver.find_element(By.ID, 'r1-7').text
        res7 = res7.replace(' › ', '/')
    except NoSuchElementException:
        res7 = "None"
    time.sleep(2)
    try:
        res8 = driver.find_element(By.ID, 'r1-8').text
        res8 = res8.replace(' › ', '/')
    except NoSuchElementException:
        res8 = "None"
    time.sleep(2)
    try:
        res9 = driver.find_element(By.ID, 'r1-9').text
        res9 = res9.replace(' › ', '/')
    except NoSuchElementException:
        res9 = "None"
    time.sleep(2)
    try:
        res10 = driver.find_element(By.ID, 'r1-10').text
        res10 = res10.replace(' › ', '/')
    except NoSuchElementException:
        res10 = "None"
    time.sleep(2)
    try:
        res11 = driver.find_element(By.ID, 'r1-11').text
        res11 = res11.replace(' › ', '/')
    except NoSuchElementException:
        res11 = "None"
    time.sleep(2)
    try:
        res12 = driver.find_element(By.ID, 'r1-12').text
        res12 = res12.replace(' › ', '/')
    except NoSuchElementException:
        res12 = "None"
    time.sleep(2)
    try:
        res13 = driver.find_element(By.ID, 'r1-13').text
        res13 = res13.replace(' › ', '/')
    except NoSuchElementException:
        res13 = "None"
    try:
        res14 = driver.find_element(By.ID, 'r1-14').text
        res14 = res14.replace(' › ', '/')
    except NoSuchElementException:
        res14 = "None"
    time.sleep(2)
    try:
        res15 = driver.find_element(By.ID, 'r1-15').text
        res15 = res15.replace(' › ', '/')
    except NoSuchElementException:
        res15 = "None"
    time.sleep(2)
    try:
        res16 = driver.find_element(By.ID, 'r1-16').text
        res16 = res16.replace(' › ', '/')
    except NoSuchElementException:
        res16 = "None"
    time.sleep(2)
    try:
        res17 = driver.find_element(By.ID, 'r1-17').text
        res17 = res17.replace(' › ', '/')
    except NoSuchElementException:
        res17 = "None"
    time.sleep(2)
    try:
        res18 = driver.find_element(By.ID, 'r1-18').text
        res18 = res18.replace(' › ', '/')
    except NoSuchElementException:
        res18 = "None"
    time.sleep(2)
    try:
        res19 = driver.find_element(By.ID, 'r1-19').text
        res19 = res19.replace(' › ', '/')
    except NoSuchElementException:
        res19 = "None"
    time.sleep(2)
    try:
        res20 = driver.find_element(By.ID, 'r1-20').text
        res20 = res20.replace(' › ', '/')
    except NoSuchElementException:
        res20 = "None"
    time.sleep(2)
    res_files = driver.find_elements(By.ID, 'links')
    
    name_fin = name.replace(' ', '-')
    
    for i in name_fin:
        if i in alphabet:
            name_fin = slugify(name)

    for i in range(len(res_files)):
        data_file = []
        res_files[i] = res_files[i].text
        res_files[i] = res_files[i].replace(' › ', '/')
        res_files[i] = res_files[i].replace('\n', ' <br><br>')
        data_file.append(f'{res_files[i]}')        
        full_list = " ".join(data_file)
        
        button = '<button onclick="myFunc()">Return and search</button><br> <script>function myFunc() {window.location.href = "http://127.0.0.1:8000";}</script>'
        
        with open(f"ysearch/search/{name_fin}.html", "a",  encoding='utf-8') as name:
            
            name.write(f'<html>\n<head>\n<title> \n{name}\n \
           </title>\n</head>  <body> <h1><font color = #FFFFFF>Welcome to</font> \
           <font color = #00b300>our Search. Return and search"</font></h1>\n \
            <body bgcolor = "#1d102f">\n \
            {button}\n \
           <h2>A CS Portal for Everyone</h2><font color = #FFFFFF>{full_list}</font> \
           </body></html>')
            
    data = {
    'res1' :res1,
    'res2' :res2,
    'res3' :res3,
    'res4' :res4,
    'res5' :res5,
    'res6' :res6,
    'res7' :res7,
    'res8' :res8,
    'res9' :res9,
    'res10' :res10,
    'res11' :res11,
    'res12' :res12,
    'res13' :res13,
    'res14' :res14,
    'res15' :res15,
    'res16' :res16,
    'res17' :res17,
    'res18' :res18,
    'res19' :res19,
    'res20' :res20,

     }
    
    return render(request, 'ducksearch.html', context=data)
    driver.quit()



# for i in range(len(res)):
#         reqres = []
#         req = res[i].text
#         reqres.append(req)
#         print(reqres)

