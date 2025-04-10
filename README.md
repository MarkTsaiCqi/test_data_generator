# 測試數據生成器

這是一個用於生成各種測試數據的工具，支持生成圖片、音頻、文本和各種文件格式。

## 功能特點

### 圖片生成
- 支持多種圖片格式（PNG、JPEG、GIF）
- 可生成不同類型的圖片（隨機、漸變、純色、棋盤格）
- 支持不同尺寸和解析度
- 支持生成大圖片（最大 4000x3000）
- 支持生成 GIF 動畫
- 支持生成指定大小的圖片（用於測試上傳限制）

### 音頻生成
- 支持多種音頻格式（WAV、MP3、FLAC、MIDI）
- 可生成不同類型的音頻（白噪聲、正弦波、光劍音效）
- 支持不同頻率和持續時間

### 文本生成
- 支持多種文本格式（TXT、JSON、Markdown、CSV、XML）
- 可生成不同類型的文本（隨機、Lorem Ipsum、代碼）
- 支持不同長度和複雜度
- 可生成不同長度的文本（50字符、5000字符）
- 可生成包含特殊字符的測試文本
- 可生成隨機事實文本

### 文件生成
- 支持多種文件格式（Excel、Word、PDF）
- 可生成不同類型的文件（表格、文檔、報告）
- 支持不同大小和複雜度

## 使用方法

### 啟動虛擬環境
每次打開新的終端機使用此工具時，都需要先執行：
```bash
source venv/bin/activate
```
使用完畢後，可以執行：
```bash
deactivate
```
來退出虛擬環境。

### 安裝依賴
```bash
pip install -r requirements.txt
```

### 生成所有測試數據
```bash
./generate_test_files.sh
```

### 生成圖片測試數據
```bash
./generate_test_images.sh
```

### 生成大圖片測試數據（用於測試上傳限制）
```bash
./generate_test_bigImages.sh
```
這會生成三種大小的圖片：
- 19MB（應該可以上傳）
- 20MB（剛好可以上傳）
- 21MB（應該不能上傳）

### 生成小圖片測試數據（用於測試頭像上傳限制）
```bash
./generate_test_smallImages.sh
```
這會生成三種大小的圖片：
- 1900KB（應該可以上傳）
- 2048KB（剛好可以上傳）
- 2100KB（應該不能上傳）

### 生成音頻測試數據
```bash
./generate_test_audio.sh
```

### 生成文本測試數據
```bash
./generate_test_text.sh
```

## 項目結構
```
.
├── audio/                # 音頻生成相關代碼
├── formats/              # 文件格式生成相關代碼
├── image/                # 圖片生成相關代碼
├── imageSize/            # 圖片大小測試相關代碼
├── text/                 # 文本生成相關代碼
├── generated_data/       # 生成的測試數據
├── generate_test_files.sh    # 生成所有測試數據的腳本
├── generate_test_images.sh   # 生成圖片測試數據的腳本
├── generate_test_bigImages.sh # 生成大圖片測試數據的腳本
├── generate_test_smallImages.sh # 生成小圖片測試數據的腳本
├── generate_test_audio.sh    # 生成音頻測試數據的腳本
├── generate_test_text.sh     # 生成文本測試數據的腳本
├── main.py               # 主程序
├── README.md             # 項目說明文檔
└── requirements.txt      # 項目依賴
```

## 依賴項
- Pillow：圖片處理
- numpy：數組處理
- pydub：音頻處理
- python-docx：Word 文檔處理
- openpyxl：Excel 文件處理
- reportlab：PDF 文件處理
- midiutil：MIDI 文件處理
- pydub：音頻處理

## 注意事項
- 生成的測試數據保存在 `generated_data` 目錄中
- 部分功能需要安裝額外的系統依賴（如音頻處理需要 ffmpeg）
- 生成大文件可能需要較長時間
