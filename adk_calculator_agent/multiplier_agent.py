# -*- coding: utf-8 -*-
"""
掛け算処理を担当するモジュール。
"""

def multiply(a: float, b: float) -> float:
    """
    2つの数値を乗算します。

    Args:
        a (float): 1つ目の数値。
        b (float): 2つ目の数値。

    Returns:
        float: 乗算結果。
    """
    print(f"掛け算実行 (from multiplier_agent): {a} * {b}") # 実行確認用のログ
    return a * b
