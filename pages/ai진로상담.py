import json
import urllib.request
import streamlit as st

st.set_page_config(page_title="AI 맞춤 진로 추천", page_icon="💡", layout="centered")


# Gemini API 호출 함수
def get_ai_recommendation(api_key, mbti, interest, favorite_act):
  url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
  headers = {"Content-Type": "application/json"}

  prompt = f"""
    너는 청소년 전문 진로 상담가 쌤이야.
    다음 학생의 정보를 바탕으로 따뜻하고 구체적인 맞춤형 진로 추천서를 작성해줘.

    [학생 정보]
    - MBTI: {mbti}
    - 관심 과목 및 분야: {interest}
    - 평소 좋아하는 활동: {favorite_act}

    [답변 양식]
    1. 🌟 **학생의 강점 분석**: MBTI와 관심사를 결합한 멋진 장점 2가지
    2. 🎯 **추천 맞춤 직업 TOP 3**: 직업명과 그 직업을 추천하는 구체적인 이유
    3. 🎓 **추천 진학 학과 / 계열**: 대학이나 고등학교 선택 시 도움이 될 학과 추천
    4. 💌 **상담가 쌤의 응원 한마디**: 희망과 용기를 주는 메시지

    친절하고 다정한 말투로 이모지를 가득 넣어서 가독성 있게 작성해줘!
    """

  payload = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}

  try:
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"), headers=headers
    )
    with urllib.request.urlopen(req, timeout=25) as response:
      result = json.loads(response.read().decode("utf-8"))
      return result["candidates"][0]["content"]["parts"][0]["text"]
  except Exception as e:
    return f"❌ 분석 중 오류가 발생했습니다: {str(e)}\n\n사이드바에 API 키가 올바르게 입력되었는지 확인해 주세요!"


st.title("💡 AI 쌤의 1:1 맞춤 진로 추천")
st.write(
    "여러분의 MBTI와 관심사를 적어주시면, AI 상담가 쌤이 꼭 맞는 진로와 직업을"
    " 분석해 드릴게요! 🌱"
)

# API 키 가져오기 (세션 또는 Secrets)
api_key = st.session_state.get(
    "api_key", st.secrets.get("GEMINI_API_KEY", "")
)

with st.sidebar:
  st.header("🔑 AI 연동 설정")
  api_key_input = st.text_input(
      "Gemini API Key",
      value=api_key,
      type="password",
      placeholder="API 키 입력",
  )
  if api_key_input != api_key:
    st.session_state["api_key"] = api_key_input
    api_key = api_key_input

  if api_key:
    st.success("✅ AI 추천 엔진 작동 준비 완료")
  else:
    st.warning("⚠️ API 키를 입력하면 AI 분석이 동작합니다.")

# 1. 학생 입력 폼
with st.form("recommendation_form"):
  st.subheader("📝 나의 진로 프로필 입력")

  col1, col2 = st.columns(2)
  with col1:
    user_mbti = st.selectbox(
        "1. 나의 MBTI",
        [
            "INFP",
            "ENFP",
            "INFJ",
            "INTJ",
            "INTP",
            "ISFP",
            "ISFJ",
            "ISTJ",
            "ISTP",
            "ENFJ",
            "ENTJ",
            "ENTP",
            "ESFP",
            "ESFJ",
            "ESTJ",
            "ESTP",
        ],
    )
  with col2:
    user_interest = st.text_input(
        "2. 관심 과목/분야",
        placeholder="예: 생물, 로봇, 미술, 미디어, 심리학 등",
    )

  user_activity = st.text_area(
      "3. 평소 즐겨하거나 보람을 느끼는 활동",
      placeholder="예: 만들기/실험하기, 친구 고민 들어주기, 그림 그리기, 게임 분석하기 등",
  )

  submit_btn = st.form_submit_button("🚀 AI 쌤에게 맞춤 진로 분석 받기")

# 2. 결과 출력
if submit_btn:
  if not user_interest or not user_activity:
    st.warning("⚠️ 관심 분야와 좋아하는 활동을 간단히 적어주세요!")
  elif not api_key:
    st.error(
        "🔑 사이드바에 Google AI Studio API 키를 입력해야 분석이 가능합니다!"
    )
  else:
    with st.spinner("AI 상담가 쌤이 학생의 프로필을 정성껏 분석 중입니다... 💭"):
      result = get_ai_recommendation(
          api_key, user_mbti, user_interest, user_activity
      )
      st.markdown("---")
      st.write(result)