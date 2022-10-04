mascota=["perro", "gato", "pez", "ave", "avestruz", "dinosaurio"];
print(mascota);
a=int(1); b=int(1);
num=int()
string=();
rta=input(print("agregar yes O no"));
while(rta=="yes"):
    if(len(mascota)<10):
        objeto=input("ingrese una mascota ")
        mascota.append(objeto);
        print("agregar mas mascotas yes o no");
        rta=input();
    else:
        print("suficientes mascotas por hoy, no se agregaran mas boludo")
        rta="no";
print(" le gustaria suprimir alguna mascota fea de la lista, yes o no");
rta=input();

while(rta=="yes"):
    if(len(mascota)>1):
        objeto=input("que mascota quiere quitarse de encima")
        mascota.remove(objeto);
        print("algun otro animal feo para quitarse? yes o no")
        rta=input();
    else:
        print(" no tenemos mas mascotas, no hay nada para quitar");
        rta=="no";
print("se te perdio un animal?, quieres buscarlo?, yes o no");
rta=input();

while(rta=="s"):
    objeto=input(" otra mascota a encontrar?")
    num=mascota.index(objeto);
    print(mascota[num+1]);
    print(mascota[num-1]);

    print(" algun otro a encontrar? yes o no")
    rta=input();

print(" hora de horientar a las mascotas, quiere ordenarlas? yes o no")
rta=input();

if (rta=="yes"):
    for a in range (1, len(mascota)+1):
        for b in range(1, len(mascota)):
            if(mascota[b-1]>mascota[b]):
                string=mascota[b-1];
                mascota[b-1]-mascota[b];
                mascota[b]=string;

print(mascota);