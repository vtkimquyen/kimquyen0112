# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:43:32 2024

@author: Kim Quyên
"""

from datetime import datetime
nam = int(input("Nhập vào năm sinh: "))
hientai = datetime.now().year
tuoi = hientai - nam
print(f"Bạn sinh năm {nam} vậy bạn {tuoi} tuổi")