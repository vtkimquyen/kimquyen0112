# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:00:17 2024

@author: Kim Quyên
"""

gio=int(input("Nhập số giờ: "))
phut=int(input("Nhập số phút: "))
giay=int(input("Nhập số giây: "))

if 0<=gio<=23 and 0<=phut<=59 and 0<=giay<=59:
    print("Thời gian: ", gio, ":", phut, ":", giay)
else:
    print("Không hợp lệ")