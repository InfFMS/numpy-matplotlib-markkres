# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import matplotlib.pyplot as plt

def ATTACK(x,y):
    if 0<=x<8 and 0<=y<8:
        ax.add_patch(plt.Circle((x,y),0.2,color="orange", alpha=1))

chess=[[0 for _ in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        if (i%2+j%2)%2==0:
            chess[i][j]=1
            
x,y=map(int,input("координаты ферзя: ").split())
x,y=x-1,y-1

_,ax=plt.subplots()

plt.imshow(chess, cmap="binary")
rect=plt.Circle((x,y),0.4,color="green",alpha=1)
ax.add_patch(rect)

ax.invert_yaxis()
bukvbl=["A","B","C","D","E","F","G","H"]
xlabels = [bukvbl[x] for x in range(0,8)]
ax.set_xticks(list(range(8)), labels=xlabels)
ylabels = [f'{y}' for y in range(1,9)]
ax.set_yticks(list(range(8)), labels=ylabels)

#for i in range(8):
#    if i!=x:
#        circle=plt.Circle((i,y),0.2,color="orange",alpha=1)
#        ax.add_patch(circle)
#    if i!=y:
#        circle=plt.Circle((x,i),0.2,color="orange",alpha=1)
#        ax.add_patch(circle)
for i in range(8):
    if i!=x:
        ATTACK(i,y)
    if i!=y:
        ATTACK(x,i)
for i in range(1,8):
    ATTACK(x+i,y+i)
    ATTACK(x-i,y+i)
    ATTACK(x+i,y-i)
    ATTACK(x-i,y-i)
plt.show()

