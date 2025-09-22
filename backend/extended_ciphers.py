#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扩展算法：培根 / 栅栏 / 猪圈 / ROT13 / Atbash / 仿射"""
import string
from typing import Tuple

_alpha = string.ascii_uppercase

# ---------- 培根 ----------
BACON_DICT = {
    'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
    'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
    'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
    'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
    'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA', 'Z': 'BBAAB'
}
INV_BACON = {v: k for k, v in BACON_DICT.items()}

def bacon_enc(pt: str) -> str:
    return ''.join(BACON_DICT.get(c.upper(), c) for c in pt if c.isalpha())

def bacon_dec(ct: str) -> str:
    ct = ct.replace(' ', '')
    return ''.join(INV_BACON.get(ct[i:i+5], '?') for i in range(0, len(ct), 5))

# ---------- 栅栏 ----------
def rail_fence_enc(pt: str, rails: int) -> str:
    if rails <= 1: return pt
    fence = [[] for _ in range(rails)]
    rail, direction = 0, 1
    for ch in pt.upper():
        if ch.isalpha():
            fence[rail].append(ch)
            rail += direction
            if rail == rails - 1 or rail == 0: direction = -direction
    return ''.join(''.join(row) for row in fence)

def rail_fence_dec(ct: str, rails: int) -> str:
    if rails <= 1: return ct
    pattern = []
    rail, direction = 0, 1
    for _ in range(len(ct)):
        pattern.append(rail)
        rail += direction
        if rail == rails - 1 or rail == 0: direction = -direction
    # 重建索引
    pos = 0
    idx_map = {}
    for r in range(rails):
        for i, p in enumerate(pattern):
            if p == r: idx_map[i] = pos; pos += 1
    return ''.join(ct[idx_map[i]] for i in range(len(ct)))

# ---------- 猪圈（简版符号） ----------
PIGPEN_DICT = {
    'A': '⌝', 'B': '⌟', 'C': '⌞', 'D': '⌜', 'E': '⊔', 'F': '⊐',
    'G': '⊏', 'H': '⊓', 'I': '◸', 'J': '◹', 'K': '◿', 'L': '◺',
    'M': '△', 'N': '▽', 'O': '◁', 'P': '▷', 'Q': '▲', 'R': '▼',
    'S': '◀', 'T': '▶', 'U': '◣', 'V': '◢', 'W': '◤', 'X': '◥',
    'Y': '⧋', 'Z': '⧻'
}
INV_PIGPEN = {v: k for k, v in PIGPEN_DICT.items()}

def pigpen_enc(pt: str) -> str:
    return ''.join(PIGPEN_DICT.get(c.upper(), c) for c in pt if c.isalpha())

def pigpen_dec(ct: str) -> str:
    return ''.join(INV_PIGPEN.get(c, '?') for c in ct)

# ---------- ROT13 ----------
def rot13(pt: str) -> str:
    return ''.join(_alpha[( _alpha.index(c)+13 ) % 26] if c in _alpha else c for c in pt.upper())

# ---------- Atbash ----------
def atbash(pt: str) -> str:
    return ''.join(_alpha[25 - _alpha.index(c)] if c in _alpha else c for c in pt.upper())

# ---------- 仿射 ----------
def _gcd(a, b): 
    while b: a, b = b, a % b
    return a
def _modinv(a, m):
    if _gcd(a, m) != 1: return None
    return pow(a, -1, m)

def affine_enc(pt: str, a: int, b: int) -> str:
    if _gcd(a, 26) != 1: raise ValueError("a 必须与 26 互质")
    return ''.join(_alpha[(a * _alpha.index(c) + b) % 26] if c in _alpha else c for c in pt.upper())

def affine_dec(ct: str, a: int, b: int) -> str:
    if _gcd(a, 26) != 1: raise ValueError("a 必须与 26 互质")
    inv = _modinv(a, 26)
    return ''.join(_alpha[inv * (_alpha.index(c) - b) % 26] if c in _alpha else c for c in ct.upper())