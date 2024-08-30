# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:42:06 2024

@author: Kim Quyên
"""

N = int(input("Nhập số nguyên dương N có 2 chữ số: "))

if N < 10 or N > 99:
    print("N phải là số nguyên dương có 2 chữ số!")
else:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    tong = hang_chuc + hang_don_vi
    
    print(f"Tổng các chữ số của {N} là: {hang_chuc} + {hang_don_vi} = {tong}")