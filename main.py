import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


SEED = 17
COUNT = 1000
LEFT_BORDER = -10000
RIGHT_BORDER = 10000

np.random.seed(SEED)

source_values = np.random.randint(LEFT_BORDER, RIGHT_BORDER + 1, COUNT)
data = pd.Series(source_values, name="value")

minimum = data.min()
maximum = data.max()
total_sum = data.sum()

average = data.mean()
dispersion = ((data - average) ** 2).mean()
standard_deviation = math.sqrt(dispersion)

value_counts = data.value_counts()
repeated_values_count = value_counts[value_counts > 1].sum()

print("SimpleAnalysis")
print("Количество чисел:", COUNT)
print("Диапазон значений:", LEFT_BORDER, "до", RIGHT_BORDER)
print()

print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)
print("Сумма всех чисел:", total_sum)
print("Количество повторяющихся значений:", repeated_values_count)
print("Среднеквадратическое отклонение:", round(standard_deviation, 2))

plt.figure(figsize=(11, 5))
plt.plot(data.index, data.values)
plt.title("Линейный график исходного набора данных")
plt.xlabel("Порядковый номер")
plt.ylabel("Значение")
plt.grid(True)
plt.show()

rounded_to_hundreds = (data / 100).round() * 100

plt.figure(figsize=(11, 5))
plt.hist(rounded_to_hundreds, bins=35, edgecolor="black")
plt.title("Гистограмма значений после округления до сотен")
plt.xlabel("Округлённое значение")
plt.ylabel("Частота")
plt.grid(True)
plt.show()

ascending_values = data.sort_values().reset_index(drop=True)
descending_values = data.sort_values(ascending=False).reset_index(drop=True)

table = pd.DataFrame()
table["Исходный ряд"] = data
table["По возрастанию"] = ascending_values
table["По убыванию"] = descending_values

print()
print("Фрагмент DataFrame:")
print(table.head(15))

plt.figure(figsize=(11, 5))
plt.plot(table.index, table["По возрастанию"], label="Сортировка по возрастанию")
plt.plot(table.index, table["По убыванию"], label="Сортировка по убыванию")
plt.title("Графики отсортированных значений")
plt.xlabel("Порядковый номер")
plt.ylabel("Значение")
plt.legend()
plt.grid(True)
plt.show()