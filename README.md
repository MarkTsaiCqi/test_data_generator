# Test Data Generator

這是一個用於生成測試數據的工具集，包括文本、圖像和音頻數據。

## 功能

### 1. 文本生成
- 使用 `generate_test_string.sh` 腳本生成測試文本
- 生成包含特殊字符的文本
- 生成 50 字符的隨機文本
- 生成 5000 字符的文章（使用預設文本文件）

### 2. 圖像生成
- 使用 `generate_test_images.sh` 腳本生成測試圖像
- 生成各種尺寸的圖像
- 生成包含特殊字符的圖像
- 生成大尺寸圖像

### 3. 音頻生成
- 使用 `generate_test_audio.sh` 腳本生成測試音頻
- 生成 MP3 格式的音頻文件
- 生成 WAV 格式的音頻文件

## 使用方法

### 文本生成
```bash
./generate_test_string.sh
```
這將在 `generated_data` 目錄下生成測試文本文件。

### 圖像生成
```bash
./generate_test_images.sh
```
這將在 `generated_data` 目錄下生成測試圖像文件。

### 音頻生成
```bash
./generate_test_audio.sh
```
這將在 `generated_data` 目錄下生成測試音頻文件。

## 目錄結構

```
.
├── text/                # 文本生成相關代碼和資源
│   ├── generator.py     # 文本生成器
│   └── ...             # 其他文本相關文件
├── image/               # 圖像生成相關代碼和資源
│   ├── generator.py     # 圖像生成器
│   └── ...             # 其他圖像相關文件
├── audio/               # 音頻生成相關代碼和資源
│   ├── generator.py     # 音頻生成器
│   └── ...             # 其他音頻相關文件
├── generated_data/      # 生成的測試數據
├── generate_test_string.sh    # 文本生成腳本
├── generate_test_images.sh    # 圖像生成腳本
└── generate_test_audio.sh     # 音頻生成腳本
```

## 注意事項

- 所有生成的測試數據都會保存在 `generated_data` 目錄下
- 確保有足夠的磁盤空間來存儲生成的測試數據
- 在運行腳本之前，確保已安裝所有必要的依賴項

## 圖片與 Base64 轉換工具

腳本 `scripts/image_converter.sh` 提供了圖片與 Base64 之間的轉換功能。

用法:
```bash
# 1. 圖片轉 Base64
./scripts/image_converter.sh image_to_base64 <圖片文件路徑> [輸出目錄]

# 2. Base64 轉圖片
./scripts/image_converter.sh base64_to_image <base64文件路徑> [輸出目錄]

# 3. b64_json 轉圖片 (例如處理來自某些 API 的 JSON 格式)
./scripts/image_converter.sh b64_json_to_image <json文件路徑> [輸出目錄]
#   示例:
./scripts/image_converter.sh b64_json_to_image scripts/example_image.json
```
- 輸出文件默認保存在腳本運行目錄下的 `generated_data` 子目錄中。

## 安裝說明

1. 複製這個repository：
```bash
git clone [repository_url]
cd test_data_generator
```

2. 創建並啟動虛擬環境：
```bash
# 創建虛擬環境
python -m venv venv

# 啟動虛擬環境
source venv/bin/activate
```

3. 安裝必要元件：
```bash
pip install -r requirements.txt
# 如果需要處理 b64_json，確保安裝了 jq
# sudo apt-get install jq  (Debian/Ubuntu)
# brew install jq        (macOS)
```

## 使用說明

1. 確保虛擬環境已啟動（終端機提示符前應顯示 (venv)）

2. 執行主生成腳本：
```bash
./generate_test_data.sh
```
   - 此腳本會自動生成預設的文本和圖片測試數據。

3. （可選）使用圖片/Base64 轉換腳本：
```bash
cd scripts
./image_converter.sh <操作類型> <輸入文件> [輸出目錄]
```

## 注意事項

- 每次打開新的終端機使用此工具時，都需要先執行 `source venv/bin/activate` 來啟動虛擬環境。
- 使用完畢後，可以執行 `deactivate` 來退出虛擬環境。
- 生成的測試檔案會保存在 `generated_data` 目錄下。

## 依賴套件

- Pillow：用於生成圖片
- numpy：用於生成audio（如果恢復該功能）
- pydub：用於audio處理（如果恢復該功能）
- faker：用於生成文本（如果恢復使用該腳本）
- jq (外部工具)：用於處理 JSON (b64_json 轉換需要) 
