#!/bin/bash

# 設置輸出目錄
OUTPUT_DIR="generated_data"
mkdir -p "$OUTPUT_DIR"

echo "開始生成測試文件..."

# 運行 Python 腳本生成各種文件
python3 formats/generator.py

echo "文件生成完成！生成的文件在 $OUTPUT_DIR 目錄中。" 