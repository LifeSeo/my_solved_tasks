import pandas as pd
import seaborn as sb
import matplotlib.pyplot as pl
from seaborn import relplot
from seaborn import histplot
from seaborn import PairGrid

# df = pd.read_csv(r'C:\Users\Chris\Desktop\california_housing_train.csv')
# print(df.head())
# maps = sb.scatterplot(data=df, x="longitude", y="latitude")
# pl.show()

# # Изобразите отношение households к population с
# # помощью точечного графика

# maps = sb.scatterplot(data=df, x="households", y="population")
# pl.show()

# # Визуализировать longitude по отношения к
# # median_house_value, используя линейный график

# maps = relplot(x="longitude", y="medianHouseValue", kind="line", data=df)
# pl.show()

# Представить гистограмму по housing_median_age

# maps = histplot(data = df, x = "housingMedianAge")
# pl.show()

# Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

# maps = histplot(data = df, x = "medianHouseValue", hue="housingMedianAge")
# pl.show()

# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы

penguins = sb.load_dataset("penguins")
print(penguins.head())

sb.scatterplot(x="species", y="island",data=penguins)
sb.scatterplot(x="species", y="island",data=penguins, size=41)
sb.scatterplot(x="species", y="island", hue="body_mass_g", data=penguins)

# all_colums = ["species","island","bill_length_mm","bill_depth_mm",
#               "flipper_length_mm","body_mass_g","sex"]

# temp = sb.PairGrid(penguins[all_colums])
# temp.map(sb.scatterplot)

# pl.show()

# Создать новый столбец в таблице с
# пингвинами, который будет отвечать за
# показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

penguins.loc[penguins["bill_length_mm"] <= 35, "beak"] = "Small"
penguins.loc[(penguins["bill_length_mm"] > 35) & (penguins["bill_length_mm"] < 42), "beak"] = "Medium"
penguins.loc[penguins["bill_length_mm"] >= 42, "beak"] = "Big"

print(penguins.columns)

print(penguins.head(29))

# Изобразить гистограмму по flipper_length_mm
# с оттенком height_group. Сделать анализ


histplot(data=penguins, x ="flipper_length_mm", hue="body_mass_g")
pl.show()
