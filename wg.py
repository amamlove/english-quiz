import streamlit as st
import random
import time

# 1. PDF에서 추출한 영단어 데이터 (표 1 ~ 표 6 통합)
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        # 표 1 (Source 3)
        "spoon": "숟가락", "beauty": "아름다움, 미", "honesty": "정직", "peace": "평화",
        "America": "미국", "bottle": "(유리)병", "earring": "귀걸이", "clock": "시계",
        "city": "도시", "dish": "접시, 음식", "lady": "숙녀", "strawberry": "딸기",
        "deer": "사슴", "sheep": "양", "movie": "영화", "air": "공기, 대기",
        "light": "빛", "speaker": "화자, 연설가", "stick": "막대기",
        
        # 표 4 (Source 4) - PDF 순서상 표 4가 먼저 등장
        "stage": "무대", "fancy": "고급의", "take a picture": "사진을 찍다", "enjoy": "즐기다",
        "novel": "소설", "burn": "(햇볕에) 타다", "excited": "신이 난", "dream": "꿈",
        "around": "사방에", "favorite": "가장 좋아하는", "actress": "여배우", "vegetable": "채소",
        "meat": "고기", "present": "선물", "get a prize": "상을 받다", "follow": "따라가다",
        "turn off": "~을 끄다", "heater": "난방기", "message": "메시지", "scientist": "과학자",
        "niece": "여자 조카", "guest": "손님", "classmate": "급우, 반 친구", "become": "~이 되다",
        "subway station": "지하철역", "every day": "매일",

        # 표 2 (Source 6)
        "honest": "정직한", "call": "~을 ...라고 부르다", "comb": "빗", "take": "~을 데려가다",
        "ZOO": "동물원", "remember": "기억하다", "forget": "잊어버리다", "closely": "면밀히, 꼼꼼하게",

        # 5번 데이터 (Source 8)
        "wallet": "지갑", "engineer": "엔지니어, 기사", "music": "음악", "after school": "방과 후(에)",
        "rule": "규칙", "library": "도서관", "there": "거기에, 그곳에", "Chinese": "중국어/중국인의",
        "leave": "떠나다", "draw": "~을 그리다", "take a shower": "샤워하다", "go fishing": "낚시하러 가다",
        "pet": "애완동물",

        # 표 3 (Source 10)
        "speak": "말하다", "taste": "맛보다", "turtle": "거북이", "get up": "일어나다",
        "wear": "(옷을) 입다", "delicious": "맛있는", "very": "매우", "hard": "열심히",
        "perfect": "완벽한", "painting": "그림", "well": "잘", "bank": "은행",
        "park": "공원", "train": "기차", "miss": "놓치다",

        # 6번 데이터 (Source 12)
        "late": "늦은", "sleepy": "졸린", "winner": "우승자, 승리자", "lucky": "운이 좋은",
        "stay": "머무르다", "angry": "화난", "rich": "부유한", "visit": "방문하다",
        "princess": "공주", "warm": "따뜻한", "Japanese": "일본인의", "office": "사무실",
        "cheap": "저렴한, 싼", "laugh at": "~을 비웃다", "fair": "공정한", "scared": "겁먹은",
        "cello": "첼로", "wish": "바라다", "learn": "배우다", "cover": "~로 덮다",
        "turn": "돌다", "finish": "끝나다, 끝내다", "pass": "지나가다"
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 초기화 및 UI 로직
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.prev_idx = -1
    st.session_state.is_wrong = False

st.set_page_config(page_title="PDF 영단어 마스터 퀴즈", page_icon="📖")
st.title("📖 영단어777 3-1-6")

# 완료 화면
if st.session_state.current_idx >= len(st.session_state.word_list):
    st.balloons()
    st.header(f"🎊 모든 단어를 마쳤습니다!")
    st.subheader(f"최종 점수: {st.session_state.score} / {len(st.session_state.word_list)}")
    if st.button("다시 도전하기"):
        st.session_state.score = 0
        st.session_state.current_idx = 0
        st.session_state.prev_idx = -1
        random.shuffle(st.session_state.word_list)
        st.rerun()
    st.stop()

# 현재 문제 설정
current_word = st.session_state.word_list[st.session_state.current_idx]
correct_mean = st.session_state.words_dict[current_word]

# 보기 생성 (문제 바뀔 때 한 번만)
if st.session_state.prev_idx != st.session_state.current_idx:
    other_means = [v for k, v in st.session_state.words_dict.items() if v != correct_mean]
    # 중복된 뜻이 있을 수 있으므로 set으로 중복 제거 후 리스트화
    other_means = list(set(other_means))
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

# 버튼 배치
col1, col2 = st.columns(2)
for i, option in enumerate(st.session_state.options):
    with col1 if i % 2 == 0 else col2:
        if st.session_state.is_wrong:
            # 틀렸을 때 정답 강조 표시
            if option == correct_mean:
                st.markdown(f"""<div style="background-color: #ff4b4b; color: white; padding: 10px; border-radius: 5px; text-align: center; border: 2px solid #b22222; font-weight: bold; margin-bottom: 10px;">🎯 {option} (정답)</div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""<div style="background-color: #f0f2f6; color: #a3a8b4; padding: 10px; border-radius: 5px; text-align: center; border: 1px solid #dcdde1; margin-bottom: 10px;">{option}</div>""", unsafe_allow_html=True)
        else:
            # 일반 버튼 상태
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

# 오답 시 대기 후 자동 다음 문제
if st.session_state.is_wrong:
    time.sleep(2.0)
    st.session_state.current_idx += 1
    st.session_state.is_wrong = False
    st.rerun()

st.divider()
st.markdown(f"#### 📈 현재 성적: **{st.session_state.score}** / {st.session_state.current_idx}")
