import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="우리나라 MBTI 비율", page_icon="📊", layout="centered"
)

st.title("📊 우리나라 MBTI 성향 비율")
st.caption(
    "대한민국 청소년 및 성인들의 MBTI 분포 현황을 그래프로 알아봐요! 🇰🇷"
)

# 1. 한국 MBTI 데이터 (비율 %)
korea_mbti_data = {
    "MBTI": [
        "INFP",
        "ENFP",
        "ISTJ",
        "ISFP",
        "ISFJ",
        "ESTJ",
        "INTP",
        "INFJ",
        "ESFP",
        "ESFJ",
        "ENTP",
        "ISTP",
        "INTJ",
        "ESTP",
        "ENFJ",
        "ENTJ",
    ],
    "비율(%)": [
        13.3,
        12.6,
        11.8,
        8.6,
        8.4,
        8.2,
        6.3,
        6.2,
        5.3,
        5.4,
        5.0,
        4.7,
        4.3,
        4.4,
        3.5,
        2.0,
    ],
}

df = pd.DataFrame(korea_mbti_data)

# 2. 정렬 옵션 선택
col1, col2 = st.columns([2, 1])
with col1:
  st.subheader("📈 MBTI 분포 막대그래프")
with col2:
  sort_order = st.selectbox(
      "정렬 방식", ["비율 높은 순", "MBTI 알파벳순"], index=0
  )

if sort_order == "비율 높은 순":
  df_sorted = df.sort_values(by="비율(%)", ascending=False)
else:
  df_sorted = df.sort_values(by="MBTI")

# 3. 막대그래프 출력 (Streamlit 내장 차트 사용 - 한글 폰트 깨짐 없음)
st.bar_chart(data=df_sorted.set_index("MBTI")["비율(%)"], height=350)

st.divider()

# 4. 요약 및 데이터 표
st.markdown("### 💡 한국인 MBTI의 주요 특징")
st.info("""
* **1위 INFP (13.3%) & 2위 ENFP (12.6%)**: 대한민국 청소년 및 젊은 층에서 감성적이고 창의적인 **F(감정형)** 및 **N(직관형)** 비율이 매우 높게 나타납니다.
* **3위 ISTJ (11.8%)**: 원칙과 성실함을 중시하는 전통적인 내향 실행가 유형도 큰 비중을 차지합니다.
* **상대적 희귀 유형**: **ENTJ(2.0%)**, **ENFJ(3.5%)** 등 외향 리더형 유형은 전체 비중 중 비교적 희소한 편입니다.
""")

with st.expander("📋 전체 데이터 상세표 보기"):
  st.dataframe(
      df_sorted.reset_index(drop=True), use_container_width=True
  )