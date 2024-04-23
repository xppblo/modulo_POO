"""
FUNCION OPEN
Open(ruta, argumento o modo de apertura)
"""

import os

try:
    log_file = open(os.path.abspath("Dia11/logs/error.log"))
    print(log_file)
except FileNotFoundError as fnfe:
    print("Archivo o directorio no encontrado")
    print(fnfe)
    
#ARGUMENTO r Solo lectura
log_file2 = open(os.path.abspath("Dia11/html/index.html"),"r")
print(log_file2.read())
log_file2.close()
print("***********READLINE***************\n")
log_file3 = open(os.path.abspath("Dia11/html/index.html"),"r")
print(log_file3.readline())#trabaja con un for para leer linea por linea
log_file3.close()
print("***********READLINES***************\n")
log_file4 = open(os.path.abspath("Dia11/html/index.html"),"r")
print(log_file4.readlines())#retorna una lista de cada una de las lineas
log_file4.close()
print("***********WITH***************\n")
with open(os.path.abspath("Dia11/html/index.html"),"r") as archivo:
    #print(archivo) <_io.TextIOWrapper name='D:\\CursoPython\\0044-1\\Modulo_POO\\Dia11\\html\\index.html' mode='r' encoding='cp1252'> 
    for linea in archivo:
        print(linea.strip())
        
#ARGUMENTO w Solo escritura
#la ruta donde se creara el archivo debe existir
log_file5 = open(os.path.abspath("Dia11/html/assets/css/style.css"),"w")
log_file5.write("/*esto es un comentario*/\n") #escribe en el archivo indicado, pero siempre escribe continuadamente
log_file5.write("*{ margin: 0px }\n")
log_file5.close()

import time
try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open(f"dia11/logs/{round(time.time())}.log", "w") as log:
        log.write(f"ERROR: {e}")