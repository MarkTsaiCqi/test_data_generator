#!/bin/bash

# 設置輸出目錄
OUTPUT_DIR="generated_data"
mkdir -p "$OUTPUT_DIR"

echo "開始生成測試圖片..."

# 運行 Python 腳本生成各種大小的圖片
python3 imageSize/generator.py --small

echo "圖片生成完成！生成的文件在 $OUTPUT_DIR 目錄中。" 