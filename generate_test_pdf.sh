#!/bin/bash

# 檢查是否提供了輸入檔案
if [ "$#" -ne 1 ]; then
    echo "用法: $0 input.txt"
    exit 1
fi

# 指定輸入和輸出檔案
input_file="$1"
output_file="output.pdf"

# 呼叫 generator.py 生成 PDF
python3 file/generator.py "$input_file" "$output_file"
