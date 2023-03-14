# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:07:10 2023

@author: Belén
"""


# archivo = open("archivo.txt")
# contenido = archivo.read()
# print(contenido)
# archivo.close()

#%%
# with open("archivo.txt") as arch:
#     contenido = arch.readline()
#     print(contenido)
#     contenido = arch.readline()
#     print(contenido)

# print("Mensaje adicional")

#%%

# with open("archivo.txt") as arch:
#     for linea in arch:
#         print(linea,end="")

#%%

# with open("archivo.txt") as arch:
#     l_arch = list(arch)

# print(l_arch)     

#%%

# with open("archivo.txt") as arch:
#     l_arch = arch.readlines()

# print(l_arch)


# #%%
# mode 'w' y 'a' si no existe el archivo, lo crea

# with open("archivo_nuevo.txt", mode='w') as arch:
#     n = arch.write("Este es un archivo nuevo.\nArchivo de prueba.")
# print(n)

# #%% 

# with open("archivo_nuevo.txt", mode='a') as arch:
#     n = arch.write("\nAgrego una línea.")
# print(n)

   
# #%%

# with open("archivo_nuevo.txt", mode='r+') as arch:
#     arch.read()
#     n=arch.write("\nAgrego contenido al final del archivo.")
# print(n)       
        
# #%%

# with open("archivo_nuevo.txt") as arch:
#     for nro_linea, linea in enumerate(arch):
#         print(f" {nro_linea}: {linea.strip()}")