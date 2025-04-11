#!/bin/bash

# 設置輸出目錄
OUTPUT_DIR="generated_data"

# 創建輸出目錄（如果不存在）
mkdir -p "$OUTPUT_DIR"

# 運行個人資料生成器
echo "開始生成測試用個人資料..."
python3 text/personal_data_generator.py

echo "個人資料生成完成！"
echo "生成的文件位於 $OUTPUT_DIR 目錄中" 