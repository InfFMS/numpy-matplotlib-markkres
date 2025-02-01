# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import numpy as np
import matplotlib.pyplot as plt

mas=np.random.randint(1,7,size=(1000,))
#print(mas)
numbers,col=np.unique(mas, return_counts=True)
print("вероятность выпадения чисел от 1 до 6: ",end='')
for i in range(6):
    print(col[i]/1000,end=" ")
print()
maximum=1
cur=1
for i in range(999):
    if mas[i]==mas[i+1]:
        cur+=1
    else:
        maximum=max(maximum,cur)
        cur=1
print(maximum)
plt.bar(numbers,col,color="blue")
plt.title("количество выпадений")
plt.show()
