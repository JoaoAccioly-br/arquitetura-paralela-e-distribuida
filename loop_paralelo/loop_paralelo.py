# OpenMp
# 200 pontos = mesmo código só que em troca de mensagens (padrão mpi) (escrito para o prof)

from threading import Thread

a = [10, 20, 30, 40, 50, 60]
n = len(a)
center = n // 2
sum = [0, 0]

def left():
    for i in range(0,center):
        sum[0] = sum[0] + a[i]

def right():
    for i in range(center,n):
            sum[1] = sum[1] + a[i]

t1 = Thread(target=left)
t2 = Thread(target=right)

threads = [t1, t2]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(sum)
print(sum[0] + sum[1])