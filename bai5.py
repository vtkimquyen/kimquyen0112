# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:42:41 2024

@author: Kim Quyên
"""

thoi_gian = input("Nhập giờ, phút, giây theo định dạng hh:mm:ss : ")
hh, mm, ss = map(int, thoi_gian.split(':'))
tong_giay = hh * 3600 + mm * 60 + ss
print("Tống số giây là:", tong_giay)