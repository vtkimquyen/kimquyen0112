# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:23:47 2024

@author: Kim Quyên
"""

a=int(input("Số nguyên a: "))
b=int(input("Số nguyên b: "))
c=int(input("Số nguyên c: "))
d=int(input("Số nguyên d: "))
so_nho_nhat=a
if b<a:
    b=so_nho_nhat
    
if c<b:
    c=so_nho_nhat
    
if d<c:
    d=so_nho_nhat
    
print("Số nhỏ nhất là: ", so_nho_nhat)