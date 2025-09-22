#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""古典密码：凯撒 / 维吉尼亚 / 摩斯"""
import string
from typing import List, Tuple

# ---------- Classical ----------
class ClassicalSuite:
    alpha = string.ascii_uppercase
    
    @staticmethod
    def caesar_enc(pt: str, shift: int) -> str:
        return ''.join(ClassicalSuite.alpha[(ClassicalSuite.alpha.index(c)+shift)%26] if c in ClassicalSuite.alpha else c
                       for c in pt.upper())
    
    @staticmethod
    def caesar_dec(ct: str, shift: int) -> str:
        return ClassicalSuite.caesar_enc(ct, -shift)
    
    @staticmethod
    def caesar_brute(ct: str) -> List[Tuple[int,str]]:
        return [(i, ClassicalSuite.caesar_dec(ct, i)) for i in range(26)]
    
    @staticmethod
    def vigenere_enc(pt: str, key: str) -> str:
        pt, key = pt.upper(), key.upper()
        i = 0; out = ""
        for ch in pt:
            if ch in ClassicalSuite.alpha:
                out += ClassicalSuite.alpha[(ClassicalSuite.alpha.index(ch) + ClassicalSuite.alpha.index(key[i%len(key)]))%26]
                i+=1
            else: out+=ch
        return out
    
    @staticmethod
    def vigenere_dec(ct: str, key: str) -> str:
        ct, key = ct.upper(), key.upper()
        i = 0; out = ""
        for ch in ct:
            if ch in ClassicalSuite.alpha:
                out += ClassicalSuite.alpha[(ClassicalSuite.alpha.index(ch) - ClassicalSuite.alpha.index(key[i%len(key)]))%26]
                i+=1
            else: out+=ch
        return out
    
    @staticmethod
    def morse_enc(pt: str) -> str:
        MORSE = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}
        return ' '.join(MORSE.get(c.upper(), c) for c in pt)
    
    @staticmethod
    def morse_dec(ct: str) -> str:
        INV = {v:k for k,v in {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}.items()}
        return ''.join(INV.get(c, c) for c in ct.split())

# 为保持与现有代码的兼容性，定义全局函数
def caesar_enc(pt: str, shift: int) -> str:
    return ClassicalSuite.caesar_enc(pt, shift)

def caesar_dec(ct: str, shift: int) -> str:
    return ClassicalSuite.caesar_dec(ct, shift)

def vigenere_enc(pt: str, key: str) -> str:
    return ClassicalSuite.vigenere_enc(pt, key)

def vigenere_dec(ct: str, key: str) -> str:
    return ClassicalSuite.vigenere_dec(ct, key)

def morse_enc(pt: str) -> str:
    return ClassicalSuite.morse_enc(pt)

def morse_dec(ct: str) -> str:
    return ClassicalSuite.morse_dec(ct)