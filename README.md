# 測試數據生成器

這是一個用於生成各種測試數據的工具，支持生成圖片、音頻、文本等多種格式的測試文件。

## 功能特點

### 圖片生成
- 支持多種格式：PNG、JPEG、GIF
- 支持多種圖片類型：隨機噪點、漸變、純色、棋盤格
- 支持指定圖片大小（用於測試上傳限制）
  - 大圖片：24MB、25MB、26MB
  - 小圖片：50KB、100KB、200KB

### 音頻生成
- 支持多種格式：MP3、WAV、FLAC、MIDI
- 支持多種音頻類型：白噪聲、正弦波、光劍音效
- 支持指定音頻大小（用於測試上傳限制）
  - 大音頻：24MB、25MB、26MB
  - 音頻品質可調（32kbps-320kbps）

### 文本生成
- 支持多種格式：TXT、JSON、Markdown、CSV、XML
- 支持生成不同長度的文本（50字符到5000字符）
- 支持生成包含特殊字符的測試文本
- 支持生成隨機事實文本

### 文件生成
- 支持生成各種格式的測試文件
- 支持生成不同大小的文件
- 支持生成包含特殊字符的文件名

## 使用方法

### 環境設置
1. 創建並激活虛擬環境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

2. 安裝依賴：
```bash
pip install -r requirements.txt
```

### 生成大圖片（用於測試上傳限制）
```bash
./generate_test_bigImage.sh
```
這將生成三個圖片文件：
- `size_24mb.jpg`（約24MB）
- `size_25mb.jpg`（約25MB）
- `size_26mb.jpg`（約26MB）

### 生成小圖片（用於測試上傳限制）
```bash
./generate_test_smallImage.sh
```
這將生成三個圖片文件：
- `size_50kb.jpg`（約50KB）
- `size_100kb.jpg`（約100KB）
- `size_200kb.jpg`（約200KB）

### 生成大音頻（用於測試上傳限制）
```bash
./generate_test_bigAudio.sh
```
這將生成三個音頻文件：
- `size_24mb.mp3`（約24MB）
- `size_25mb.mp3`（約25MB）
- `size_26mb.mp3`（約26MB）

### 生成測試音頻
```bash
./generate_test_audio.sh
```
這將生成多種測試音頻：
- 白噪聲（`white_noise.mp3`）
- 不同頻率的正弦波（`sine_220hz.mp3`、`sine_440hz.mp3`、`sine_880hz.mp3`）
- 光劍音效（`lightsaber.wav`、`lightsaber.mp3`、`lightsaber.flac`）
- MIDI 文件（`test_midi.mid`）

### 生成測試文本
```bash
./generate_test_text.sh
```
這將生成多種格式的測試文本文件。

### 生成測試文件
```bash
./generate_test_files.sh
```
這將生成各種格式的測試文件。

## 項目結構
```
test_data_generator/
├── audio/                # 音頻生成相關代碼
│   └── generator.py      # 音頻生成器
├── image/                # 圖片生成相關代碼
│   └── generator.py      # 圖片生成器
├── text/                 # 文本生成相關代碼
│   └── generator.py      # 文本生成器
├── generated_data/       # 生成的測試數據
├── requirements.txt      # 項目依賴
└── README.md            # 項目說明文檔
```

## 依賴
- Python 3.8+
- Pillow (PIL)
- numpy
- pydub
- soundfile
- mido
- python-docx
- openpyxl
- reportlab
- tqdm

## 注意事項
1. 生成的測試數據僅用於測試目的
2. 使用前請確保已安裝所有依賴
3. 每次使用新終端時，需要先執行 `source venv/bin/activate` 啟動虛擬環境
4. 使用完畢後，可以執行 `deactivate` 退出虛擬環境
