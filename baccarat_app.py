
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="百家樂 AI 算牌神器 (進階版)", layout="wide")
st.title("🎲 百家樂 AI 算牌神器 (電腦本地版)")

# Session State 保存歷史局
if 'history' not in st.session_state:
    st.session_state['history'] = []

# 按鈕輸入局結果
col1, col2, col3 = st.columns(3)
if col1.button("莊 (B)"):
    st.session_state['history'].append("B")
if col2.button("閒 (P)"):
    st.session_state['history'].append("P")
if col3.button("和 (T)"):
    st.session_state['history'].append("T")

history = st.session_state['history']

# 顯示歷史局
st.subheader(f"歷史局 ({len(history)} 局)")
st.write(history)

# 統計表
def make_df(h):
    rows=[]
    for r in h:
        size="大" if r=="T" else "小"
        sd="雙" if r=="B" else "單" if r=="P" else "和"
        rows.append({"結果":r,"大小":size,"單雙":sd})
    return pd.DataFrame(rows)

df = make_df(history)
st.subheader("📊 統計表")
st.dataframe(df)

# 熱冷號
st.subheader("🔥 熱冷號")
c = df["結果"].value_counts()
fig1, ax1 = plt.subplots()
c.plot(kind="bar",color=["red","blue","green"],ax=ax1)
st.pyplot(fig1)

# 大小/單雙
st.subheader("📈 大小/單雙")
fig2, (a2,a3)=plt.subplots(1,2,figsize=(8,3))
df["大小"].value_counts().plot(kind="bar",color=["orange","purple"],ax=a2)
df["單雙"].value_counts().plot(kind="bar",color=["cyan","magenta"],ax=a3)
st.pyplot(fig2)

# 連莊/連閒
def streaks(h):
    s={"莊":[],"閒":[]}
    cur={"type":None,"count":0}
    for x in h:
        if x==cur["type"]:
            cur["count"]+=1
        else:
            if cur["type"]=="B": s["莊"].append(cur["count"])
            if cur["type"]=="P": s["閒"].append(cur["count"])
            cur={"type":x,"count":1}
    if cur["type"]=="B": s["莊"].append(cur["count"])
    if cur["type"]=="P": s["閒"].append(cur["count"])
    return s

st.subheader("🔗 連莊/連閒")
st.write(streaks(history))

# 路珠走勢
st.subheader("🎨 路珠走勢")
fig3, ax3 = plt.subplots(figsize=(10,2))
cm={"B":"red","P":"blue","T":"green"}
ax3.scatter(range(len(history)),[1]*len(history),c=[cm[x] for x in history],s=200)
st.pyplot(fig3)

# 下注建議
def advice(h):
    if len(h)<2:
        return "資料不足"
    if h[-1]==h[-2] and h[-1]!="T":
        return f"建議追 {h[-1]}"
    return "建議觀望"

st.subheader("💡下注建議")
st.write(advice(history))
