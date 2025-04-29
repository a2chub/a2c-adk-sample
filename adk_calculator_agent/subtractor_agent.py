# -*- coding: utf-8 -*-
"""
引き算を実行する子エージェントのロジック。
"""

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
