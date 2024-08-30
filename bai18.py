# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:15:04 2024

@author: Kim Quyên
"""

a=input("Nhập giờ thứ nhất(hh1:mm1:ss1): ")
b=input("Nhập giờ thứ (hh2:mm2:ss2): ")
hh1, mm1, ss1 = map(int, a.split(':'))
hh2, mm2, ss2 = map(int, b.split(':'))
print("Tổng hai giờ là:", hh1+hh2, ":", mm1+mm2, ":", ss1+ss2)
print("Hiệu hai giờ là:", hh1-hh2, ":", mm1-mm2, ":", ss1-ss2)
