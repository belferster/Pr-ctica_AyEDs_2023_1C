# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:41:00 2023

@author: Belén
"""

from modulos import Cuadrado

if __name__ == '__main__':


    salir = False
    
    while not salir:
        
      try:
            lado = float(input("Por favor ingrese el valor del lado: "))
            
            if lado > 0:
                cuadrado1 = Cuadrado(lado)
                salir = True
        
            else:
                print("Atencion! debe ingresar un valor positivo")
                
      except ValueError:
            
            print("Debe ingresar un valor numérico")
           
    area = cuadrado1.calcular_area()
    perimetro = cuadrado1.calcular_perimetro()
    print(f"El área del cuadrado es {area} y su perímetro {perimetro}")
        

    
    
