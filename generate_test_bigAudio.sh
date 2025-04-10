#!/bin/bash

# 設置輸出目錄
OUTPUT_DIR="generated_data"
mkdir -p "$OUTPUT_DIR"

echo "開始生成測試音頻..."

# 運行 Python 腳本生成各種大小的音頻
python3 audio/generator.py --big

echo "音頻生成完成！生成的文件在 $OUTPUT_DIR 目錄中。" 