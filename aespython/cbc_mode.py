#!/usr/bin/env python
"""
CBC Mode of operation

Running this file as __main__ will result in a self-test of the algorithm.

Algorithm per NIST SP 800-38A http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf

Copyright (c) 2010, Adam Newman http://www.caller9.com/
Licensed under the MIT license http://www.opensource.org/licenses/mit-license.php
"""
__author__ = "Adam Newman"
__all__ = "CBCMode",

class CBCMode:
    """Perform CBC operation on a block and retain IV information for next operation"""
    def __init__(self, block_cipher, block_size):
        self._block_cipher = block_cipher
        self._block_size = block_size
        self._iv = [0] * block_size

    def set_iv(self, iv):
        if len(iv) == self._block_size:
            self._iv = iv

    def encrypt_block(self, plaintext):
        iv=self._iv=self._block_cipher.cipher_block([i ^ j for i,j in zip(plaintext, self._iv)])
        return iv

    def decrypt_block(self, ciphertext):
        plaintext = self._block_cipher.decipher_block(ciphertext)
        for i,v in enumerate(self._iv):plaintext[i]^=v
        self._iv = ciphertext
        return plaintext
