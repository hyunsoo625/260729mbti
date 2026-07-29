import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="청소년 MBTI & AI 진로 탐색 센터",
    page_icon="🎓",
    layout="centered",
)

# 메인 타이틀 및 소개 문구
st.title("🎓 MBTI 데이터 분석 & AI 진로 탐색 센터")
st.markdown("""
### 반가워요! MBTI 통계 분석과 AI 상담이 결합된 진로 탐색소입니다. 🌱

왼쪽 **사이드바 메뉴**에서 이동하고 싶은 페이지를 선택해 보세요!

---

### 📌 주요 기능 안내

1. 📊 **우리나라 MBTI 비율**: 대한민국 청소년 및 성인의 MBTI 성향 분포를 시각적 그래프로 확인
2. 🌍 **나라별 MBTI 분포도**: 한국, 미국, 일본, 독일 등 세계 여러 국가의 MBTI 차이 비교
3. 💡 **AI 쌤의 맞춤 진로 추천**: 내 MBTI와 관심 과목/활동을 입력하고 1:1 맞춤형 진로 분석 받기
""")

st.divider()

# 사이드바 Gemini API Key 설정 (전체 페이지 공유 세션)
st.sidebar.header("🔑 AI 쌤 연동 설정")
default_key = st.secrets.get(
    "GEMINI_API_KEY", st.session_state.get("api_key", "")
)

api_key = st.sidebar.text_input(
    "Gemini API Key 입력",
    value=default_key,
    type="password",
    placeholder="AI Studio 키를 입력하세요",
    help="Google AI Studio(aistudio.google.com)에서 발급받은 키를 입력하면 'AI 맞춤 진로 추천' 페이지가 활성화됩니다.",
)

# 세션 상태에 저장하여 다른 페이지(3번 페이지 등)에서도 공유
st.session_state["api_key"] = api_key

if api_key:
  st.sidebar.success("✅ AI 추천 엔진 연결 완료!")
else:
  st.sidebar.warning("⚠️ API 키를 입력하면 AI 진로 추천 기능이 작동합니다.")

st.info(
    "💡 **사용 팁**: 메인 화면 사이드바에 API 키를 한 번만 등록해 두면, 페이지를"
    " 이동해도 키가 유지되어 편리하게 사용할 수 있습니다!"
)

st.caption("© 청소년 MBTI & AI 진로 탐색 센터 🎈")