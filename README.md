# 計算エージェント - アプリケーション起動手順

このプロジェクトは、Google ADK（Agent Development Kit）を使用した計算エージェントのサンプル実装です。
足し算、引き算、掛け算の自然言語処理機能を持つ対話型エージェントを提供します。

## 必要環境

- Python 3.7以上
- `uv` パッケージマネージャー

## セットアップ手順

### 1. リポジトリをクローン

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. 仮想環境のセットアップ

提供されている `activate_venv.sh` スクリプトを使用して仮想環境をセットアップします：

```bash
# 仮想環境をセットアップして有効化
source activate_venv.sh
```

### 3. Google ADK Pythonのインストール

仮想環境内に Google ADK Python ライブラリをインストールします：

```bash
# ADK Python ライブラリをインストール
uv pip install git+https://github.com/google/adk-python.git
```

### 4. API Keyの設定

1. Google AI Studio（https://makersuite.google.com/）からAPIキーを取得します
2. `adk_calculator_agent/.env` ファイルを編集し、APIキーを設定します

```
# .envファイルを開く
nano adk_calculator_agent/.env

# 以下の行を編集（APIキーを貼り付け）
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

## アプリケーションの実行

### コンソールで実行

```bash
# 仮想環境が有効化されていることを確認
cd adk_calculator_agent
python run.py
```

### 使用方法

エージェントが起動したら、自然言語で計算リクエストを入力できます：

- **足し算の例**: 「5たす3は？」「10と20を足して」
- **引き算の例**: 「10ひく5は？」「15から7を引いて」
- **掛け算の例**: 「3かける4は？」「5と6を掛けて」

終了するには `quit` と入力します。

## プロジェクト構造

```
adk_calculator_agent/
├── .env                      # 環境変数設定ファイル
├── run.py                    # ルートレベルの実行スクリプト
└── calculator_agent/         # メインパッケージディレクトリ
    ├── __init__.py           # モジュール初期化ファイル
    ├── agent.py              # エージェント定義ファイル
    ├── operations.py         # 計算操作の実装ファイル
    └── run.py                # エージェント実行ファイル
```

## トラブルシューティング

- **APIキーエラー**: `.env` ファイル内のAPIキーが正しく設定されていることを確認してください
- **インポートエラー**: 必要なパッケージがすべてインストールされていることを確認してください
- **実行エラー**: 仮想環境が正しく有効化されていることを確認してください 