# -*- coding: utf-8 -*-
"""
足し算処理を担当するモジュール。
"""

def add(a: float, b: float) -> float:
    """
    2つの数値を加算します。

    Args:
        a (float): 1つ目の数値。
        b (float): 2つ目の数値。

    Returns:
        float: 加算結果。
    """
    print(f"足し算実行 (from adder_agent): {a} + {b}") # 実行確認用のログ
    return a + b
