# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:52:51 2024

@author: Kim Quyên
"""

a=float(input("Nhập hệ số a: "))
b=float(input("Nhập hệ số b: "))

if a==0:
    if b==0:
        print("Vì a=0, b=0 thì phương trình đúng với mọi giá trị của x")
        print("Phương trình có vô số nghiệm")
    else:
        print("Vì a=0, b={b}!=0 nên phương trình trở thành {b}=0")
        print("Đây là 1 đẳng thức vô lý")
        print("Phương trình vô nghiệm")
else:
    x=-b/a
    print("Vì a={a}!=0, Phương trình có nghiệm duy nhất", x)