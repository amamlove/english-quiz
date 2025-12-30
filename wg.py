import streamlit as st
import random
import time

# 1. 영단어 데이터 (100개)
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        "life [laɪf]": "삶, 인생", "job [dʒɒb]": "일, 직업", "country [ˈkʌntri]": "나라, 시골",
        "earth [ɜːrθ]": "지구, 땅", "problem [ˈprɒbləm]": "문제", "way [weɪ]": "방법, 길",
        "language [ˈlæŋɡwɪdʒ]": "언어", "dialog [ˈdaɪəlɒɡ]": "대화", "story [ˈstɔːri]": "이야기",
        "lot [lɒt]": "다량", "name [neɪm]": "이름", "hand [hænd]": "손",
        "place [pleɪs]": "장소", "practice [ˈpræktɪs]": "연습", "work [wɜːrk]": "일",
        "use [juːz]": "사용하다", "kind [kaɪnd]": "종류, 친절한", "have [hæv]": "가지다",
        "make [meɪk]": "만들다", "let [let]": "~하게 하다", "get [ɡet]": "얻다",
        "take [teɪk]": "데려가다", "live [lɪv]": "살다", "different [ˈdɪfrənt]": "다른",
        "important [ɪmˈpɔːrtnt]": "중요한", "other [ˈʌðə(r)]": "다른", "right [raɪt]": "옳은",
        "sure [ʃʊə(r)]": "확신하는", "too [tuː]": "너무", "well [wel]": "잘",
        "person [ˈpɜːrsn]": "사람", "clothes [kləʊðz]": "옷", "movie [ˈmuːvi]": "영화",
        "activity [ækˈtɪvəti]": "활동", "example [ɪɡˈzæmpl]": "예", "letter [ˈletə(r)]": "편지",
        "fire [ˈfaɪə(r)]": "불", "minute [ˈmɪnɪt]": "분", "part [pɑːrt]": "부분",
        "plan [plæn]": "계획", "plant [plænt]": "식물", "park [pɑːrk]": "공원",
        "call [kɔːl]": "부르다", "try [traɪ]": "시도하다", "need [niːd]": "필요하다",
        "fun [fʌn]": "재미", "future [ˈfjuːtʃə(r)]": "미래", "keep [kiːp]": "유지하다",
        "listen [ˈlɪsn]": "듣다", "find [faɪnd]": "찾다", "learn [lɜːrn]": "배우다",
        "mean [miːn]": "의미하다", "last [lɑːst]": "마지막", "any [ˈeni]": "어떤",
        "each [iːtʃ]": "각각", "another [əˈnʌðə(r)]": "또 다른", "same [seɪm]": "같은",
        "hard [hɑːrd]": "어려운", "also [ˈɔːlsəʊ]": "또한", "really [ˈrɪəli]": "정말",
        "bird [bɜːrd]": "새", "trip [trɪp]": "여행", "vacation [veɪˈkeɪʃn]": "휴가",
        "course [kɔːrs]": "과정", "space [speɪs]": "공간", "street [striːt]": "거리",
        "side [saɪd]": "쪽", "paper [ˈpeɪpə(r)]": "종이", "newspaper [ˈnjuːzpeɪpə(r)]": "신문",
        "face [feɪs]": "얼굴", "mind [maɪnd]": "마음", "volunteer [ˌvɒlənˈtɪə(r)]": "자원봉사자",
        "change [tʃeɪndʒ]": "변화", "visit [ˈvɪzɪt]": "방문하다", "start [stɑːrt]": "시작하다",
        "watch [wɒtʃ]": "보다", "light [laɪt]": "빛", "present [ˈpreznt]": "선물",
        "favorite [ˈfeɪvərɪt]": "가장 좋아하는", "enjoy [ɪnˈdʒɔɪ]": "즐기다", "win [wɪn]": "이기다",
        "understand [ˌʌndəˈstænd]": "이해하다", "warm [wɔːrm]": "따뜻한", "clean [kliːn]": "깨끗한",
        "please [pliːz]": "제발", "interesting [ˈɪntrəstɪŋ]": "재미있는", "famous [ˈfeɪməs]": "유명한",
        "special [ˈspeʃl]": "특별한", "only [ˈəʊnli]": "오직", "just [dʒʌst]": "단지",
        "nature [ˈneɪtʃə(r)]": "자연", "restaurant [ˈrestrɒnt]": "식당", "group [ɡruːp]": "집단",
        "habit [ˈhæbɪt]": "습관", "culture [ˈkʌltʃə(r)]": "문화", "information [ˌɪnfəˈmeɪʃn]": "정보",
        "advertisement [ədˈvɜːrtɪsmənt]": "광고", "science [ˈsaɪəns]": "과학", "gene [dʒiːn]": "유전자",
        "war [wɔːr]": "전쟁"
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.prev_idx = -1
    st.session_state.is_wrong = False

st.set_page_config(page_title="영단어 퀴즈 왕!", page_icon="⭐")
st.title("🎡 객관식 영단어 퀴즈")

# 게임 종료 화면
if st.session_state.current_idx >= len(st.session_state.word_list):
    st.balloons()
    st.header(f"🎊 완료! 최종 점수: {st.session_state.score} / {len(st.session_state.word_list)}")
    if st.button("다시 도전하기"):
        # 전체 상태 초기화
        for key in list(st.session_state.keys()):
            del st.session_state[key]
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

# 문제와 버튼 영역
container = st.empty()

with container.container():
    if st.session_state.is_wrong:
        # 오답일 때 단어와 뜻을 함께 아주 크게 표시
        st.markdown(f"""
            <div style="background-color: #fff0f0; padding: 40px; border-radius: 20px; border: 6px solid #ff4b4b; text-align: center; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);">
                <h2 style="color: #555; margin-bottom: 20px;">틀렸습니다! 다시 외워보세요.</h2>
                <div style="background-color: white; padding: 20px; border-radius: 10px; display: inline-block; border: 2px solid #ff4b4b;">
                    <h1 style="color: #111; font-size: 2.5rem; margin: 0;">{current_word}</h1>
                    <h1 style="color: #ff4b4b; font-size: 3.5rem; margin: 10px 0;">{correct_mean}</h1>
                </div>
                <p style="color: #888; margin-top: 20px;">잠시 후 다음 문제로 넘어갑니다...</p>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(2.0) # 학습을 위해 조금 더 긴 시간 제공
        st.session_state.current_idx += 1
        st.session_state.is_wrong = False
        st.rerun()
    
    else:
        st.info(f"다음 단어의 뜻은? \n\n ## **[ {current_word} ]**")
        col1, col2 = st.columns(2)
        for i, option in enumerate(st.session_state.options):
            with col1 if i % 2 == 0 else col2:
                if st.button(option, key=f"btn_{st.session_state.current_idx}_{i}", use_container_width=True):
                    if option == correct_mean:
                        st.session_state.score += 1
                        st.success("🎉 정답입니다!")
                        time.sleep(0.6)
                        st.session_state.current_idx += 1
                        st.rerun()
                    else:
                        st.session_state.is_wrong = True
                        st.rerun()

# 누적 점수 하단 고정 표시
st.divider()
st.markdown(f"#### 📈 실시간 성적: <span style='color:blue'>{st.session_state.score}</span> / {st.session_state.current_idx} (맞은 개수 / 진행 수)", unsafe_allow_html=True)
