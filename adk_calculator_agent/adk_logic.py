# -*- coding: utf-8 -*-
"""
ADKエージェントのコアロジックを管理するモジュール。
FastAPIから呼び出されることを想定しています。
"""

import re
from adk import Agent, Message, IntentHandler
# 各計算モジュールから関数をインポート
from .adder_agent import add
from .subtractor_agent import subtract
from .multiplier_agent import multiply

# --- インテントハンドラー定義 (main_agent.py からコピー・調整) ---

class AddIntentHandler(IntentHandler):
    """足し算インテントを処理するハンドラー"""
    intent_name = "AddIntent"

    def can_handle(self, message: Message) -> bool:
        text = message.text.lower()
        return "たす" in text or "足し算" in text or "+" in text or "足して" in text

    def handle(self, message: Message) -> Message:
        numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", message.text)
        num_list = [float(n) for n in numbers]
        if len(num_list) >= 2:
            a, b = num_list[0], num_list[1]
            result = add(a, b)
            response_text = f"{a} たす {b} は {result} です。"
        else:
            response_text = "すみません、足し算する2つの数値を認識できませんでした。"
        return Message(text=response_text)

class SubtractIntentHandler(IntentHandler):
    """引き算インテントを処理するハンドラー"""
    intent_name = "SubtractIntent"

    def can_handle(self, message: Message) -> bool:
        text = message.text.lower()
        return "ひく" in text or "引き算" in text or "-" in text or "引いて" in text

    def handle(self, message: Message) -> Message:
        numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", message.text)
        num_list = [float(n) for n in numbers]
        if len(num_list) >= 2:
            a, b = num_list[0], num_list[1]
            result = subtract(a, b)
            response_text = f"{a} ひく {b} は {result} です。"
        else:
            response_text = "すみません、引き算する2つの数値を認識できませんでした。"
        return Message(text=response_text)

class MultiplyIntentHandler(IntentHandler):
    """掛け算インテントを処理するハンドラー"""
    intent_name = "MultiplyIntent"

    def can_handle(self, message: Message) -> bool:
        text = message.text.lower()
        return "かける" in text or "掛け算" in text or "*" in text or "掛けて" in text

    def handle(self, message: Message) -> Message:
        numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", message.text)
        num_list = [float(n) for n in numbers]
        if len(num_list) >= 2:
            a, b = num_list[0], num_list[1]
            result = multiply(a, b)
            response_text = f"{a} かける {b} は {result} です。"
        else:
            response_text = "すみません、掛け算する2つの数値を認識できませんでした。"
        return Message(text=response_text)

class FallbackIntentHandler(IntentHandler):
    """どのインテントにもマッチしなかった場合のフォールバックハンドラー"""
    intent_name = "FallbackIntent"

    def can_handle(self, message: Message) -> bool:
        return True # 他のハンドラーが処理しなかった場合に常に処理

    def handle(self, message: Message) -> Message:
        response_text = "すみません、よく分かりませんでした。足し算、引き算、掛け算のいずれかを含む形で質問してください。（例：「5たす3は？」）"
        return Message(text=response_text)

# --- エージェントの初期化 ---

# Agentインスタンスをグローバル（またはシングルトンパターンなど）で作成・保持
# FastAPIアプリの起動時に一度だけ初期化されるようにする想定
agent = Agent(agent_id="calculator_agent_api")

# インテントハンドラーを登録
agent.register_intent_handler(AddIntentHandler())
agent.register_intent_handler(SubtractIntentHandler())
agent.register_intent_handler(MultiplyIntentHandler())
agent.register_intent_handler(FallbackIntentHandler()) # フォールバックは最後に

# --- 応答生成関数 ---

def get_agent_response(user_input: str) -> str:
    """
    ユーザー入力テキストを受け取り、ADKエージェントで処理して応答テキストを返します。

    Args:
        user_input (str): ユーザーからの入力テキスト。

    Returns:
        str: エージェントからの応答テキスト。
    """
    # ユーザー入力をADKのMessageオブジェクトに変換
    request_message = Message(text=user_input)

    # エージェントにメッセージ処理を依頼 (同期的に処理されるメソッドを想定)
    # adk-python の Agent クラスに `handle_message` のようなメソッドがあるか、
    # または内部的に同期処理を行う仕組みがあるかを仮定しています。
    # (もし非同期処理が必要な場合は、FastAPI側で工夫が必要です)
    # ここでは仮に `agent.process_message` が応答Messageを返すとします。
    # 実際のADKのAPIに合わせて調整が必要になる可能性があります。
    try:
        # ADKのAgentクラスが直接メッセージを処理して応答を返すメソッドを持っているか確認が必要
        # ここでは仮のメソッド名 `process_message` を使用
        response_message = agent.handle_message(request_message) # handle_message が Message を返すと仮定
        return response_message.text
    except Exception as e:
        # エラーハンドリング (実際の状況に合わせて調整)
        print(f"エージェント処理中にエラーが発生しました: {e}")
        return "すみません、処理中にエラーが発生しました。"

# 注意: 上記の `agent.handle_message` は adk-python の実際のAPIに基づいたものではなく、
#       同期的にリクエストを処理するための仮のメソッド呼び出しです。
#       実際の adk-python の使い方によっては、この部分の実装方法が変わる可能性があります。
#       特に、Agentが非同期処理を前提としている場合、FastAPIでの扱い方が異なります。
