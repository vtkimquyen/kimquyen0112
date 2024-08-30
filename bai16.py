# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:58:49 2024

@author: Kim Quyên
"""

thoigian=input("Nhập vào thời gian ..h ..p..s: ")
so= ""
for i in thoigian:
    if i.isalpha():
        so += ":"
    else:
        so += i
so_cuoi = so[:-1]
hh, mm, ss = map(int, so_cuoi.split (':'))
print(thoigian,"khi đổi ra giây bằng = ", hh*3600 + mm*60 + ss, "giây")