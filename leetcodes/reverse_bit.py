# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 13:44:16 2021

@author: zhous
"""
def reverseBits(self, n):
    res = 0
    for _ in range(32):
        res = (res<<1) + (n&1)
        n>>=1
    return res