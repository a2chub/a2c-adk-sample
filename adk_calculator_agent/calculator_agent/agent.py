# -*- coding: utf-8 -*-
"""
計算エージェントの主要モジュール。
自然言語入力から計算操作を識別し、適切な計算関数を呼び出します。
"""

import re
from adk.agents import Agent
from adk.messages import Message
from adk.intents import IntentHandler
from adk.channels import ConsoleChannel
from .operations import add, subtract, multiply


class AddIntentHandler(IntentHandler):
    """足し算インテントを処理するハンドラー"""
    intent_name = "AddIntent"

    def can_handle(self, message: Message) -> bool:
        """
        メッセージが足し算に関連するかどうかを判断します。
        単純なキーワードマッチングを行います。

        Args:
            message (Message): 処理するメッセージ

        Returns:
            bool: メッセージが処理可能ならTrue、そうでなければFalse
        """
        text = message.text.lower()
        return "たす" in text or "足し算" in text or "+" in text or "足して" in text

    def handle(self, message: Message) -> Message:
        """
        メッセージから数値を抽出し、足し算を実行して結果を返します。

        Args:
            message (Message): 処理するメッセージ

        Returns:
            Message: 応答メッセージ
        """
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
        """
        メッセージが引き算に関連するかどうかを判断します。

        Args:
            message (Message): 処理するメッセージ

        Returns:
            bool: メッセージが処理可能ならTrue、そうでなければFalse
        """
        text = message.text.lower()
        return "ひく" in text or "引き算" in text or "-" in text or "引いて" in text

    def handle(self, message: Message) -> Message:
        """
        メッセージから数値を抽出し、引き算を実行して結果を返します。

        Args:
            message (Message): 処理するメッセージ

        Returns:
            Message: 応答メッセージ
        """
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
        """
        メッセージが掛け算に関連するかどうかを判断します。

        Args:
            message (Message): 処理するメッセージ

        Returns:
            bool: メッセージが処理可能ならTrue、そうでなければFalse
        """
        text = message.text.lower()
        return "かける" in text or "掛け算" in text or "*" in text or "掛けて" in text

    def handle(self, message: Message) -> Message:
        """
        メッセージから数値を抽出し、掛け算を実行して結果を返します。

        Args:
            message (Message): 処理するメッセージ

        Returns:
            Message: 応答メッセージ
        """
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
        """
        常に True を返します。
        他のハンドラーが can_handle で False を返した場合に、このハンドラーが選択されます。

        Args:
            message (Message): 処理するメッセージ

        Returns:
            bool: 常にTrue
        """
        return True

    def handle(self, message: Message) -> Message:
        """
        どの計算処理も実行できなかった場合の応答を返します。

        Args:
            message (Message): 処理するメッセージ

        Returns:
            Message: 応答メッセージ
        """
        response_text = "すみません、よく分かりませんでした。足し算、引き算、掛け算のいずれかを含む形で質問してください。（例：「5たす3は？」）"
        return Message(text=response_text)


# エージェントインスタンス（外部からインポートされる主要オブジェクト）
root_agent = Agent(
    name="calculator_agent",
    model="gemini-2.0-flash",  # ADKドキュメントに基づくモデル指定
    description="計算機能を持つエージェント。足し算、引き算、掛け算をサポートします。",
    instruction="あなたは計算を手伝うエージェントです。ユーザーからの数値計算のリクエストに応答してください。"
)

# インテントハンドラーを登録
root_agent.register_intent_handler(AddIntentHandler())
root_agent.register_intent_handler(SubtractIntentHandler())
root_agent.register_intent_handler(MultiplyIntentHandler())
root_agent.register_intent_handler(FallbackIntentHandler()) 