# Обьединение файлов с одинакым названием

import os
import glob

folder1 = os.listdir(r"C:\Users\Chris\Desktop\Verified_1")
folder2 = os.listdir(r"C:\Users\Chris\Desktop\Verified_2")
folder3 = os.listdir(r"C:\Users\Chris\Desktop\Verified_3")
verified1 = []
verified1.extend(glob.glob(r"C:\Users\Chris\Desktop\Verified_1\***.txt"))

verified2 = []
verified2.extend(glob.glob(r"C:\Users\Chris\Desktop\Verified_2\***.txt"))

verified3 = []
verified2.extend(glob.glob(r"C:\Users\Chris\Desktop\Verified_3\***.txt"))
for i in folder1:
    for j in folder2:
        for k in folder3:
            if i == j == k:
                try:
                    with open(r"C:\Users\Chris\Desktop\Verified_1\\" + i) as f1:
                        data1 = f1.read()
                        with open(r"C:\Users\Chris\Desktop\Verified_2\\" + j) as f2:
                            data2 = f2.read()
                            with open(r"C:\Users\Chris\Desktop\Verified_3\\" + j) as f3:
                                data3 = f3.read()
                                with open('C:\\Users\\Chris\\Desktop\\Verified\\{}'.format(i), "a") as fd:
                                    fd.write(data1 + data2 + data3)
                except UnicodeDecodeError:    
                    pass
        