# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:29:19 2024

@author: Kim Quyên
"""

so_xe=int(input("Nhập số xe gồm 4 số: "))
ngan = so_xe // 1000
tram = so_xe //100 % 10
chuc = so_xe // 10 % 10
donvi = so_xe % 10
so_nut = ngan + tram + chuc + donvi
a = so_nut // 10
b = so_nut % 10
c = a + b
x = c // 10
y = c % 10
print("Biển số xe của bạn là:", x+y, "nút.")
