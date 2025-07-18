#!/bin/bash

# 設置輸出目錄
OUTPUT_DIR="generated_data"
mkdir -p "$OUTPUT_DIR"

echo "開始生成測試圖片..."

# 運行 Python 腳本生成各種大小的圖片（包括9.9MB、10.0MB、10.1MB）
python3 image/generator.py

echo "圖片生成完成！生成的文件在 $OUTPUT_DIR 目錄中。"
echo ""
echo "查看生成的圖片大小："
ls -lh "$OUTPUT_DIR"/*.png "$OUTPUT_DIR"/*.jpeg "$OUTPUT_DIR"/*.gif 2>/dev/null 