n = int(input("numeros a promediar:"))
suma=0
i=1
while (i <= n):
	print("ingrese numero",i)
	nota = float(input())
	suma=suma+nota
	i+=1
prom = suma / n 
print("El promedio:",prom)
print ("mensaje nuevo")
	
