# -*- coding: utf-8 -*-
"""
ADK計算エージェントのロジックをラップするFastAPIアプリケーション。
Streamlit UIからのリクエストを受け付け、エージェントの応答を返します。
"""

from fastapi import FastAPI
from pydantic import BaseModel # リクエスト/レスポンスのデータ構造定義用
import uvicorn

# ADKエージェントの応答生成関数をインポート
# 注意: FastAPIサーバーを起動するディレクトリによっては、
#       相対インポートがうまく機能しない場合があります。
#       その場合は `from adk_calculator_agent.adk_logic import get_agent_response` のように
#       絶対パスでのインポートが必要になるかもしれません。
from .adk_logic import get_agent_response

# --- Pydanticモデル定義 ---

class AskRequest(BaseModel):
    """ /ask エンドポイントへのリクエストボディのスキーマ """
    text: str # ユーザーからの入力テキスト

class AskResponse(BaseModel):
    """ /ask エンドポイントのレスポンスボディのスキーマ """
    response: str # エージェントからの応答テキスト

# --- FastAPIアプリケーションの初期化 ---

app = FastAPI(
    title="ADK Calculator Agent API",
    description="ADK計算エージェントと対話するためのAPI",
    version="0.1.0",
)

# --- APIエンドポイント定義 ---

@app.post("/ask", response_model=AskResponse, summary="エージェントに質問する")
async def ask_agent(request: AskRequest):
    """
    ユーザーからのテキスト入力を受け取り、ADKエージェントで処理し、
    その応答を返します。
    """
    print(f"API 受信: {request.text}") # 受信ログ
    # ADKロジック関数を呼び出して応答を取得
    agent_reply = get_agent_response(request.text)
    print(f"API 応答: {agent_reply}") # 応答ログ
    # レスポンスモデルに従って応答を返す
    return AskResponse(response=agent_reply)

# --- Uvicornでの実行設定 (直接実行用) ---
# 通常は `uvicorn adk_calculator_agent.api:app --reload` のようにコマンドラインから起動します。
if __name__ == "__main__":
    # ホスト '0.0.0.0' は、ローカルネットワーク内の他のデバイスからのアクセスを許可します。
    # ローカルマシンからのみアクセスする場合は '127.0.0.1' を使用します。
    # ポート8000でリッスンします。
    uvicorn.run(app, host="127.0.0.1", port=8000)
