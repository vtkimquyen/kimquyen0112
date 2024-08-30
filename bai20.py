# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:35:21 2024

@author: Kim Quyên
"""

a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))

so_lon_nhat=a

if b>a:
    b=so_lon_nhat
if c>b:
    c=so_lon_nhat

    
print("Số lớn nhất là:", so_lon_nhat)