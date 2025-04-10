#!/bin/bash

# 定義輸出目錄
OUTPUT_DIR="generated_data"

# 創建輸出目錄
mkdir -p "$OUTPUT_DIR"

# --- 主程序 --- #

echo "開始生成測試文本..."

# 生成文本文件
echo "--- 生成文本文件 ---"
if [ -f "text/generator.py" ]; then
    echo "調用 text/generator.py 生成測試文本..."
    if PYTHONPATH=. python3 text/generator.py --output-dir "$OUTPUT_DIR"; then
        echo "text/generator.py 執行完畢。"
    else
        echo "錯誤：執行 text/generator.py 失敗。"
    fi
else
    echo "警告：未找到 text/generator.py，跳過文本生成。"
fi

echo "--- 測試文本生成完畢 ---" 