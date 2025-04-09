#!/bin/bash

# 獲取腳本所在目錄的絕對路徑
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 創建輸出目錄
OUTPUT_DIR="$SCRIPT_DIR/generated_data"
mkdir -p "$OUTPUT_DIR"

# 顯示選單
show_menu() {
    echo "測試資料生成工具"
    echo "1. 生成所有測試文檔和圖檔"
    echo "2. 生成Base64編碼的圖片"
    echo "3. 從Base64檔案還原圖片"
    echo "4. 退出"
    echo -n "請選擇操作 (1-4): "
}

# 生成測試文字
generate_text() {
    echo "正在生成測試文字..."
    
    # 創建輸出檔案
    output_file="$OUTPUT_DIR/test_text.txt"
    echo "測試文字內容：" > "$output_file"
    echo "=====================" >> "$output_file"
    echo >> "$output_file"
    
    # 生成50字元的英文文字
    echo "1. 50字元的英文文字：" >> "$output_file"
    python3 "$SCRIPT_DIR/text/generator.py" --type short >> "$output_file"
    echo >> "$output_file"
    
    # 生成5000字元的英文文章
    echo "2. 5000字元的英文文章：" >> "$output_file"
    python3 "$SCRIPT_DIR/text/generator.py" --type long >> "$output_file"
    echo >> "$output_file"
    
    # 生成特殊字元文字
    echo "3. 特殊字元文字：" >> "$output_file"
    python3 "$SCRIPT_DIR/text/generator.py" --type special >> "$output_file"
    
    echo "測試文字已生成完成！"
    echo "檔案位置: $output_file"
}

# 生成測試圖片
generate_image() {
    echo "正在生成測試圖片..."
    
    # 生成指定大小的圖片
    echo "生成指定大小的圖片 (1.9MB, 2.0MB, 2.1MB)..."
    python3 image/big_imageGenerator.py --output-dir "$OUTPUT_DIR"
    
    # 生成不同解析度的圖片
    echo "生成不同解析度的圖片..."
    python3 image/resolution_imageGenerator.py --width 1920 --height 1080 --output-dir "$OUTPUT_DIR"
    python3 image/resolution_imageGenerator.py --width 3840 --height 2160 --output-dir "$OUTPUT_DIR"
    python3 image/resolution_imageGenerator.py --width 800 --height 600 --output-dir "$OUTPUT_DIR"
    
    echo "所有測試圖片已生成完成！"
    echo "檔案位置: $OUTPUT_DIR/"
    echo "包含以下檔案："
    echo "- size_1.9MB.png"
    echo "- size_2.0MB.png"
    echo "- size_2.1MB.png"
    echo "- resolution_1920x1080.png"
    echo "- resolution_3840x2160.png"
    echo "- resolution_800x600.png"
}

# 生成所有測試資料
generate_all() {
    generate_text
    echo
    generate_image
}

# 主循環
while true; do
    show_menu
    read -r choice
    
    case $choice in
        1)
            generate_all
            ;;
        2)
            echo -n "請輸入要轉換的圖片路徑: "
            read -r image_path
            scripts/convert_to_base64.sh "$image_path" "$OUTPUT_DIR"
            ;;
        3)
            echo -n "請輸入Base64檔案路徑: "
            read -r base64_path
            scripts/base64_to_file.sh "$base64_path" "$OUTPUT_DIR"
            ;;
        4)
            echo "退出程式"
            exit 0
            ;;
        *)
            echo "無效的選擇，請重試"
            ;;
    esac
    
    echo
    echo "按Enter鍵繼續..."
    read
done 