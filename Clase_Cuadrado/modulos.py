# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:40:46 2023

@author: Belén
"""

    
class Cuadrado:
    
    """ clase que modela un cuadrado mediante su atributo lado, posee métodos para 
        modificar/obtener el lado y para calcular y devolver su perímetro y su área.
        ----------------
        atributos:
        lado --> float. 
        valor entero que representa el lado del cuadrado 
    """

    def __init__(self, valor):
        
        """ método inicializador que se ejecuta al crear una instancia de la clase
            recibe como parámetro el valor del lado del cuadrado 
        """
        
        self.lado = valor
        
    @property    
    def lado(self):
        
        """ método que devuelve el valor actual del lado """
        
        return self._lado
        
    @lado.setter
    def lado(self, valor):
        
        """ método que permite modificar el valor del lado """
        
        if valor > 0 and type(valor)!=str:
            
            self._lado = valor    
            
        else:
            print("Debe ingresar un valor positivo")
            
    # @lado.deleter
    # def lado(self):
    #     del self._lado
        
    
    def calcular_area(self):
        
        """ método que calcula el area del cuadrado y devuelve su valor """
        
        self.area = self.lado ** 2
        return self.area
    
    def calcular_perimetro(self):
        
        """ método que calcula el perimetro del cuadrado y devuelve su valor """
        
        self.perimetro = self.lado * 4
        return self.perimetro
        
  

        
    
        
        
        