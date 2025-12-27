import streamlit as st
import random


# 1. 단어 데이터 (예시 20개, 필요하면 100개 전체 넣으세요)
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
        "lot [lɒt]": "다량",
        "name [neɪm]": "이름",
        "hand [hænd]": "손",
        "place [pleɪs]": "장소",
        "practice [ˈpræktɪs]": "연습",
        "work [wɜːrk]": "일",
        "use [juːz]": "사용하다",
        "kind [kaɪnd]": "종류, 친절한",
        "have [hæv]": "가지다",
        "make [meɪk]": "만들다",
        "let [let]": "~하게 하다"
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 게임 상태
if 'idx' not in st.session_state:
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.answered = False

st.set_page_config("영단어 퀴즈", "⭐")
st.title("🎯 영단어 100제 퀴즈")

# 현재 문제
if st.session_state.idx < len(st.session_state.word_list):
    word = st.session_state.word_list[st.session_state.idx]
    answer = st.session_state.words_dict[word]

    # 객관식 선택지 준비
    if not st.session_state.answered:
        wrong = [v for v in st.session_state.words_dict.values() if v != answer]
        options = random.sample(wrong, 3) + [answer]
        random.shuffle(options)
        st.session_state.options = options

    st.write(f"### 문제 {st.session_state.idx + 1} / {len(st.session_state.word_list)}")

    # 단어 + 발음 버튼
    col_word, col_audio = st.columns([3,1])
    with col_word:
        st.info(f"**{word}** 의 뜻은?")
    with col_audio:
        if st.button("🔊 발음 듣기", key=f"audio_{st.session_state.idx}"):
            tts = gTTS(text=word.split()[0], lang='en')
            tts.save("temp.mp3")
            st.audio("temp.mp3")
            os.remove("temp.mp3")

    # 객관식 버튼 2x2
    cols = st.columns(2)
    for i, opt in enumerate(st.session_state.options):
        with cols[i % 2]:
            if st.button(opt, disabled=st.session_state.answered):
                st.session_state.answered = True
                # 정답/오답 표시
                if opt == answer:
                    st.success("🎉 정답!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ 틀렸어요! 정답: **{answer}**")
                # 선택한 단어 발음 재생
                tts = gTTS(text=word.split()[0], lang='en')
                tts.save("temp.mp3")
                st.audio("temp.mp3")
                os.remove("temp.mp3")
                st.rerun()

    # 다음 문제 버튼
    if st.session_state.answered:
        if st.button("다음 문제 ▶"):
            st.session_state.idx += 1
            st.session_state.answered = False
            st.rerun()

else:
    st.success("🎊 모든 문제 완료!")
    st.header(f"점수: {st.session_state.score} / {len(st.session_state.word_list)}")
    if st.button("다시 하기"):
        random.shuffle(st.session_state.word_list)
        st.session_state.idx = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()

# 사이드바 점수
st.sidebar.metric("현재 점수", st.session_state.score)

