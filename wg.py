import streamlit as st
import random

# =====================
# 1. 단어 데이터 (100단어)
# =====================
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        "life [laɪf]": "삶, 인생",
        "job [dʒɒb]": "일, 직업",
        "country [ˈkʌntri]": "나라, 시골",
        "earth [ɜːrθ]": "지구, 땅",
        "problem [ˈprɒbləm]": "문제",
        "way [weɪ]": "방법, 길",
        "language [ˈlæŋɡwɪdʒ]": "언어",
        "dialog [ˈdaɪəlɒɡ]": "대화",
        "story [ˈstɔːri]": "이야기",
        "lot [lɒt]": "많이",
        "name [neɪm]": "이름",
        "hand [hænd]": "손",
        "place [pleɪs]": "장소",
        "practice [ˈpræktɪs]": "연습",
        "work [wɜːrk]": "일",
        "use [juːz]": "사용하다",
        "kind [kaɪnd]": "친절한",
        "have [hæv]": "가지다",
        "make [meɪk]": "만들다",
        "let [let]": "~하게 하다",
        "get [ɡet]": "얻다",
        "take [teɪk]": "데려가다",
        "live [lɪv]": "살다",
        "different [ˈdɪfrənt]": "다른",
        "important [ɪmˈpɔːrtnt]": "중요한",
        "other [ˈʌðə(r)]": "다른",
        "right [raɪt]": "옳은",
        "sure [ʃʊə(r)]": "확신하는",
        "too [tuː]": "너무",
        "well [wel]": "잘",
        "person [ˈpɜːrsn]": "사람",
        "movie [ˈmuːvi]": "영화",
        "example [ɪɡˈzæmpl]": "예",
        "plan [plæn]": "계획",
        "try [traɪ]": "시도하다",
        "future [ˈfjuːtʃə(r)]": "미래",
        "learn [lɜːrn]": "배우다",
        "hard [hɑːrd]": "어려운",
        "enjoy [ɪnˈdʒɔɪ]": "즐기다",
        "science [ˈsaɪəns]": "과학",
        "war [wɔːr]": "전쟁"
    }

    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# =====================
# 상태 초기화
# =====================
if 'idx' not in st.session_state:
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.result = None
    st.session_state.correct_answer = None

st.set_page_config("영단어 퀴즈", "🔊")
st.title("🎯 영단어 퀴즈")

# =====================
# 게임 진행
# =====================
if st.session_state.idx < len(st.session_state.word_list):
    word = st.session_state.word_list[st.session_state.idx]
    answer = st.session_state.words_dict[word]
    pure_word = word.split(" ")[0]

    st.write(f"### 문제 {st.session_state.idx + 1} / 100")
    st.info(f"**{word}** 의 뜻은?")

    # 🔊 발음 버튼 (브라우저 TTS)
    st.markdown(
        f"""
        <button onclick="
        var msg = new SpeechSynthesisUtterance('{pure_word}');
        msg.lang = 'en-US';
        speechSynthesis.speak(msg);
        ">
        🔊 발음 듣기
        </button>
        """,
        unsafe_allow_html=True
    )

    # 보기 생성
    if not st.session_state.answered:
        wrong = [v for v in st.session_state.words_dict.values() if v != answer]
        options = random.sample(wrong, 3) + [answer]
        random.shuffle(options)
        st.session_state.options = options

    cols = st.columns(2)
    for i, opt in enumerate(st.session_state.options):
        with cols[i % 2]:
            if st.button(opt, disabled=st.session_state.answered, key=f"opt_{i}"):
                st.session_state.answered = True
                st.session_state.correct_answer = answer
                if opt == answer:
                    st.session_state.result = "correct"
                    st.session_state.score += 1
                else:
                    st.session_state.result = "wrong"
                st.rerun()

    # 결과 표시
    if st.session_state.answered:
        if st.session_state.result == "correct":
            st.success("🎉 정답입니다!")
        else:
            st.error(f"❌ 틀렸어요! 정답은 **{st.session_state.correct_answer}** 입니다.")

        if st.button("다음 문제 ▶"):
            st.session_state.idx += 1
            st.session_state.answered = False
            st.session_state.result = None
            st.session_state.correct_answer = None
            st.rerun()

else:
    st.success("🎊 모든 문제 완료!")
    st.header(f"최종 점수: {st.session_state.score} / 100")

st.sidebar.metric("현재 점수", st.session_state.score)
