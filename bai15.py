# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:50:23 2024

@author: Kim Quyên
"""
import math

a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))

a1=a**1/3
b1=b**1/3
ab=(a*b)**1/3
print("Giá trị biểu thức= ", ((((a+b)/(a1+b1))-(ab))/((a1-b1)**2)))
