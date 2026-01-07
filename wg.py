import streamlit as st
import random
import time

# 1. 영단어 데이터 (중학영어 101~200 단어로 교체)
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        "middle": "한가운데", "store": "가게, 비축하다", "sound": "소리, 들리다, 건전한", "point": "요점, 점수, 가리키다", "land": "땅, 육지, 착륙하다", "clone": "복제생물, 복제하다", "turn": "돌다, 차례, 회전", "fly": "날다, 파리", "begin": "시작하다", "grow": "성장하다, 기르다, 되다", "believe": "믿다", "worry": "걱정시키다", "save": "구하다, 저축하다, 절약하다", "easy": "쉬운, 편한", "poor": "가난한, 불쌍한", "such": "그러한", "own": "자신의, 소유하다", "fast": "빨리, 단단히", "back": "뒤, 등", "always": "늘, 언제나", "history": "역사", "state": "국가, 상태", "soldier": "군인", "village": "마을", "office": "사무실", "island": "섬", "piece": "조각", "grade": "성적, 등급, 학년", "spring": "봄, 용수철", "rock": "바위, 흔들다", "line": "선, 줄을 서다", "cook": "요리사, 요리하다", "fall": "떨어지다, 가을", "exercise": "운동, 연습(하다)", "end": "끝(나다)", "front": "앞의", "second": "제2의, 초, 잠깐", "few": "소수의, 조금의", "both": "양쪽, 둘 다의", "happen": "일어나다, 우연히 ~하다", "leave": "떠나다, 내버려두다", "remember": "기억하다", "wear": "입다, 쓰다, 착용하다", "move": "움직이다, 감동시키다", "send": "보내다", "TRUE": "진짜의, 참된", "hot": "뜨거운, 매운", "early": "초기의, 일찍", "often": "종종, 자주", "sometimes": "때때로", "pet": "애완동물", "vegetable": "채소, 야채", "leaf": "잎", "forest": "숲", "area": "지역, 분야", "neighbor": "이웃", "art": "미술, 예술", "poem": "시", "subject": "과목, 주제", "bottle": "병", "machine": "기계", "fact": "사실", "rule": "규칙, 지배(하다)", "break": "깨뜨리다, 휴식", "check": "점검(하다)", "stay": "머무르다, ~인 채로 있다", "cold": "추운, 감기", "bring": "가져(데려)오다", "build": "짓다, 건축하다", "join": "가입하다", "lose": "잃다, 지다", "die": "죽다", "large": "큰, 넓은", "sick": "병든, 아픈", "busy": "바쁜, 번화한", "real": "진짜의, 현실의", "most": "대부분, 가장", "late": "늦은, 늦게", "together": "함께, 같이", "even": "~조차, 더욱~", "health": "건강", "holiday": "공휴일", "gift": "선물, 타고난 재능", "field": "들판, 경기장, 분야", "site": "장소, 현장, 웹사이트", "goal": "목표, 골", "effect": "영향, 결과, 효과", "sign": "표지, 신호, 서명하다", "report": "보고하다", "order": "순서, 질서, 명령(하다)", "experience": "경험(하다)", "result": "결과", "ride": "타다, 타기", "wish": "바라다, 소원", "half": "절반의", "past": "지나간, 과거", "carry": "가지고 가다, 나르다", "draw": "그리다, 끌다", "spend": "(시간, 돈을) 쓰다", "wait": "기다리다"
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.prev_idx = -1
    st.session_state.is_wrong = False

st.set_page_config(page_title="중학 영단어 퀴즈! (101-200)", page_icon="⭐")
st.title("🎡 매일 영단어 (101-200)")

# 게임 종료 화면
if st.session_state.current_idx >= len(st.session_state.word_list):
    st.balloons()
    st.header(f"🎊 완료! 최종 점수: {st.session_state.score} / {len(st.session_state.word_list)}")
    if st.button("다시 도전하기"):
        st.session_state.score = 0
        st.session_state.current_idx = 0
        st.session_state.prev_idx = -1
        random.shuffle(st.session_state.word_list)
        st.rerun()
    st.stop()

# 문제 설정
current_word = st.session_state.word_list[st.session_state.current_idx]
correct_mean = st.session_state.words_dict[current_word]

if st.session_state.prev_idx != st.session_state.current_idx:
    other_means = [v for k, v in st.session_state.words_dict.items() if v != correct_mean]
    options = random.sample(other_means, 3)
    options.append(correct_mean)
    random.shuffle(options)
    st.session_state.options = options
    st.session_state.prev_idx = st.session_state.current_idx
    st.session_state.is_wrong = False

# UI 표시
st.write(f"### 문제 {st.session_state.current_idx + 1} / {len(st.session_state.word_list)}")
st.progress((st.session_state.current_idx) / len(st.session_state.word_list))
st.info(f"다음 단어의 뜻은? \n\n ## **[ {current_word} ]**")

# 객관식 버튼 레이아웃
col1, col2 = st.columns(2)
for i, option in enumerate(st.session_state.options):
    with col1 if i % 2 == 0 else col2:
        if st.session_state.is_wrong:
            # 오답을 눌렀을 때의 보기 스타일
            if option == correct_mean:
                st.markdown(f"""
                    <div style="background-color: #ff4b4b; color: white; padding: 10px; border-radius: 5px; 
                    text-align: center; border: 2px solid #b22222; font-weight: bold; margin-bottom: 10px;">
                        🎯 {option} (정답)
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style="background-color: #f0f2f6; color: #a3a8b4; padding: 10px; border-radius: 5px; 
                    text-align: center; border: 1px solid #dcdde1; margin-bottom: 10px;">
                        {option}
                    </div>
                """, unsafe_allow_html=True)
        else:
            # 기본 게임 중 버튼 표시
            if st.button(option, key=f"btn_{st.session_state.current_idx}_{i}", use_container_width=True):
                if option == correct_mean:
                    st.session_state.score += 1
                    st.success("🎉 정답!")
                    time.sleep(0.5)
                    st.session_state.current_idx += 1
                    st.rerun()
                else:
                    st.session_state.is_wrong = True
                    st.error("❌ 틀렸습니다!")
                    st.rerun()

# 오답 상태일 때 2초 대기 후 다음으로 자동 전환
if st.session_state.is_wrong:
    time.sleep(2.0)
    st.session_state.current_idx += 1
    st.session_state.is_wrong = False
    st.rerun()

# 누적 점수 하단 표시
st.divider()
st.markdown(f"#### 📈 실시간 성적: **{st.session_state.score}** / {st.session_state.current_idx} (맞은 개수 / 진행 수)")
