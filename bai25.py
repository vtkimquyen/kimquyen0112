# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:28:36 2024

@author: Kim Quyên
"""

ky_tu=input("Nhập một chữ cái: ")
if ky_tu.islower():
    print("Đổi thành chữ hoa:", ky_tu.upper())
else:
    print("Đổi thành chữ thường:", ky_tu.lower())