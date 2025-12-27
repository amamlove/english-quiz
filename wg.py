import streamlit as st
import random
from gtts import gTTS
import os

# 1. 영단어 데이터 (100개)
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        # --- PAGE 1 (1~20) ---
        "life [laɪf]": "삶, 인생", "job [dʒɒb]": "일, 직업",
        "country [ˈkʌntri]": "나라, 시골", "earth [ɜːrθ]": "지구, 땅",
        "problem [ˈprɒbləm]": "문제", "way [weɪ]": "방법, 길",
        "language [ˈlæŋɡwɪdʒ]": "언어", "dialog [ˈdaɪəlɒɡ]": "대화",
        "story [ˈstɔːri]": "이야기, 층", "lot [lɒt]": "다량, 많이",
        "name [neɪm]": "이름(을 붙이다)", "hand [hænd]": "손, 건네주다",
        "place [pleɪs]": "장소, 두다", "practice [ˈpræktɪs]": "연습(하다)",
        "work [wɜːrk]": "일(하다)", "use [juːz]": "사용(하다)",
        "kind [kaɪnd]": "종류, 친절한", "have [hæv]": "가지고있다, 먹다",
        "make [meɪk]": "만들다", "let [let]": "~하게 하다, 허락하다",
        # PAGE 2~5 생략 가능 (위와 같은 형식으로 100개 모두 추가)
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 게임 상태 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.game_over = False
    st.session_state.prev_idx = -1
    st.session_state.options = []

# 3. 화면 UI 설정
st.set_page_config(page_title="영단어 퀴즈 왕!", page_icon="⭐")
st.title("🎡 객관식 영단어 퀴즈")

# 게임 진행 중
if st.session_state.current_idx < len(st.session_state.word_list):
    current_word = st.session_state.word_list[st.session_state.current_idx]
    correct_meaning = st.session_state.words_dict[current_word]

    # 객관식 옵션 생성
    if st.session_state.prev_idx != st.session_state.current_idx:
        other_meanings = [v for k, v in st.session_state.words_dict.items() if v != correct_meaning]
        options = random.sample(other_meanings, 3)
        options.append(correct_meaning)
        random.shuffle(options)
        st.session_state.options = options
        st.session_state.prev_idx = st.session_state.current_idx

    # 문제 표시
    st.write(f"### 문제 {st.session_state.current_idx + 1} / 100")
    st.progress((st.session_state.current_idx) / 100)

    # 단어 + 발음 버튼
    col_word, col_audio = st.columns([3,1])
    with col_word:
        st.info(f"다음 단어의 뜻은 무엇일까요?\n\n ## **[ {current_word} ]**")
    with col_audio:
        if st.button("🔊 발음 듣기", key=f"audio_{st.session_state.current_idx}"):
            tts = gTTS(text=current_word.split()[0], lang='en')
            tts.save("temp.mp3")
            st.audio("temp.mp3")
            os.remove("temp.mp3")

    # 객관식 버튼 2x2
    col1, col2 = st.columns(2)
    for i, option in enumerate(st.session_state.options):
        with col1 if i % 2 == 0 else col2:
            if st.button(option, key=f"btn_{i}", use_container_width=True):
                # 정답 확인
                if option == correct_meaning:
                    st.session_state.score += 1
                    st.success("🎉 정답이에요!")
                    st.balloons()
                else:
                    st.error(f"❌ 틀렸어요! 정답은 **{correct_meaning}** 입니다.")
                
                # 선택 후 단어 발음 재생
                tts = gTTS(text=current_word.split()[0], lang='en')
                tts.save("temp.mp3")
                st.audio("temp.mp3")
                os.remove("temp.mp3")

                # 다음 문제로 이동
                st.session_state.current_idx += 1
                st.rerun()

# 게임 종료
else:
    st.balloons()
    st.success("🎊 모든 문제를 다 풀었습니다!")
    st.header(f"나의 점수: {st.session_state.score} / 100 점")
    if st.button("다시 도전하기"):
        st.session_state.score = 0
        st.session_state.current_idx = 0
        random.shuffle(st.session_state.word_list)
        st.rerun()

# 사이드바 점수 표시
st.sidebar.metric("현재 점수", f"{st.session_state.score}점")
