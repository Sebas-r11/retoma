import matplotlib.pyplot as plt
import numpy as np
import os #llamar comandos de windows como cls

xpoints = np.array([0, 6])
ypoints = np.array ([0, 500])

plt.plot(xpoints, ypoints)
plt.show()

plt.plot(xpoints, ypoints, "o:r") #0 crea puntos :linea punteada r linea punteada
plt.show()

#no necesitamos puntos x

ypoints = np.array ([3,500,100,300,50])

plt.plot(ypoints)
#plt.plot(ypoints, maker="o")
#plt.plot(ypoints, maker="o", ms=20) #ms=markersize
#plt.plot(ypoints, maker="o", ms=20, mec='r') #mec = color 

plt.show()

#leyendas
plt.plot(ypoints, marker= "o", ms=20, mec='r')

plt.title("titulo del grafico")
plt.xlabel("leyenda eje X")
plt.ylabel("leyenda eje Y")

plt.show()

#cambiar propiedades de fuentes del grafico

diccFuenteTitulo = {'family':'serif','color':'blue','size':20}
diccFuenteEjes = {'family':'serif','color':'darkred','size':15}

#aplicar cambios

plt.plot(ypoints, marker= "o", ms=20, mec='r')

plt.title("titulo del grafico", fontdict=diccFuenteTitulo)
plt.xlabel("leyenda eje X", fontdict=diccFuenteEjes)
plt.ylabel("leyenda eje Y", fontdict=diccFuenteEjes)

plt.show()

# dibujar cuadriculas
plt.plot(ypoints, marker= "o", ms=20, mec='r')
plt.grid(color = 'red', linestyle = '--', linewidth =0.1)

plt.show()

#graficos de barras

x = np.array(["dato1","dato2","dato3","dato4"])
y = np.array([3, 8, 1, 10])

os.system("cls") #clear

#plt.bar(x,y)#vertical

#plt.barh(x,y)#horizontal
plt.bar(x,y, color="green", width=0.5) #color y grosor

plt.show()

