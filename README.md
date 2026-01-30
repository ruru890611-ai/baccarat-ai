
# 百家樂 AI 進階版 (電腦本地版)

## Step 1：安裝 Python
- 確認 Python 3.9+ 已安裝
- 在終端機檢查版本：python --version

## Step 2：安裝套件
1. 解壓縮本壓縮包
2. 打開 Terminal / CMD
3. 進入資料夾：cd 路徑到解壓資料夾
4. 安裝套件：pip install -r requirements.txt

## Step 3：啟動程式
在資料夾終端機輸入：
streamlit run baccarat_app.py

程式會自動打開瀏覽器頁面
- 點按「莊 (B)」「閒 (P)」「和 (T)」按鈕輸入局結果
- 自動累計歷史局
- 即時生成統計表、圖表、連莊/連閒、路珠走勢圖、下注建議
