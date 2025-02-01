# Описание задачи:
# Робот начинает своё движение из точки (0,0) на координатной плоскости. Его маршрут задаётся массивом из 100 случайных значений, где:1 — движение вверх.2 — движение вниз.3 — движение вправо.4 — движение влево.
# Ваша задача:
# Сымитировать маршрут робота, используя случайные числа.
# Найти конечное положение робота.
# Построить путь робота на графике (соединяя все пройденные точки).
# Подсчитать, сколько шагов робот сделал в каждую сторону.
# Определить расстояние от начальной точки до конечной.
import numpy as np
import matplotlib.pyplot as plt
mas=np.random.randint(1,5,size=100)
unique,count=np.unique(mas,return_counts=True)
print("верх: ",count[0])
print("вниз: ",count[1])
print("вправо: ",count[2])
print("влево: ",count[3])
x=count[0]-count[1]
y=count[2]-count[3]
print("(",x,",",y,")")
print(np.sqrt(x**2+y**2))
x=[0]
y=[0]
for i in mas:
    if i==1:
        x.append(x[-1])
        y.append(y[-1]+1)
    elif i==2:
        x.append(x[-1])
        y.append(y[-1]-1)
    elif i==3:
        x.append(x[-1]+1)
        y.append(y[-1])
    elif i==4:
        x.append(x[-1]-1)
        y.append(y[-1])
plt.plot(x,y)
plt.show()
