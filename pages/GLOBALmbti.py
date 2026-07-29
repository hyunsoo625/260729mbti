import pandas as pd
import streamlit as st

st.set_page_config(page_title="나라별 MBTI 분포도", page_icon="🌍", layout="centered")

st.title("🌍 나라별 MBTI 분포도 비교")
st.caption("세계 여러 나라 사람들의 MBTI 성향 비율에는 어떤 차이가 있을까요?")

# 나라별 MBTI 데이터 세트
global_mbti_data = {
    "MBTI": [
        "ISTJ",
        "ISFJ",
        "INFJ",
        "INTJ",
        "ISTP",
        "ISFP",
        "INFP",
        "INTP",
        "ESTP",
        "ESFP",
        "ENFP",
        "ENTP",
        "ESTJ",
        "ESFJ",
        "ENFJ",
        "ENTJ",
    ],
    "한국 🇰🇷": [
        11.8,
        8.4,
        6.2,
        4.3,
        4.7,
        8.6,
        13.3,
        6.3,
        4.4,
        5.3,
        12.6,
        5.0,
        8.2,
        5.4,
        3.5,
        2.0,
    ],
    "미국 🇺🇸": [
        11.6,
        13.8,
        1.5,
        2.1,
        5.4,
        8.8,
        4.4,
        3.3,
        4.3,
        8.5,
        8.1,
        3.2,
        8.7,
        12.3,
        2.5,
        1.8,
    ],
    "일본 🇯🇵": [
        3.6,
        6.8,
        6.0,
        3.7,
        2.9,
        6.7,
        13.0,
        7.2,
        2.6,
        4.9,
        13.8,
        5.2,
        3.4,
        6.7,
        5.6,
        3.6,
    ],
    "독일 🇩🇪": [
        13.0,
        9.5,
        3.2,
        5.8,
        7.1,
        6.2,
        7.5,
        8.1,
        4.5,
        4.0,
        7.8,
        5.5,
        10.2,
        6.0,
        4.0,
        3.6,
    ],
}

df_global = pd.DataFrame(global_mbti_data)

# 1. 국가 선택 박스
selected_country = st.selectbox(
    "조회할 국가를 선택해 보세요:",
    ["한국 🇰🇷", "미국 🇺🇸", "일본 🇯🇵", "독일 🇩🇪"],
    index=0,
)

# 선택한 국가의 차트
st.subheader(f"📊 {selected_country} MBTI 분포 비율")
chart_data = df_global.set_index("MBTI")[selected_country]
st.bar_chart(chart_data, height=320)

st.divider()

# 2. 두 국가 비교 기능
st.subheader("🔍 국가 간 비교하기")
countries_to_compare = st.multiselect(
    "비교할 국가를 2개 이상 선택하세요:",
    ["한국 🇰🇷", "미국 🇺🇸", "일본 🇯🇵", "독일 🇩🇪"],
    default=["한국 🇰🇷", "미국 🇺🇸"],
)

if countries_to_compare:
  compare_df = df_global.set_index("MBTI")[countries_to_compare]
  st.bar_chart(compare_df, height=360)

st.markdown("""
> **💡 흥미로운 국가별 문화 포인트:**
> * **한국 & 일본**: INFP, ENFP 등 감성적이고 자유로운 생각을 가진 **N/F 성향**이 젊은 층에서 강세를 보입니다.
> * **미국**: ISFJ, ESFJ, ISTJ 등 체계적이고 실용적인 **S/J 성향**의 비중이 높게 나타납니다.
> * **독일**: ISTJ, ESTJ, INTP 등 논리와 규율을 중시하는 **T(사고형)** 비율이 상대적으로 높습니다.
""")
