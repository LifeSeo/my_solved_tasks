# Евгению предоставили строку, состоящую из русских букв разных регистров
# и попросили очистить ее от заглавных литер.
 
string = "ВАаапавУККутлопоранроЦККеирмвкУа"
string_replace = ""

for el in string:
    if not el.isupper():
        string_replace += el
print(string_replace)
    
    
