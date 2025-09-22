#!/usr/bin/env python3
# -*- coding: utf-8 -*-
CATALOG = [
    # Base
    {"name_en": "B16",  "name_cn": "Base16",      "module": "base",  "func_enc": "base16_encode", "func_dec": "base16_decode", "need_key": False},
    {"name_en": "B32",  "name_cn": "Base32",      "module": "base",  "func_enc": "base32_encode", "func_dec": "base32_decode", "need_key": False},
    {"name_en": "B64",  "name_cn": "Base64",      "module": "base",  "func_enc": "base64_encode", "func_dec": "base64_decode", "need_key": False},
    {"name_en": "B85",  "name_cn": "Base85",      "module": "base",  "func_enc": "base85_encode", "func_dec": "base85_decode", "need_key": False},
    {"name_en": "B58",  "name_cn": "Base58",      "module": "base",  "func_enc": "base58_encode", "func_dec": "base58_decode", "need_key": False},
    {"name_en": "B36",  "name_cn": "Base36",      "module": "base",  "func_enc": "base36_encode", "func_dec": "base36_decode", "need_key": False},

    # 古典
    {"name_en": "CAE",  "name_cn": "凯撒 Caesar", "module": "classical", "func_enc": "caesar_enc", "func_dec": "caesar_dec", "need_key": True, "key_name": "shift", "key_type": "int"},
    {"name_en": "ROT",  "name_cn": "ROT13",       "module": "extended",  "func_enc": "rot13",      "func_dec": "rot13",      "need_key": False},
    {"name_en": "ATB",  "name_cn": "埃特巴什 Atbash", "module": "extended", "func_enc": "atbash", "func_dec": "atbash", "need_key": False},
    {"name_en": "AFF",  "name_cn": "仿射 Affine", "module": "extended",  "func_enc": "affine_enc", "func_dec": "affine_dec", "need_key": True, "key_name": "a,b", "key_type": "int,int"},
    {"name_en": "VIG",  "name_cn": "维吉尼亚 Vigenère", "module": "classical", "func_enc": "vigenere_enc", "func_dec": "vigenere_dec", "need_key": True, "key_name": "key", "key_type": "str"},
    {"name_en": "MOR",  "name_cn": "摩斯 Morse", "module": "classical", "func_enc": "morse_enc", "func_dec": "morse_dec", "need_key": False},
    {"name_en": "BAC",  "name_cn": "培根 Bacon", "module": "extended",  "func_enc": "bacon_enc", "func_dec": "bacon_dec", "need_key": False},
    {"name_en": "RAL",  "name_cn": "栅栏 Rail-Fence", "module": "extended", "func_enc": "rail_fence_enc", "func_dec": "rail_fence_dec", "need_key": True, "key_name": "rails", "key_type": "int"},
    {"name_en": "PIG",  "name_cn": "猪圈 Pigpen", "module": "extended",  "func_enc": "pigpen_enc", "func_dec": "pigpen_dec", "need_key": False},

    # 现代
    {"name_en": "RSA",  "name_cn": "RSA", "module": "rsa", "func_enc": "rsa_enc", "func_dec": "rsa_dec", "need_key": True, "key_name": "e,n|d,n", "key_type": "rsa"},
]

def get_catalog():
    return CATALOG

def find_cipher(name_en: str):
    for c in CATALOG:
        if c["name_en"] == name_en:
            return c
    return None