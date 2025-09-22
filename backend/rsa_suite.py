#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统一 dispatcher：Base / Classical / RSA / Extended"""
from .extended_ciphers import (
    bacon_enc, bacon_dec, rail_fence_enc, rail_fence_dec,
    pigpen_enc, pigpen_dec, rot13, atbash, affine_enc, affine_dec
)
from .classical_suite import *
from .base_suite import *
# Deleted:from .rsa_suite import *
from .cipher_catalog import find_cipher









#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rsa_enc(plaintext: int, public_key: tuple) -> int:
    """RSA加密函数
    
    Args:
        plaintext: 明文（整数）
        public_key: 公钥 (e, n)
    
    Returns:
        密文（整数）
    """
    e, n = public_key
    return pow(plaintext, e, n)


def rsa_dec(ciphertext: int, private_key: tuple) -> int:
    """RSA解密函数
    
    Args:
        ciphertext: 密文（整数）
        private_key: 私钥 (d, n)
    
    Returns:
        明文（整数）
    """
    d, n = private_key
    return pow(ciphertext, d, n)











def dispatch_encrypt(name_en: str, text: str, key: dict = None) -> str:
    algo = find_cipher(name_en)
    if not algo:
        raise ValueError("不支持的算法")
    m, f = algo["module"], algo["func_enc"]
    if m == "base":
        return globals()[f](text, key["type"])               # key={"type":"64"}
    if m == "classical":
        if name_en == "CAE":
            return caesar_enc(text, int(key["shift"]))
        if name_en == "VIG":
            return vigenere_enc(text, key["key"])
        if name_en == "MOR":
            return morse_enc(text)
    if m == "extended":
        if name_en == "ROT":
            return rot13(text)
        if name_en == "ATB":
            return atbash(text)
        if name_en == "AFF":
            return affine_enc(text, int(key["a"]), int(key["b"]))
        if name_en == "BAC":
            return bacon_enc(text)
        if name_en == "RAL":
            return rail_fence_enc(text, int(key["rails"]))
        if name_en == "PIG":
            return pigpen_enc(text)
    if m == "rsa":
        return str(rsa_enc(int(text), (int(key["e"]), int(key["n"]))))
    raise RuntimeError("dispatch 未实现")


def dispatch_decrypt(name_en: str, text: str, key: dict = None) -> str:
    algo = find_cipher(name_en)
    if not algo:
        raise ValueError("不支持的算法")
    m, f = algo["module"], algo["func_dec"]
    if m == "base":
        return globals()[f](text, key["type"])
    if m == "classical":
        if name_en == "CAE":
            return caesar_dec(text, int(key["shift"]))
        if name_en == "VIG":
            return vigenere_dec(text, key["key"])
        if name_en == "MOR":
            return morse_dec(text)
    if m == "extended":
        if name_en == "ROT":
            return rot13(text)
        if name_en == "ATB":
            return atbash(text)
        if name_en == "AFF":
            return affine_dec(text, int(key["a"]), int(key["b"]))
        if name_en == "BAC":
            return bacon_dec(text)
        if name_en == "RAL":
            return rail_fence_dec(text, int(key["rails"]))
        if name_en == "PIG":
            return pigpen_dec(text)
    if m == "rsa":
        return str(rsa_dec(int(text), (int(key["d"]), int(key["n"]))))
    raise RuntimeError("dispatch 未实现")