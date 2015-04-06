import csv
import random

lista = []
listausers=[]
listalocations=[]

lf = open('foursquare_checkins.csv')
listafoursq = csv.reader(lf)

for line in listafoursq:
    lista.append(line)
    listausers.append(line[0])
    listalocations.append(line[4])
    
lista=lista[1::]
listausers=listausers[1::]
listalocations=listalocations[1::]

lista_unica_users=set(listausers)
lista_unica_locations=set(listalocations)

qusers=len(lista_unica_users)
qubicaciones=len(lista_unica_locations)
qcheckins=len(lista)

promedio_u_c=len(lista)/qusers
promedio_l_c=len(lista)/qubicaciones

listfriends=[]
listaaux=[]
la = open('foursquare_friendship.csv')
listaamigos = csv.reader(la)

for line in listaamigos:
    listaaux.append(line)
    for x in line:
        listfriends.append(x)

listfriends=listfriends[2::]
listaaux=listaaux[1::]
listfriends=set(listfriends)

Dic={}
for user in listfriends:
    Dic[user]=[]

for line in listaaux:
    
    x = line[0]
    y = line[1]
    if x not in Dic[y]:
        Dic[y].append(x)
    if y not in Dic[x]:
        Dic[x].append(y)

cantamigos=[]
for user in listfriends:
    z=len(Dic[user])
    cantamigos.append(z)

promamigos=sum(cantamigos)/qusers

lm=open('muestra_usuarios.csv','w')
archivo_muestra=csv.writer(lm)
archivo_muestra.writerow(['user','latitude','longitude','time','location'])

muestra=[]
listamuestra=[]
for i in range(0,500):
    x=random.randint(0,2290997)
    if x not in muestra:
        muestra.append(x)
        listamuestra.append(lista[x])
        archivo_muestra.writerow(lista[x])
lm.close()
lf.close()
lm.close()
            
print("Número de usuarios del dataset: "+str(qusers))
print("Número de ubicaciones del dataset: "+str(qubicaciones))
print("Número de check-ins: "+str(qcheckins))
print("Promedio de amigos por usuario: "+str(promamigos)) 
print("Promedio de check-ins por usuario: "+str(promedio_u_c))
print("Promedio de check-ins por lugar: "+str(promedio_l_c))


