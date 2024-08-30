# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:08:33 2024

@author: Kim Quyên
"""

ngay=int(input("Nhập ngày: "))
thang=int(input("Nhập tháng: "))
nam=int(input("Nhập năm: "))
a = f"{ngay}/{thang}/{nam}"
print("Ngày/tháng/năm:", a)
b = f"{ngay}/{thang}/{str(nam)[-2:]}"
print("Ngày/tháng/năm:", b)
c = f"{nam}/{thang}/{ngay}"
print("Năm/tháng/ngày:", c)
