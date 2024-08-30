# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:20:38 2024

@author: Kim Quyên
"""

can_nang=float(input("Nhập cân nặng(kg): "))
chieu_cao=float(input("Nhập chiều cao(m): "))
bmi = can_nang / (chieu_cao ** 2)
print("Chỉ số BMI  của bạn là:", bmi)