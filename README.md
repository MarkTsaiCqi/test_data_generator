# 測試數據生成器

這是一個用於生成各種測試數據的工具，支持生成圖片、音頻、文本和各種文件格式。

## 功能特點

### 圖片生成
- 支持多種格式：PNG、JPEG、GIF
- 支持多種圖片類型：隨機、漸變、純色、棋盤格
- 可指定圖片大小和分辨率
- 支持生成特定大小的圖片（用於測試上傳限制）

### 音頻生成
- 支持多種格式：MP3、WAV、FLAC、MIDI
- 可生成不同類型的音頻：正弦波、白噪聲、光劍音效
- 支持生成特定大小的音頻文件

### 文本生成
- 支持多種格式：TXT、JSON、Markdown、CSV、XML
- 可生成不同類型的文本：隨機、Lorem Ipsum、代碼
- 支持生成不同長度和複雜度的文本
- 可生成包含特殊字符的測試文本
- 可生成隨機事實文本

### 文件生成
- 支持多種文件格式（詳見 [SUPPORTED_FORMATS.md](SUPPORTED_FORMATS.md)）
- 可生成特定大小的文件

## 使用方法

1. 激活虛擬環境：
```bash
source venv/bin/activate
```

2. 安裝依賴：
```bash
pip install -r requirements.txt
```

3. 生成圖片：
```bash
# 生成大圖片（用於測試上傳限制）
./generate_test_bigImage.sh

# 生成小圖片（KB級別）
./generate_test_smallImage.sh
```

4. 生成音頻：
```bash
# 生成大音頻文件（用於測試上傳限制）
./generate_test_bigAudio.sh

# 生成普通音頻文件
./generate_test_audio.sh
```

5. 生成文本：
```bash
./generate_test_text.sh
```

6. 生成各種文件：
```bash
./generate_test_files.sh
```

7. 退出虛擬環境：
```bash
deactivate
```

## 項目結構
```
.
├── audio/                # 音頻生成相關代碼
├── file/                 # 文件生成相關代碼
├── image/                # 圖片生成相關代碼
├── text/                 # 文本生成相關代碼
├── generated_data/       # 生成的測試數據
├── requirements.txt      # 項目依賴
├── README.md            # 項目說明文檔
└── SUPPORTED_FORMATS.md  # 支持的文件格式說明
```

## 依賴
- Python 3.x
- Pillow (圖片處理)
- numpy (數組處理)
- pydub (音頻處理)
- python-docx (Word文檔處理)
- reportlab (PDF生成)
- python-pptx (PPT生成)
- pandas (Excel文件處理)
- openpyxl (Excel文件處理)

## 注意事項
1. 生成的測試數據僅用於測試目的，不應在生產環境中使用
2. 大文件生成可能需要較長時間，請耐心等待
3. 每次打開新的終端時，都需要執行 `source venv/bin/activate` 來啟動虛擬環境
4. 使用完畢後，可以執行 `deactivate` 來退出虛擬環境
