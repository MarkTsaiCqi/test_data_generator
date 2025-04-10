#!/bin/bash

# 定義輸出目錄
OUTPUT_DIR="generated_data"

# 創建輸出目錄
mkdir -p "$OUTPUT_DIR"

# --- 主程序 --- #

echo "開始生成測試圖片..."

# 生成圖片文件
echo "--- 生成圖片文件 ---"
if [ -d "image" ]; then
    # 首先執行除了 big_imageGenerator.py 之外的所有腳本
    for py_script in image/*.py; do
        if [ -f "$py_script" ] && [ "$(basename "$py_script")" != "big_imageGenerator.py" ]; then
            script_name=$(basename "$py_script")
            echo "調用 $script_name 生成圖片..."
            if PYTHONPATH=. python3 "$py_script" --output-dir "$OUTPUT_DIR"; then
                echo "$script_name 執行完畢。"
            else
                echo "錯誤：執行 $script_name 失敗。"
            fi
        fi
    done

    # 最後執行 big_imageGenerator.py
    if [ -f "image/big_imageGenerator.py" ]; then
        echo "調用 big_imageGenerator.py 生成大型圖片..."
        if PYTHONPATH=. python3 image/big_imageGenerator.py --output-dir "$OUTPUT_DIR"; then
            echo "big_imageGenerator.py 執行完畢。"
        else
            echo "錯誤：執行 big_imageGenerator.py 失敗。"
        fi
    fi
else
    echo "警告：未找到 image 目錄，跳過圖片生成。"
fi

echo "--- 測試圖片生成完畢 ---" 