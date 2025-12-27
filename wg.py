import streamlit as st
import random

# =====================
# 단어 데이터
# =====================
words_dict = {
    "life [laɪf]": "삶, 인생",
    "job [dʒɒb]": "일, 직업",
    "country [ˈkʌntri]": "나라, 시골",
    "earth [ɜːrθ]": "지구, 땅",
    "problem [ˈprɒbləm]": "문제",
    "way [weɪ]": "방법, 길",
    "language [ˈlæŋɡwɪdʒ]": "언어",
    "story [ˈstɔːri]": "이야기",
    "name [neɪm]": "이름",
    "place [pleɪs]": "장소",
    "practice [ˈpræktɪs]": "연습",
    "work [wɜːrk]": "일",
    "use [juːz]": "사용하다",
    "make [meɪk]": "만들다",
    "get [ɡet]": "얻다",
    "live [lɪv]": "살다",
    "important [ɪmˈpɔːrtnt]": "중요한",
    "learn [lɜːrn]": "배우다",
    "enjoy [ɪnˈdʒɔɪ]": "즐기다",
    "science [ˈsaɪəns]": "과학",
    "war [wɔːr]": "전쟁"
}

# =====================
# 상태
# =====================
if "words" not in st.session_state:
    st.session_state.words = list(words_dict.keys())
    random.shuffle(st.session_state.words)
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.answered = False

st.set_page_config("영단어 퀴즈", "🔊")
st.title("🎯 영단어 퀴즈")

# =====================
# 문제
# =====================
if st.session_state.idx < len(st.session_state.words):
    word = st.session_state.words[st.session_state.idx]
    answer = words_dict[word]
    pure = word.split(" ")[0]

    st.write(f"### 문제 {st.session_state.idx + 1}")
    st.info(word)

    # 🔊 브라우저 발음 버튼
    st.markdown(
        f"""
        <button onclick="
        var u = new SpeechSynthesisUtterance('{pure}');
        u.lang = 'en-US';
        speechSynthesis.speak(u);
        ">
        🔊 발음 듣기
        </button>
        """,
        unsafe_allow_html=True
    )

    options = random.sample(list(words_dict.values()), 3)
    if answer not in options:
        options[0] = answer
    random.shuffle(options)

    for opt in options:
        if st.button(opt):
            if opt == answer:
                st.success("정답!")
                st.session_state.score += 1
            else:
                st.error(f"틀림! 정답: {answer}")

            st.session_state.idx += 1
            st.rerun()

else:
    st.success("🎉 끝!")
    st.write(f"점수: {st.session_state.score}")
