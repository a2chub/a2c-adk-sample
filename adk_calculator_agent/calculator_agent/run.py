# -*- coding: utf-8 -*-
"""
計算エージェントの実行スクリプト。
コンソールチャネルを使用してエージェントを実行します。
"""

from adk.channels import ConsoleChannel
from .agent import root_agent


def main():
    """
    エージェントをコンソールチャネルで実行します。
    ユーザーはコンソールからテキストを入力し、エージェントが応答します。
    終了するには 'quit' と入力します。
    """
    channel = ConsoleChannel()
    print("計算エージェントを開始します。「5たす3は？」のように話しかけてください。終了するには 'quit' と入力してください。")
    root_agent.run(channel)
    print("エージェントを終了します。")


if __name__ == "__main__":
    main() 