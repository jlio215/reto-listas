lista_1= input()
lista_2= input()
lista_3= input()
a=0
b=0
c=str()
k=len(lista_3)
h=len(lista_1)
for j in range(0, k):
    for i in range(0, h):
        if lista_1[i]==lista_3[j]:
            a +=1
        if lista_2[i]==lista_3[j]:
            b +=1
    if a>b:
        c +="1"
    elif a==b:
        c +="*"
    else:
        c +="2"

print(c)

#QCWKFI

#LGECUO

#KATOAETFQUAPMVKLGMT