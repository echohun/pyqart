# Added at  : 2016.07.28
# Author    : 7sDream
# Usage     : Some common function to process data.

import functools


__all__ = ['bit_at', 'one_at', 'zero_at', 'set_bit']


@functools.lru_cache(maxsize=8)
def one_at(pos):
    """
    Create a 8-bit int which only has one '1' bit at specific position.

    example:

    one_at(0) -> 0b10000000
    one_at(3) -> 0b00010000

    :param int pos: position of '1' bit.
    :rtype: int
    """
    assert 0 <= pos < 8
    return 1 << (7 - pos)


@functools.lru_cache(maxsize=8)
def zero_at(pos):
    """
    Create a 8-bit int which only has one '0' bit at specific position.

    :param int pos: position of '0' bit.
    :rtype: int
    """
    assert 0 <= pos < 8
    return (~one_at(pos)) & 0xFF


def set_bit(value, pos, bit):
    """
    Set bit at specific position of a 8-bit value to '1' or '0'

    :param int value: Original value, 8 bit.
    :param int pos: Position of bit which will be set.
    :param bool bit: True for 1, False for 0.
    :return: New value
    :rtype: int
    """
    assert 0 <= pos < 8

    if bit:
        return value | one_at(pos)
    else:
        return value & zero_at(pos)


def bit_at(value, length, pos):
    """
    Get bit at pos of number, True for '1', False for '0':

    :param int value: Int value to get the bit.
    :param int length: Length of value by bit.
    :param int pos: Bit position, highest position is 0.
    :rtype: bool
    """

    assert length > 0
    assert 0 <= pos < length
    return ((value >> (length - 1 - pos)) & one_at(7)) == 1
