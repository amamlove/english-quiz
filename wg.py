import streamlit as st
import random

# 1. 영단어 데이터 (30개)
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
       "삶, 인생": "life" , "일, 직업": "job" , "나라, 시골": "country" , "지구, 땅": "earth" , "문제": "problem" , "방법, 길": "way" , "언어": "language" , "대화": "dialog" , "이야기, 층": "story" , "다량, 많이": "lot" , "이름(을 붙이다)": "name" , "손, 건네주다": "hand" , "장소, 두다": "place" , "연습(하다)": "practice" , "일(하다)": "work" , "사용(하다)": "use" , "종류, 친절한": "kind" , "가지고있다, 먹다": "have" , "만들다": "make" , "~하게 하다, 허락하다": "let" , "얻다, 이르다, 되다": "get" , "데려가다, 필요로 하다": "take" , "살다, 살아있는": "live" , "다른": "different" , "중요한": "important" , "다른, 그 밖의": "other" , "옳은, 오른쪽의": "right" , "확신하는, 물론": "sure" , "너무, ~도 또한": "too" , "잘, 건강한, 우물": "well" , "사람, 인물": "person" , "옷, 의복": "clothes" , "영화": "movie" , "활동": "activity" , "예, 모범": "example" , "편지, 글자": "letter" , "불, 화재": "fire" , "분, 순간": "minute" , "부분, 가르다": "part" , "계획(하다)": "plan" , "식물, 공장": "plant" , "공원, 주차하다": "park" , "통화하다, 부르다": "call" , "시도하다, 노력하다": "try" , "필요(하다)": "need" , "재미, 장난": "fun" , "미래": "future" , "유지하다, 지키다": "keep" , "듣다": "listen" , "찾아내다, 발견하다": "find" , "배우다, 알아내다": "learn" , "의미하다": "mean" , "지난, 마지막의": "last" , "무슨, 약간의": "any" , "각각": "each" , "또 하나의": "another" , "같은": "same" , "단단한, 어려운": "hard" , "~도 또한": "also" , "참으로, 정말": "really" , "새": "bird" , "여행": "trip" , "휴가, 방학": "vacation" , "강좌, 과정, 진로": "course" , "공간, 우주": "space" , "거리, 도로": "street" , "측, 쪽, 측면": "side" , "종이, 서류, 신문": "paper" , "신문": "newspaper" , "얼굴, 직면하다": "face" , "마음, 꺼리다": "mind" , "자원봉사자, 자원하다": "volunteer" , "변화(하다), 거스름돈": "change" , "방문(하다)": "visit" , "시작(하다)": "start" , "지켜보다, 시계": "watch" , "빛, 밝은": "light" , "선물, 현재, 출석한": "present" , "가장 좋아하는": "favorite" , "즐기다": "enjoy" , "이기다, 획득하다": "win" , "이해하다": "understand" , "따뜻한": "warm" , "깨끗한": "clean" , "제발, 기쁘게 하다": "please" , "재미있는": "interesting" , "유명한": "famous" , "특별한, 전문의": "special" , "단지, 오직, 유일한": "only" , "막, 단지": "just" , "자연, 천성": "nature" , "레스토랑, 식당": "restaurant" , "무리, 집단": "group" , "습관": "habit" , "문화": "culture" , "정보": "information" , "광고": "advertisement" , "과학": "science" , "유전자": "gene" , "전쟁": "war"
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
st.title("🎡 777-3권 객관식 영단어 퀴즈")

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




