#!/usr/bin/python3
"""
Module lazy_matrix_mul
Provides matrix multiplication using NumPy.
"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's matmul.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The product matrix.
    """
    return numpy.matmul(m_a, m_b)
