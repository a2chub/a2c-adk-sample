# -*- coding: utf-8 -*-
"""
計算操作モジュール。
各種の数学的演算機能（足し算、引き算、掛け算）を提供します。
"""

def add(a: float, b: float) -> float:
    """
    2つの数値を加算します。

    Args:
        a (float): 1番目の数値。
        b (float): 2番目の数値。

    Returns:
        float: 加算結果。

    Raises:
        TypeError: 引数が数値でない場合。
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        error_message = f"数値以外の引数が指定されました。関数名: add, 引数a: {a} (型: {type(a)}), 引数b: {b} (型: {type(b)})"
        raise TypeError(error_message)
    return a + b

def subtract(a: float, b: float) -> float:
    """
    1番目の数値から2番目の数値を減算します。

    Args:
        a (float): 1番目の数値 (被減数)。
        b (float): 2番目の数値 (減数)。

    Returns:
        float: 減算結果。

    Raises:
        TypeError: 引数が数値でない場合。
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        error_message = f"数値以外の引数が指定されました。関数名: subtract, 引数a: {a} (型: {type(a)}), 引数b: {b} (型: {type(b)})"
        raise TypeError(error_message)
    return a - b

def multiply(a: float, b: float) -> float:
    """
    2つの数値を乗算します。

    Args:
        a (float): 1番目の数値。
        b (float): 2番目の数値。

    Returns:
        float: 乗算結果。

    Raises:
        TypeError: 引数が数値でない場合。
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        error_message = f"数値以外の引数が指定されました。関数名: multiply, 引数a: {a} (型: {type(a)}), 引数b: {b} (型: {type(b)})"
        raise TypeError(error_message)
    return a * b 