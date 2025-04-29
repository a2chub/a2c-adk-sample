# -*- coding: utf-8 -*-
"""
親エージェントのメインスクリプト。
ユーザーからの入力を受け付け、計算の種類を判断し、
math_operations モジュールの関数を呼び出して結果を返します。
"""

import re # 数値抽出のために正規表現を使用
from adk import Agent, Message, IntentHandler, ConsoleChannel
# 各計算モジュールから関数をインポート
from adder_agent import add
from subtractor_agent import subtract
from multiplier_agent import multiply

# --- インテントハンドラー定義 ---

class AddIntentHandler(IntentHandler):
    """足し算インテントを処理するハンドラー"""
    intent_name = "AddIntent" # インテント名（任意）

    def can_handle(self, message: Message) -> bool:
        """
        メッセージが足し算に関連するかどうかを判断します。
        単純なキーワードマッチングを行います。
        """
        text = message.text.lower()
        # 足し算を示すキーワードが含まれているかチェック
        return "たす" in text or "足し算" in text or "+" in text or "足して" in text

    def handle(self, message: Message) -> Message:
        """
        メッセージから数値を抽出し、足し算を実行して結果を返します。
        """
        # 正規表現でメッセージから数値を抽出 (整数・小数を想定)
        # 例: "5たす3", "10と-2.5を足して" -> ['5', '3'], ['10', '-2.5']
        numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", message.text)
        num_list = [float(n) for n in numbers] # 文字列を数値(float)に変換

        if len(num_list) >= 2:
            # 抽出された数値リストから最初の2つを使用
            a, b = num_list[0], num_list[1]
            result = add(a, b) # adder_agent の add 関数を呼び出し
            response_text = f"{a} たす {b} は {result} です。"
        else:
            # 数値が2つ見つからなかった場合
            response_text = "すみません、足し算する2つの数値を認識できませんでした。"

        return Message(text=response_text) # 応答メッセージを作成して返す

class SubtractIntentHandler(IntentHandler):
    """引き算インテントを処理するハンドラー"""
    intent_name = "SubtractIntent"

    def can_handle(self, message: Message) -> bool:
        """
        メッセージが引き算に関連するかどうかを判断します。
        """
        text = message.text.lower()
        # 引き算を示すキーワードが含まれているかチェック
        return "ひく" in text or "引き算" in text or "-" in text or "引いて" in text

    def handle(self, message: Message) -> Message:
        """
        メッセージから数値を抽出し、引き算を実行して結果を返します。
        """
        numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", message.text)
        num_list = [float(n) for n in numbers]

        if len(num_list) >= 2:
            a, b = num_list[0], num_list[1]
            result = subtract(a, b) # subtractor_agent の subtract 関数を呼び出し
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
        """
        text = message.text.lower()
        # 掛け算を示すキーワードが含まれているかチェック
        return "かける" in text or "掛け算" in text or "*" in text or "掛けて" in text

    def handle(self, message: Message) -> Message:
        """
        メッセージから数値を抽出し、掛け算を実行して結果を返します。
        """
        numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", message.text)
        num_list = [float(n) for n in numbers]

        if len(num_list) >= 2:
            a, b = num_list[0], num_list[1]
            result = multiply(a, b) # multiplier_agent の multiply 関数を呼び出し
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
        """
        return True

    def handle(self, message: Message) -> Message:
        """
        どの計算処理も実行できなかった場合の応答を返します。
        """
        response_text = "すみません、よく分かりませんでした。足し算、引き算、掛け算のいずれかを含む形で質問してください。（例：「5たす3は？」）"
        return Message(text=response_text)

# --- エージェントのセットアップと実行 ---

def main():
    """エージェントを初期化し、コンソールチャネルで実行します。"""
    # エージェントインスタンスを作成
    agent = Agent(agent_id="calculator_agent") # エージェントID（任意）

    # インテントハンドラーをエージェントに登録
    # 登録順が重要。より具体的なハンドラーを先に登録する。
    agent.register_intent_handler(AddIntentHandler())
    agent.register_intent_handler(SubtractIntentHandler())
    agent.register_intent_handler(MultiplyIntentHandler())
    # FallbackHandler は最後に登録し、他のどのハンドラーも処理できなかったメッセージを捕捉する
    agent.register_intent_handler(FallbackIntentHandler())

    # コンソールチャネルを作成してエージェントを実行
    # ユーザーはコンソールからテキストを入力し、エージェントが応答する
    channel = ConsoleChannel()
    print("計算エージェントを開始します。「5たす3は？」のように話しかけてください。終了するには 'quit' と入力してください。")
    agent.run(channel) # エージェントの実行ループを開始
    print("エージェントを終了します。")

# スクリプトが直接実行された場合に main 関数を呼び出す
if __name__ == "__main__":
    main()
