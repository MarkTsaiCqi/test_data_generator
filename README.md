# 測試資料生成工具

這是一個用於生成各種測試資料的工具，包括文字、圖片和audio檔案。

## 功能特點

- 生成不同長度的文本文件（1KB, 10KB, 100KB, 1MB）
- 生成不同大小（基於 Python 腳本預設）的圖片，並嵌入文字標籤
- （可選）生成不同長度的audio檔案（需要恢復 audio 目錄及相關代碼）

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
