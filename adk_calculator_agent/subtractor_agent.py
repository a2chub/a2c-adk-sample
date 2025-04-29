# -*- coding: utf-8 -*-
"""
引き算処理を担当するモジュール。
"""

def subtract(a: float, b: float) -> float:
    """
    1つ目の数値から2つ目の数値を減算します。

    Args:
        a (float): 減算される数値。
        b (float): 減算する数値。

    Returns:
        float: 減算結果。
    """
    print(f"引き算実行 (from subtractor_agent): {a} - {b}") # 実行確認用のログ
    return a - b
