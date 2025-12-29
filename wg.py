# -*- coding: utf-8 -*-
import streamlit as st
import random

# -------------------------------
# 단어 데이터 (100개)
# -------------------------------
WORDS = {
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
    "interesting [ˈɪntrəstɪŋ]": "재미있는",
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
    "war [wɔːr]": "전쟁",
}

# -------------------------------
# 상태
# -------------------------------
if "order" not in st.session_state:
    st.session_state.order = list(WORDS.keys())
    random.shuffle(st.session_state.order)
    st.session_state.idx = 0
    st.session_state.score = 0

st.title("📘 영단어 객관식 퀴즈")

# -------------------------------
# 퀴즈
# -------------------------------
if st.session_state.idx < len(st.session_state.order):

    word = st.session_state.order[st.session_state.idx]
    correct_meaning = WORDS[word]

    wrongs = random.sample(
        [v for v in WORDS.values() if v != correct_meaning], 3
    )
    options = wrongs + [correct_meaning]
    random.shuffle(options)

    correct_index = options.index(correct_meaning)

    st.write(f"### 문제 {st.session_state.idx + 1} / 100")
    st.info(f"**{word}** 의 뜻은?")

    col1, col2 = st.columns(2)
    for i, opt in enumerate(options):
        with col1 if i % 2 == 0 else col2:
            if st.button(opt, key=f"{st.session_state.idx}_{i}", use_container_width=True):
                if i == correct_index:
                    st.success("🎉 정답!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ 오답! 정답: {correct_meaning}")

                st.session_state.idx += 1
                st.rerun()

else:
    st.success("🎊 완료!")
    st.header(f"점수: {st.session_state.score} / 100")

    if st.button("다시 시작"):
        random.shuffle(st.session_state.order)
        st.session_state.idx = 0
        st.session_state.score = 0
        st.rerun()
