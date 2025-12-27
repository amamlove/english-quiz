import streamlit as st
import random
from gtts import gTTS
import os
import uuid

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
        "story [ˈstɔːri]": "이야기, 층",
        "lot [lɒt]": "다량, 많이",
        "name [neɪm]": "이름",
        "hand [hænd]": "손",
        "place [pleɪs]": "장소",
        "practice [ˈpræktɪs]": "연습",
        "work [wɜːrk]": "일",
        "use [juːz]": "사용하다",
        "kind [kaɪnd]": "종류, 친절한",
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
        "clothes [kləʊðz]": "옷",
        "movie [ˈmuːvi]": "영화",
        "activity [ækˈtɪvəti]": "활동",
        "example [ɪɡˈzæmpl]": "예",
        "letter [ˈletə(r)]": "편지",
        "fire [ˈfaɪə(r)]": "불",
        "minute [ˈmɪnɪt]": "분",
        "part [pɑːrt]": "부분",
        "plan [plæn]": "계획",
        "plant [plænt]": "식물",
        "park [pɑːrk]": "공원",
        "call [kɔːl]": "부르다",
        "try [traɪ]": "시도하다",
        "need [niːd]": "필요하다",
        "fun [fʌn]": "재미",
        "future [ˈfjuːtʃə(r)]": "미래",
        "keep [kiːp]": "유지하다",
        "listen [ˈlɪsn]": "듣다",
        "find [faɪnd]": "찾다",
        "learn [lɜːrn]": "배우다",
        "mean [miːn]": "의미하다",
        "last [lɑːst]": "마지막",
        "any [ˈeni]": "어떤",
        "each [iːtʃ]": "각각",
        "another [əˈnʌðə(r)]": "또 다른",
        "same [seɪm]": "같은",
        "hard [hɑːrd]": "어려운",
        "also [ˈɔːlsəʊ]": "또한",
        "really [ˈrɪəli]": "정말",
        "bird [bɜːrd]": "새",
        "trip [trɪp]": "여행",
        "vacation [veɪˈkeɪʃn]": "휴가",
        "course [kɔːrs]": "과정",
        "space [speɪs]": "공간",
        "street [striːt]": "거리",
        "side [saɪd]": "쪽",
        "paper [ˈpeɪpə(r)]": "종이",
        "newspaper [ˈnjuːzpeɪpə(r)]": "신문",
        "face [feɪs]": "얼굴",
        "mind [maɪnd]": "마음",
        "volunteer [ˌvɒlənˈtɪə(r)]": "자원봉사자",
        "change [tʃeɪndʒ]": "변화",
        "visit [ˈvɪzɪt]": "방문하다",
        "start [stɑːrt]": "시작하다",
        "watch [wɒtʃ]": "보다",
        "light [laɪt]": "빛",
        "present [ˈpreznt]": "선물",
        "favorite [ˈfeɪvərɪt]": "가장 좋아하는",
        "enjoy [ɪnˈdʒɔɪ]": "즐기다",
        "win [wɪn]": "이기다",
        "understand [ˌʌndəˈstænd]": "이해하다",
        "warm [wɔːrm]": "따뜻한",
        "clean [kliːn]": "깨끗한",
        "please [pliːz]": "제발",
        "interesting [ˈɪntrestɪŋ]": "재미있는",
        "famous [ˈfeɪməs]": "유명한",
        "special [ˈspeʃl]": "특별한",
        "only [ˈəʊnli]": "오직",
        "just [dʒʌst]": "단지",
        "nature [ˈneɪtʃə(r)]": "자연",
        "restaurant [ˈrestrɒnt]": "식당",
        "group [ɡruːp]": "집단",
        "habit [ˈhæbɪt]": "습관",
        "culture [ˈkʌltʃə(r)]": "문화",
        "information [ˌɪnfəˈmeɪʃn]": "정보",
        "advertisement [ədˈvɜːrtɪsmənt]": "광고",
        "science [ˈsaɪəns]": "과학",
        "gene [dʒiːn]": "유전자",
        "war [wɔːr]": "전쟁"
    }

    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# =====================
# 2. 상태
# =====================
if 'idx' not in st.session_state:
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.result = None
    st.session_state.correct_answer = None
    st.session_state.options = []

# =====================
# 3. UI
# =====================
st.set_page_config("영단어 퀴즈", "🔊")
st.title("🎯 영단어 퀴즈 + 발음 듣기")

# =====================
# 4. 게임 진행
# =====================
if st.session_state.idx < 100:
    word = st.session_state.word_list[st.session_state.idx]
    answer = st.session_state.words_dict[word]

    pure_word = word.split(" ")[0]  # 발음용 (기호 제거)

    # 🔊 발음 생성
    tts = gTTS(text=pure_word, lang="en")
    audio_file = f"audio_{uuid.uuid4()}.mp3"
    tts.save(audio_file)

    st.write(f"### 문제 {st.session_state.idx + 1} / 100")
    st.info(f"**{word}**")

    st.audio(audio_file)

    if not st.session_state.answered:
        wrong = [v for v in st.session_state.words_dict.values() if v != answer]
        st.session_state.options = random.sample(wrong, 3) + [answer]
        random.shuffle(st.session_state.options)

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

    # 임시 오디오 파일 삭제
    os.remove(audio_file)

else:
    st.success("🎊 완료!")
    st.header(f"점수: {st.session_state.score} / 100")

    if st.button("다시 하기"):
        random.shuffle(st.session_state.word_list)
        st.session_state.idx = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.result = None
        st.session_state.correct_answer = None
        st.rerun()

st.sidebar.metric("현재 점수", st.session_state.score)
