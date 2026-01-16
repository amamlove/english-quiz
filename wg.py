import streamlit as st
import random
import time

# 1. PDF 전체 데이터 (표 1 ~ 표 15 통합)
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        # --- PAGE 1 ---
        "spoon": "숟가락", "beauty": "아름다움, 미", "honesty": "정직", "peace": "평화",
        "America": "미국", "bottle": "(유리)병", "earring": "귀걸이", "clock": "시계",
        "city": "도시", "dish": "접시, 음식", "lady": "숙녀", "strawberry": "딸기",
        "deer": "사슴", "sheep": "양", "movie": "영화", "air": "공기, 대기",
        "light": "빛", "speaker": "화자, 연설가", "stick": "막대기",
        "stage": "무대", "fancy": "고급의", "take a picture": "사진을 찍다", "enjoy": "즐기다",
        "novel": "소설", "burn": "(햇볕에) 타다", "excited": "신이 난", "dream": "꿈",
        "around": "사방에", "favorite": "가장 좋아하는", "actress": "여배우", "vegetable": "채소",
        "meat": "고기", "present": "선물", "get a prize": "상을 받다", "follow": "따라가다",
        "turn off": "~을 끄다", "heater": "난방기", "message": "메시지", "scientist": "과학자",
        "niece": "여자 조카", "guest": "손님", "classmate": "급우, 반 친구", "become": "~이 되다",
        "subway station": "지하철역", "every day": "매일",
        "honest": "정직한", "call": "~을 ...라고 부르다", "comb": "빗", "take": "~을 데려가다",
        "ZOO": "동물원", "remember": "기억하다", "forget": "잊어버리다", "closely": "면밀히, 꼼꼼하게",
        "wallet": "지갑", "engineer": "엔지니어, 기사", "music": "음악", "after school": "방과 후(에)",
        "rule": "규칙", "library": "도서관", "there": "거기에, 그곳에", "Chinese": "중국어/중국인의",
        "leave": "떠나다", "draw": "~을 그리다", "take a shower": "샤워하다", "go fishing": "낚시하러 가다",
        "pet": "애완동물",
        "speak": "말하다", "taste": "맛보다", "turtle": "거북이", "get up": "일어나다",
        "wear": "(옷을) 입다", "delicious": "맛있는", "very": "매우", "hard": "열심히",
        "perfect": "완벽한", "painting": "그림", "well": "잘", "bank": "은행",
        "park": "공원", "train": "기차", "miss": "놓치다",

        # --- PAGE 2 ---
        "late": "늦은", "sleepy": "졸린", "winner": "우승자, 승리자", "lucky": "운이 좋은",
        "stay": "머무르다", "angry": "화난", "rich": "부유한", "visit": "방문하다",
        "princess": "공주", "warm": "따뜻한", "Japanese": "일본어/일본인의", "office": "사무실",
        "cheap": "저렴한, 싼", "laugh at": "~을 비웃다", "fair": "공정한", "scared": "겁먹은",
        "cello": "첼로", "wish": "바라다", "learn": "배우다", "cover": "~로 덮다",
        "turn": "돌다", "finish": "끝나다, 끝내다", "pass": "지나가다",
        "find": "~을 찾다", "thief": "도둑", "lose": "잃어버리다", "backpack": "책가방",
        "summer vacation": "여름 방학", "sit": "앉다", "make": "~을 ...하게 만들다",
        "over": "~위로", "blanket": "담요", "go to bed": "잠자리에 들다", "toy": "장난감",
        "much": "많은", "French": "프랑스의, 프랑스어의",

        # --- PAGE 3 ---
        "rain": "비가 내리다", "choose": "고르다", "gloves": "장갑(복수형)", "wake up": "~을 깨우다",
        "hold": "잡고 있다, 들고 있다", "sell": "팔다", "blow": "불다", "candle": "초, 양초",
        "homework": "숙제", "movie star": "영화배우", "jog": "조깅하다", "poem": "시",
        "bake": "~을 굽다", "newspaper": "신문", "horror": "공포", "work": "직장",
        "grow": "키우다", "look for": "~을 찾다", "way": "길", "museum": "박물관",
        "water": "물을 주다", "island": "섬", "catch": "잡다", "spinach": "시금치",
        "build": "짓다", "bridge": "다리", "ask": "묻다, 질문하다", "classical": "고전의",
        "December": "12월", "science": "과학",
        "have dinner": "저녁을 먹다", "hate": "미워하다", "fly": "~을 날리다", "kite": "연",
        "push": "밀다", "wash the dishes": "설거지하다", "do the laundry": "빨래를 하다", "bark": "짖다",
        "carry": "나르다", "magazine": "잡지", "go shopping": "쇼핑하러 가다", "touch": "만지다",
        "top": "꼭대기, 맨 위", "hide": "숨기다", "treasure": "보물", "pick up": "~을 줍다",
        "check": "점검하다", "chopsticks": "젓가락", "climb up": "위로 올라가다", "ladder": "사다리",
        "in the future": "미래에", "ticket": "표", "tonight": "오늘밤(에)", "cartoon": "만화",
        "grape": "포도", "front door": "현관, 정문", "have a party": "파티를 열다",
        "great": "멋진, 좋은", "fantastic": "환상적인", "people": "사람들", "wrong": "잘못된",
        "weather": "날씨", "melon": "멜론", "dark": "어두운", "cloud": "구름",
        "smart": "영리한, 똑똑한", "pink": "분홍의", "sour": "신, 시큼한", "need": "필요로 하다",
        "windy": "바람이 부는", "poor": "가난한", "wise": "현명한, 지혜로운", "soft": "부드러운",

        # --- PAGE 4 ---
        "soap": "비누", "fresh": "신선한", "cheese stick": "치즈스틱", "easy": "쉬운",
        "police officer": "경찰관", "tired": "피곤한", "amazing": "놀라운", "silk": "비단",
        "writer": "작가", "angel": "천사", "terrible": "끔찍한, 안 좋은", "singer": "가수",
        "often": "자주, 종종", "go to the movies": "영화 보러 가다", "wonderful": "근사한, 멋진",
        "curious": "궁금한", "whale": "고래", "club": "동아리, 클럽", "president": "대통령, 사장",
        "among": "~ 사이에", "spend": "(시간을) 보내다", "because of": "~ 때문에", "runner": "주자, 달리는 사람",
        "mountain": "산", "subject": "과목", "restaurant": "식당", "neighborhood": "이웃, 동네", "bright": "밝은",
        "carefully": "조심해서, 주의하여", "by car": "자동차로", "on weekends": "주말에", "answer": "대답하다",
        "wisely": "지혜롭게", "clear": "명확한", "different": "다른", "silent": "조용한",
        "careful": "조심하는", "quiet": "조용한", "quick": "빠른, 빨리", "trust": "믿다, 신뢰하다",
        "important": "중요한", "dangerous": "위험한", "soon": "곧, 머지않아", "near": "근처의",
        "popular": "인기 있는", "interesting": "흥미로운", "exciting": "흥미진진한", "voice": "목소리",
        "acting": "행동", "saying": "말"
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 초기화 및 UI 로직
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.prev_idx = -1
    st.session_state.is_wrong = False

st.set_page_config(page_title="영단어 전체 정복 퀴즈", page_icon="🎓")
st.title("🎓 영단어777-3권권")

# 완료 화면
if st.session_state.current_idx >= len(st.session_state.word_list):
    st.balloons()
    st.header(f"🎊 대단합니다! 모든 단어를 완료했어요!")
    st.subheader(f"최종 점수: {st.session_state.score} / {len(st.session_state.word_list)}")
    if st.button("처음부터 다시 하기"):
        st.session_state.score = 0
        st.session_state.current_idx = 0
        st.session_state.prev_idx = -1
        random.shuffle(st.session_state.word_list)
        st.rerun()
    st.stop()

# 현재 문제 설정
current_word = st.session_state.word_list[st.session_state.current_idx]
correct_mean = st.session_state.words_dict[current_word]

# 보기 생성
if st.session_state.prev_idx != st.session_state.current_idx:
    other_means = [v for k, v in st.session_state.words_dict.items() if v != correct_mean]
    other_means = list(set(other_means))  # 중복 뜻 제거
    options = random.sample(other_means, 3)
    options.append(correct_mean)
    random.shuffle(options)
    st.session_state.options = options
    st.session_state.prev_idx = st.session_state.current_idx
    st.session_state.is_wrong = False

# UI 표시
st.write(f"### 문제 {st.session_state.current_idx + 1} / {len(st.session_state.word_list)}")
st.progress((st.session_state.current_idx) / len(st.session_state.word_list))
st.info(f"다음 단어의 뜻을 고르세요: \n\n ## **[ {current_word} ]**")

# 버튼 배치
col1, col2 = st.columns(2)
for i, option in enumerate(st.session_state.options):
    with col1 if i % 2 == 0 else col2:
        if st.session_state.is_wrong:
            if option == correct_mean:
                st.markdown(f"""<div style="background-color: #2ecc71; color: white; padding: 10px; border-radius: 5px; text-align: center; border: 2px solid #27ae60; font-weight: bold; margin-bottom: 10px;">🎯 {option} (정답)</div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""<div style="background-color: #f8f9fa; color: #adb5bd; padding: 10px; border-radius: 5px; text-align: center; border: 1px solid #dee2e6; margin-bottom: 10px;">{option}</div>""", unsafe_allow_html=True)
        else:
            if st.button(option, key=f"btn_{st.session_state.current_idx}_{i}", use_container_width=True):
                if option == correct_mean:
                    st.session_state.score += 1
                    st.success("🎉 정답입니다!")
                    time.sleep(0.6)
                    st.session_state.current_idx += 1
                    st.rerun()
                else:
                    st.session_state.is_wrong = True
                    st.error("❌ 오답입니다!")
                    st.rerun()

# 오답 시 자동 이동
if st.session_state.is_wrong:
    time.sleep(2.0)
    st.session_state.current_idx += 1
    st.session_state.is_wrong = False
    st.rerun()

st.divider()
st.markdown(f"#### 📈 현재 성적: **{st.session_state.score}** 점 / 진행: **{st.session_state.current_idx}** 문제")
