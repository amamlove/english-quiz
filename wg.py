import streamlit as st
import random

# 1. 영단어 데이터 (30개)
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        "늦은": "late", "졸린": "sleepy", "우승자,승리자": "winner", "운이 좋은": "lucky", "머무르다": "stay",
        "화난": "angry", "부유한": "rich", "방문하다": "visit", "공주": "princess", "따뜻한": "warm",
        "일본의": "japanese", "사무실": "office", "저렴한,싼": "cheap", "~을 비웃다": "laugh at", "공정한": "fair",
        "겁먹은": "scared", "첼로": "cello", "바라다": "wish", "배우다": "learn", "~로 덮다": "cover",
        "돌다": "turn", "끝나다,끝내다": "finish", "지나가다": "pass", "신발": "shoes", "엄마": "mother",
        "아빠": "father", "친구": "friend", "아기": "baby", "선생님": "teacher", "의사": "doctor"
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 게임 상태 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.game_over = False

# 3. 화면 UI 설정
st.set_page_config(page_title="영단어 퀴즈 왕!", page_icon="⭐")
st.title("🎡 객관식 영단어 퀴즈")

# 게임이 진행 중일 때
if st.session_state.current_idx < len(st.session_state.word_list):
    current_ko = st.session_state.word_list[st.session_state.current_idx]
    correct_en = st.session_state.words_dict[current_ko]

    # 오답 보기 생성 (현재 정답 제외하고 랜덤하게 3개 선택)
    if 'options' not in st.session_state or st.session_state.prev_idx != st.session_state.current_idx:
        other_words = [v for k, v in st.session_state.words_dict.items() if v != correct_en]
        options = random.sample(other_words, 3)
        options.append(correct_en)
        random.shuffle(options)
        st.session_state.options = options
        st.session_state.prev_idx = st.session_state.current_idx

    # 진행도와 문제 표시
    st.write(f"### 문제 {st.session_state.current_idx + 1} / 30")
    st.progress((st.session_state.current_idx) / 30)
    st.info(f"다음 단어의 뜻은 무엇일까요? \n\n ## **[ {current_ko} ]**")

    # 객관식 버튼 배치 (2x2 레이아웃)
    col1, col2 = st.columns(2)
    for i, option in enumerate(st.session_state.options):
        with col1 if i % 2 == 0 else col2:
            if st.button(option, key=f"btn_{i}", use_container_width=True):
                if option == correct_en:
                    st.session_state.score += 1
                    st.success("🎉 정답이에요!")
                    st.balloons()
                else:
                    st.error(f"❌ 틀렸어요! 정답은 **{correct_en}** 입니다.")
                
                # 다음 문제로 넘어가기 위한 상태 업데이트
                st.session_state.current_idx += 1
                st.rerun()

else:
    # 게임 종료 결과 화면
    st.balloons()
    st.success("🎊 모든 문제를 다 풀었습니다!")
    st.header(f"나의 점수: {st.session_state.score} / 30 점")
    
    if st.button("다시 도전하기"):
        st.session_state.score = 0
        st.session_state.current_idx = 0
        random.shuffle(st.session_state.word_list)
        st.rerun()

# 사이드바 점수 표시

st.sidebar.metric("현재 점수", f"{st.session_state.score}점")
