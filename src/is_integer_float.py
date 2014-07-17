#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

In Python how to check if a float is an integer?

En Python, ¿Cómo verificar si un float es un numero entero?
'''

#create a float number
f = 46.98
print(f)

#this method verify if the float instance is finite with integral value.
#Return True or False.
print(f.is_integer())

#create a float number
f = 46.
print(f)

#return True because the decimal part is 0
print(f.is_integer())
