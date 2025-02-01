# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import numpy as np
import matplotlib.pyplot as plt
mas=np.random.randint(-10,35,size=365)
print(mas.mean())
maximum=0
cur=0
for i in mas:
    if i>0:
        cur+=1
    else:
        maximum=max(cur,maximum)
        cur=0
print(maximum)
unique,counts=np.unique(mas,return_counts=True)
plt.subplot(1,2,1)
plt.bar(unique,counts)
x=[i for i in range(1,366)]
plt.subplot(1,2,2)
plt.plot(x,mas)
plt.show()
