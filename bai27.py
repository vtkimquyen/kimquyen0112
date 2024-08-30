# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:47:28 2024

@author: Kim Quyên
"""

hinh = input("Nhập loại hình (v, n, t): ")
if hinh ==  'v':
    canh=float(input("Nhập độ dài cạnh hình vuông: "))
    dien_tich_v= canh*canh
    chu_vi_v=4*canh
    print("Diện tích:", dien_tich_v)
    print("Chu vi:", chu_vi_v)
    
elif hinh == 'n':
    chieu_dai=float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong=float(input("Nhập chiều rộng hình chữ nhật: "))
    dien_tich_n= chieu_dai * chieu_rong
    chu_vi_n= 2*(chieu_dai + chieu_dai)
    print("Diện tích:", dien_tich_n)
    print("Chu vi:", chu_vi_n)
elif hinh == 't':
    ban_kinh=float(input("Nhập bán kính hình tròn: "))
    dien_tich_t= 3.14 * (ban_kinh**2)
    chu_vi_t= 2 * 3.14 * ban_kinh
    print("Diện tích:", dien_tich_t)
    print("Chu vi:", chu_vi_t)
else:
    print("Hình không hợp lệ")
    