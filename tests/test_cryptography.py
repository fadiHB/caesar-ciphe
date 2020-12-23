from cryptography import __version__
from cryptography.caesar_cipher import encrypt,decrypt


def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    actual = encrypt('abcd yz',2)
    expected = 'cdef ab'
    assert actual == expected

def test_decrypt():
    actual = decrypt('cdef ab',2)
    expected = 'abcd yz'
    assert actual == expected
