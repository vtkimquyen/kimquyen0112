# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:12:11 2024

@author: Kim Quyên
"""

a=float(input("Nhập hệ số a: "))
b=float(input("Nhập hệ số b: "))
c=float(input("Nhập hệ số c: "))
delta=b*b - 4*a*c
if a!=0 and delta<0:
    print("Biện luận:")
    print("Vì delta<0, phương trình vô nghiệm")
elif a!=0 and delta==0:
    print("Biện luận:")
    print("Vì delta=0, phương trình có nghiệm kép x1=x2= ",-b/2*a)
elif a!=0 and delta>0:
    print("Biện luận:")
    print("Vì delta>0, phương trình có 2 nghiệm phân biệt:")
    print("x1= ", (-b + math.sqrt(delta))/2*a)
    print("x2= ", (-b - math.sqrt(delta))/2*a)
else:
    print("Không xác định")
    