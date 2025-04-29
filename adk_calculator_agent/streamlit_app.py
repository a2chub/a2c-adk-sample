# -*- coding: utf-8 -*-
"""
ADK計算エージェントと対話するためのStreamlit Web UI。
FastAPIバックエンド (api.py) と通信します。
"""

import streamlit as st
import requests # FastAPIへのリクエスト用

# --- 定数 ---
# FastAPIサーバーのアドレス (api.py を実行している場所に合わせて変更)
API_URL = "http://127.0.0.1:8000/ask"

# --- Streamlit UI 設定 ---
st.set_page_config(page_title="計算エージェント", layout="wide")
st.title("🧮 計算エージェント (ADK + FastAPI + Streamlit)")
st.caption("足し算、引き算、掛け算ができます。「5たす3は？」のように入力してください。")

# --- チャット履歴の初期化 ---
# st.session_state を使って、セッション間で履歴を保持
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- チャット履歴の表示 ---
# 既存のメッセージをループして表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]): # "user" または "assistant"
        st.markdown(message["content"])

# --- ユーザー入力の処理 ---
# st.chat_input でユーザーからの入力を受け付ける
if prompt := st.chat_input("計算式を入力してください (例: 10 ひく 4)"):
    # 1. ユーザーメッセージを履歴に追加して表示
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. FastAPIエンドポイントにリクエストを送信
    try:
        response = requests.post(API_URL, json={"text": prompt})
        response.raise_for_status() # HTTPエラーがあれば例外を発生させる

        # 3. FastAPIからの応答を取得
        api_response_data = response.json()
        assistant_response = api_response_data.get("response", "エラー: 応答を取得できませんでした。")

    except requests.exceptions.RequestException as e:
        # ネットワークエラーやAPIサーバーのエラー
        st.error(f"APIへの接続中にエラーが発生しました: {e}")
        assistant_response = "APIとの通信に失敗しました。"
    except Exception as e:
        # その他の予期せぬエラー
        st.error(f"予期せぬエラーが発生しました: {e}")
        assistant_response = "不明なエラーが発生しました。"

    # 4. アシスタント（エージェント）の応答を履歴に追加して表示
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
