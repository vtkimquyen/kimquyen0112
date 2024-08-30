# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:43:19 2024

@author: Kim Quyên
"""

so = ["Khong", "Mot", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chín"]

a=int(input("Nhập 1 số 0-9: "))

if 0<=a<=9:
    print(so[a])
else:
    print("Khong doc duoc")