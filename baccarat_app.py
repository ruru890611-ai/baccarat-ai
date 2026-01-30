import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="百家樂 AI", layout="wide")
st.title("🎲 百家樂 AI 牌局分析器")

# 初始化歷史紀錄
if "history" not in st.session_state:
st.session_state.history = []

# 歷史牌局輸入
st.subheader("📥 輸入本局結果")
choice = st.radio("選擇本局結果", ["B", "P", "T"])
if st.button("加入歷史"):
st.session_state.history.append(choice)
st.success(f"已加入 {choice}")

# 顯示歷史牌局
st.subheader("📜 歷史牌局")
st.write(st.session_state.history)

# 計算累積勝率
history = st.session_state.history
total_games = len(history)
banker_win = history.count("B")
player_win = history.count("P")

if total_games > 0:
banker_rate = banker_win / total_games * 100
player_rate = player_win / total_games * 100
else:
banker_rate = player_rate = 0

st.subheader("📊 累積勝率")
st.write(f"莊勝率: {banker_rate:.1f}%")
st.write(f"閒勝率: {player_rate:.1f}%")

# 計算最近 N 局勝率
N = st.number_input("查看最近幾局勝率？", min_value=1, max_value=50, value=5)
recent_games = history[-N:]
recent_banker = recent_games.count("B")
recent_player = recent_games.count("P")
if len(recent_games) > 0:
st.write(f"最近{len(recent_games)}局莊勝率: {recent_banker/len(recent_games)*100:.1f}%")
st.write(f"最近{len(recent_games)}局閒勝率: {recent_player/len(recent_games)*100:.1f}%")

# 勝率趨勢圖
if total_games > 0:
banker_trend = [history[:i+1].count("B")/(i+1)*100 for i in range(total_games)]
player_trend = [history[:i+1].count("P")/(i+1)*100 for i in range(total_games)]

plt.figure(figsize=(8,4))
plt.plot(range(1, total_games+1), banker_trend, label="莊勝率", marker='o')
plt.plot(range(1, total_games+1), player_trend, label="閒勝率", marker='o')
plt.xlabel("局數")
plt.ylabel("勝率 (%)")
plt.title("莊 / 閒 勝率趨勢")
plt.ylim(0, 100)
plt.legend()
plt.grid(True)
st.pyplot(plt)

# 匯出歷史 CSV
st.subheader("💾 匯出歷史牌局")
if st.button("匯出 CSV"):
df = pd.DataFrame(history, columns=["Result"])
df.to_csv("baccarat_history.csv", index=False)
st.success("已匯出 baccarat_history.csv")
