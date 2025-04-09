#!/bin/bash

# 檢查是否提供了足夠的參數
if [ $# -lt 2 ]; then
    echo "用法:"
    echo "1. 圖片轉 Base64: $0 image_to_base64 <圖片文件路徑> [輸出目錄]"
    echo "2. Base64 轉圖片: $0 base64_to_image <base64文件路徑> [輸出目錄]"
    echo "3. b64_json 轉圖片: $0 b64_json_to_image <json文件路徑> [輸出目錄]"
    echo "   示例: $0 b64_json_to_image example_image.json"
    exit 1
fi

# 獲取操作類型和文件路徑
OPERATION="$1"
INPUT_FILE="$2"
# 確保默認輸出目錄是當前目錄下的 generated_data
OUTPUT_DIR="${3:-generated_data}"

# 創建輸出目錄（如果不存在）
mkdir -p "$OUTPUT_DIR"

# 根據操作類型執行相應的轉換
case "$OPERATION" in
    "image_to_base64")
        # 檢查輸入文件是否存在
        if [ ! -f "$INPUT_FILE" ]; then
            echo "錯誤：圖片文件不存在 - $INPUT_FILE"
            exit 1
        fi

        # 生成輸出文件名
        TIMESTAMP=$(date +%Y%m%d_%H%M%S)
        OUTPUT_FILE="$OUTPUT_DIR/image_$TIMESTAMP.base64"

        # 將圖片轉換為 Base64 (使用 -w 0 避免換行)
        base64 -w 0 "$INPUT_FILE" > "$OUTPUT_FILE"
        echo "Base64 數據已保存到：$OUTPUT_FILE"
        ;;
    
    "base64_to_image")
        # 檢查輸入文件是否存在
        if [ ! -f "$INPUT_FILE" ]; then
            echo "錯誤：Base64 文件不存在 - $INPUT_FILE"
            exit 1
        fi

        # 生成輸出文件名 (恢復為 .jpg)
        TIMESTAMP=$(date +%Y%m%d_%H%M%S)
        OUTPUT_FILE="$OUTPUT_DIR/image_$TIMESTAMP.jpg"

        # 將 Base64 轉換為圖片
        if ! base64 -d "$INPUT_FILE" > "$OUTPUT_FILE" 2>/dev/null; then
            echo "錯誤：Base64 解碼失敗"
            echo "請檢查 Base64 數據是否完整且格式正確"
            exit 1
        fi

        echo "圖片已生成：$OUTPUT_FILE"
        ;;
    
    "b64_json_to_image")
        # 檢查輸入文件是否存在
        if [ ! -f "$INPUT_FILE" ]; then
            echo "錯誤：JSON 文件不存在 - $INPUT_FILE"
            exit 1
        fi

        # 檢查是否安裝了 jq
        if ! command -v jq &> /dev/null; then
            echo "錯誤：需要安裝 jq 工具"
            echo "請執行：sudo apt-get install jq"
            exit 1
        fi

        # 從 JSON 中提取 b64_json 數據並進行清理 (恢復之前的 tr/sed 清理，因為 grep 可能過於嚴格)
        B64_DATA=$(jq -r '.data[0].b64_json' "$INPUT_FILE" | tr -d '\n\r\t ' | sed 's/\\n//g')

        if [ -z "$B64_DATA" ] || [ "$B64_DATA" = "null" ]; then
            echo "錯誤：無法從 JSON 文件中提取有效的 b64_json 數據"
            exit 1
        fi

        # 生成輸出文件名 (恢復為 .jpg)
        TIMESTAMP=$(date +%Y%m%d_%H%M%S)
        OUTPUT_FILE="$OUTPUT_DIR/image_$TIMESTAMP.jpg"

        # 創建臨時文件來存儲清理後的 Base64 數據
        TEMP_FILE=$(mktemp)
        echo "$B64_DATA" > "$TEMP_FILE"

        # 將 Base64 數據解碼為圖片
        if ! base64 -d "$TEMP_FILE" > "$OUTPUT_FILE" 2>/dev/null; then
            echo "錯誤：Base64 解碼失敗"
            echo "請檢查 Base64 數據是否完整且格式正確"
            rm "$TEMP_FILE"
            exit 1
        fi

        # 清理臨時文件
        rm "$TEMP_FILE"

        echo "圖片已生成：$OUTPUT_FILE"
        ;;
    
    *)
        echo "錯誤：未知的操作類型 '$OPERATION'"
        echo "可用的操作類型：image_to_base64, base64_to_image, b64_json_to_image"
        exit 1
        ;;
esac 