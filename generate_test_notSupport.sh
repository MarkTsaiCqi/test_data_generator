#!/bin/bash

# 設置輸出目錄
OUTPUT_DIR="generated_data/not_supported"

# 創建輸出目錄（如果不存在）
mkdir -p "$OUTPUT_DIR"

# 運行文件生成器
echo "開始生成不支持的測試文件..."
python3 file/generator.py --invalid

echo "文件生成完成！"
echo "生成的文件位於 $OUTPUT_DIR 目錄中" 