# ベースイメージとして公式のPythonイメージを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get upgrade -y && apt-get install -y gcc

# アプリケーションの依存関係をインストール
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

# # アプリケーションのソースコードをコピー
# COPY . .

# # ポートを公開
# EXPOSE 80

# # アプリケーションを実行
# CMD ["python", "line_bot.py"]