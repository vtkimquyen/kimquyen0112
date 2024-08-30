# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:37:05 2024

@author: Kim Quyên
"""

a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))

if a>b:
    a, b = b, a
if a>c:
    a,c = c, a
if b>c:
    b, c = c, b

print("Thứ tự tăng dần:", a, b, c)
N = input("Nhập vào 1 số nguyên N: ")
ds = list(N)
sap_xep = sorted(ds)
hop = "".join(sap_xep)
print(hop)

    