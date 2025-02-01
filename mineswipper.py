# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
import random
import matplotlib.pyplot as plt
count=0
mas=[[0 for _ in range(10)] for _ in range(10)]
while count!=15:
    a,b=random.randint(0,9),random.randint(0,9)
    if mas[a][b]!=-1:
        mas[a][b]=-1
        count+=1
mas2=[[0 for _ in range(10)] for _ in range(10)]      
for i in range(10):
    for j in range(10):
        if mas[i][j]!=-1:
            if i==0 and j==0:
                mas2[i][j]=abs(mas[0][1]+mas[1][1]+mas[1][0])
            elif i==0 and j==9:
                mas2[i][j]=abs(mas[0][8]+mas[1][8]+mas[1][9])
            elif i==9 and j==0:
                mas2[i][j]=abs(mas[8][0]+mas[8][1]+mas[9][1])
            elif i==9 and j==9:
                mas2[i][j]=abs(mas[9][8]+mas[8][8]+mas[8][9])
            elif i==0 and j!=0 and j!=9:
                mas2[i][j]=abs(mas[0][j-1]+mas[0][j+1]+mas[1][j-1]+mas[1][j+1]+mas[1][j])
            elif i==9 and j!=0 and j!=9:
                mas2[i][j]=abs(mas[9][j-1]+mas[9][j+1]+mas[8][j-1]+mas[8][j+1]+mas[8][j])
            elif j==0 and i!=0 and i!=9:
                mas2[i][j]=abs(mas[i-1][0]+mas[i+1][0]+mas[i-1][1]+mas[i+1][1]+mas[i][1])
            elif j==9 and i!=0 and i!=9:
                mas2[i][j]=abs(mas[i-1][9]+mas[i+1][9]+mas[i-1][8]+mas[i+1][8]+mas[i][8])
            else:
                mas2[i][j]=abs(mas[i][j+1]+mas[i][j-1]+mas[i-1][j]+mas[i+1][j]+mas[i-1][j-1]+mas[i+1][j-1]+mas[i-1][j+1]+mas[i+1][j+1])
for i in range(10):
    for j in range(10):
        mas2[i][j]=mas2[i][j]+mas[i][j]
        plt.text(j,i,mas2[i][j])
print(mas2[1][1])
plt.imshow(mas2, cmap="gist_stern")
plt.show()
