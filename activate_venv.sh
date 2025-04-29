#!/bin/bash
# 仮想環境のセットアップと有効化を行うスクリプト

# 仮想環境ディレクトリ
VENV_DIR=".venv"

# 仮想環境が存在しない場合は作成
if [ ! -d "$VENV_DIR" ]; then
  echo "仮想環境 $VENV_DIR が存在しません。作成します..."
  uv venv $VENV_DIR
  if [ $? -ne 0 ]; then
    echo "仮想環境の作成に失敗しました。"
    exit 1
  fi
fi

# 仮想環境を有効化
echo "$VENV_DIR/bin/activate を source します..."
source "$VENV_DIR/bin/activate"

echo "仮想環境が有効化されました。" 