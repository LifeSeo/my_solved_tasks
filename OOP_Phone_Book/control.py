from data import input_data
from data import print_data
from put_in_file import put_file
 

def finall_button():
    a = input_data()
    res = put_file(a)
    print_data(res)
    