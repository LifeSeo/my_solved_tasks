import pandas as pd
from main_menu import MenuMain
from tabulate import tabulate

def pupils_table(main_menu_choise):
    if main_menu_choise == 5:
        df = pd.read_csv(r"Control_System_Pupils_at_the_School\table_pupils.csv")
    print(tabulate(df, showindex=False, headers=df.columns))