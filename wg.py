import streamlit as st
import random
import time

# 1. PDF 데이터 통합 (단어: [한글발음, 뜻])
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        # --- PAGE 1 ---
        "spoon": ["스푼", "숟가락"], "beauty": ["뷰티", "아름다움, 미"], "honesty": ["어니스티", "정직"], 
        "peace": ["피스", "평화"], "America": ["어메리카", "미국"], "bottle": ["바틀", "(유리)병"], 
        "earring": ["이어링", "귀걸이"], "clock": ["클락", "시계"], "city": ["시티", "도시"], 
        "dish": ["디쉬", "접시, 음식"], "lady": ["레이디", "숙녀"], "strawberry": ["스트로베리", "딸기"],
        "deer": ["디어", "사슴"], "sheep": ["쉽", "양"], "movie": ["무비", "영화"], 
        "air": ["에어", "공기, 대기"], "light": ["라이트", "빛"], "speaker": ["스피커", "화자, 연설가"], 
        "stick": ["스틱", "막대기"], "stage": ["스테이지", "무대"], "fancy": ["팬시", "고급의"], 
        "take a picture": ["테이크 어 픽처", "사진을 찍다"], "enjoy": ["인조이", "즐기다"],
        "novel": ["나블", "소설"], "burn": ["번", "(햇볕에) 타다"], "excited": ["익사이티드", "신이 난"], 
        "dream": ["드림", "꿈"], "around": ["어라운드", "사방에"], "favorite": ["페이보릿", "가장 좋아하는"], 
        "actress": ["액트리스", "여배우"], "vegetable": ["베지터블", "채소"], "meat": ["미트", "고기"], 
        "present": ["프레전트", "선물"], "get a prize": ["겟 어 프라이즈", "상을 받다"], 
        "follow": ["팔로우", "따라가다"], "turn off": ["턴 오프", "~을 끄다"], "heater": ["히터", "난방기"], 
        "message": ["메시지", "메시지"], "scientist": ["사이언티스트", "과학자"], "niece": ["니스", "여자 조카"], 
        "guest": ["게스트", "손님"], "classmate": ["클래스메이트", "급우, 반 친구"], "become": ["비컴", "~이 되다"],
        "subway station": ["서브웨이 스테이션", "지하철역"], "every day": ["에브리 데이", "매일"],
        "honest": ["어니스트", "정직한"], "call": ["콜", "~을 ...라고 부르다"], "comb": ["콤", "빗"], 
        "take": ["테이크", "~을 데려가다"], "ZOO": ["주", "동물원"], "remember": ["리멤버", "기억하다"], 
        "forget": ["포겟", "잊어버리다"], "closely": ["클로슬리", "면밀히, 꼼꼼하게"], "wallet": ["월릿", "지갑"], 
        "engineer": ["엔지니어", "엔지니어, 기사"], "music": ["뮤직", "음악"], 
        "after school": ["애프터 스쿨", "방과 후(에)"], "rule": ["룰", "규칙"], "library": ["라이브러리", "도서관"], 
        "there": ["데어", "거기에, 그곳에"], "Chinese": ["차이니즈", "중국어/중국인의"], "leave": ["리브", "떠나다"], 
        "draw": ["드로", "~을 그리다"], "take a shower": ["테이크 어 샤워", "샤워하다"], 
        "go fishing": ["고 피싱", "낚시하러 가다"], "pet": ["펫", "애완동물"], "speak": ["스피크", "말하다"], 
        "taste": ["테이스트", "맛보다"], "turtle": ["터틀", "거북이"], "get up": ["겟 업", "일어나다"],
        "wear": ["웨어", "(옷을) 입다"], "delicious": ["딜리셔스", "맛있는"], "very": ["베리", "매우"], 
        "hard": ["하드", "열심히"], "perfect": ["퍼펙트", "완벽한"], "painting": ["페인팅", "그림"], 
        "well": ["웰", "잘"], "bank": ["뱅크", "은행"], "park": ["파크", "공원"], 
        "train": ["트레인", "기차"], "miss": ["미스", "놓치다"],

        # --- PAGE 2 ---
        "late": ["레이트", "늦은"], "sleepy": ["슬리피", "졸린"], "winner": ["위너", "우승자, 승리자"], 
        "lucky": ["럭키", "운이 좋은"], "stay": ["스테이", "머무르다"], "angry": ["앵그리", "화난"], 
        "rich": ["리치", "부유한"], "visit": ["비지트", "방문하다"], "princess": ["프린세스", "공주"], 
        "warm": ["웜", "따뜻한"], "Japanese": ["재패니즈", "일본어/일본인의"], "office": ["오피스", "사무실"],
        "cheap": ["칩", "저렴한, 싼"], "laugh at": ["래프 앳", "~을 비웃다"], "fair": ["페어", "공정한"], 
        "scared": ["스케어드", "겁먹은"], "cello": ["첼로", "첼로"], "wish": ["위시", "바라다"], 
        "learn": ["런", "배우다"], "cover": ["커버", "~로 덮다"], "turn": ["턴", "돌다"], 
        "finish": ["피니시", "끝나다, 끝내다"], "pass": ["패스", "지나가다"], "find": ["파인드", "~을 찾다"], 
        "thief": ["피프", "도둑"], "lose": ["루즈", "잃어버리다"], "backpack": ["백팩", "책가방"],
        "summer vacation": ["썸머 베케이션", "여름 방학"], "sit": ["시트", "앉다"], 
        "make": ["메이크", "~을 ...하게 만들다"], "over": ["오버", "~위로"], "blanket": ["블랭킷", "담요"], 
        "go to bed": ["고 투 베드", "잠자리에 들다"], "toy": ["토이", "장난감"], "much": ["머치", "많은"], 
        "French": ["프렌치", "프랑스의, 프랑스어의"],

        # --- PAGE 3 ---
        "rain": ["레인", "비가 내리다"], "choose": ["추즈", "고르다"], "gloves": ["글러브스", "장갑(복수형)"], 
        "wake up": ["웨이크 업", "~을 깨우다"], "hold": ["홀드", "잡고 있다, 들고 있다"], 
        "sell": ["셀", "팔다"], "blow": ["블로우", "불다"], "candle": ["캔들", "초, 양초"], 
        "homework": ["홈워크", "숙제"], "movie star": ["무비 스타", "영화배우"], "jog": ["조그", "조깅하다"], 
        "poem": ["포엠", "시"], "bake": ["베이크", "~을 굽다"], "newspaper": ["뉴스페이퍼", "신문"], 
        "horror": ["호러", "공포"], "work": ["워크", "직장"], "grow": ["그로우", "키우다"], 
        "look for": ["룩 포", "~을 찾다"], "way": ["웨이", "길"], "museum": ["뮤지엄", "박물관"],
        "water": ["워터", "물을 주다"], "island": ["아일랜드", "섬"], "catch": ["캐치", "잡다"], 
        "spinach": ["스피니치", "시금치"], "build": ["빌드", "짓다"], "bridge": ["브릿지", "다리"], 
        "ask": ["애스크", "묻다, 질문하다"], "classical": ["클래시컬", "고전의"], "December": ["디셈버", "12월"], 
        "science": ["사이언스", "과학"], "have dinner": ["해브 디너", "저녁을 먹다"], "hate": ["헤이트", "미워하다"], 
        "fly": ["플라이", "~을 날리다"], "kite": ["카이트", "연"], "push": ["푸쉬", "밀다"], 
        "wash the dishes": ["와쉬 더 디쉬즈", "설거지하다"], "do the laundry": ["두 더 론드리", "빨래를 하다"], 
        "bark": ["바크", "짖다"], "carry": ["캐리", "나르다"], "magazine": ["매거진", "잡지"], 
        "go shopping": ["고 쇼핑", "쇼핑하러 가다"], "touch": ["터치", "만지다"], "top": ["탑", "꼭대기, 맨 위"], 
        "hide": ["하이드", "숨기다"], "treasure": ["트레저", "보물"], "pick up": ["픽 업", "~을 줍다"],
        "check": ["체크", "점검하다"], "chopsticks": ["찹스틱스", "젓가락"], 
        "climb up": ["클라임 업", "위로 올라가다"], "ladder": ["래더", "사다리"], 
        "in the future": ["인 더 퓨처", "미래에"], "ticket": ["티켓", "표"], "tonight": ["투나잇", "오늘밤(에)"], 
        "cartoon": ["카툰", "만화"], "grape": ["그레이프", "포도"], "front door": ["프런트 도어", "현관, 정문"], 
        "have a party": ["해브 어 파티", "파티를 열다"], "great": ["그레이트", "멋진, 좋은"], 
        "fantastic": ["판타스틱", "환상적인"], "people": ["피플", "사람들"], "wrong": ["롱", "잘못된"],
        "weather": ["웨더", "날씨"], "melon": ["멜론", "멜론"], "dark": ["다크", "어두운"], 
        "cloud": ["클라우드", "구름"], "smart": ["스마트", "영리한, 똑똑한"], "pink": ["핑크", "분홍의"], 
        "sour": ["사워", "신, 시큼한"], "need": ["니드", "필요로 하다"], "windy": ["윈디", "바람이 부는"], 
        "poor": ["푸어", "가난한"], "wise": ["와이즈", "현명한, 지혜로운"], "soft": ["소프트", "부드러운"],

        # --- PAGE 4 ---
        "soap": ["소프", "비누"], "fresh": ["프레쉬", "신선한"], "cheese stick": ["치즈 스틱", "치즈스틱"], 
        "easy": ["이지", "쉬운"], "police officer": ["폴리스 오피서", "경찰관"], "tired": ["타이어드", "피곤한"], 
        "amazing": ["어메이징", "놀라운"], "silk": ["실크", "비단"], "writer": ["라이터", "작가"], 
        "angel": ["엔젤", "천사"], "terrible": ["테러블", "끔찍한, 안 좋은"], "singer": ["싱어", "가수"],
        "often": ["오픈", "자주, 종종"], "go to the movies": ["고 투 더 무비즈", "영화 보러 가다"], 
        "wonderful": ["원더풀", "근사한, 멋진"], "curious": ["큐리어스", "궁금한"], "whale": ["웨일", "고래"], 
        "club": ["클럽", "동아리, 클럽"], "president": ["프레지던트", "대통령, 사장"], "among": ["어망", "~ 사이에"], 
        "spend": ["스펜드", "(시간을) 보내다"], "because of": ["비코즈 오브", "~ 때문에"], 
        "runner": ["러너", "주자, 달리는 사람"], "mountain": ["마운틴", "산"], "subject": ["서브젝트", "과목"], 
        "restaurant": ["레스토랑", "식당"], "neighborhood": ["네이버후드", "이웃, 동네"], "bright": ["브라이트", "밝은"],
        "carefully": ["케어풀리", "조심해서, 주의하여"], "by car": ["바이 카", "자동차로"], 
        "on weekends": ["온 위켄즈", "주말에"], "answer": ["앤서", "대답하다"], "wisely": ["와이즐리", "지혜롭게"], 
        "clear": ["클리어", "명확한"], "different": ["디퍼런트", "다른"], "silent": ["사일런트", "조용한"],
        "careful": ["케어풀", "조심하는"], "quiet": ["콰이어트", "조용한"], "quick": ["퀵", "빠른, 빨리"], 
        "trust": ["트러스트", "믿다, 신뢰하다"], "important": ["임포턴트", "중요한"], 
        "dangerous": ["데인저러스", "위험한"], "soon": ["순", "곧, 머지않아"], "near": ["니어", "근처의"],
        "popular": ["파퓰러", "인기 있는"], "interesting": ["인터레스팅", "흥미로운"], 
        "exciting": ["익사이팅", "흥미진진한"], "voice": ["보이스", "목소리"], "acting": ["액팅", "행동"], 
        "saying": ["세잉", "말"]
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 초기화 및 UI 로직
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.prev_idx = -1
    st.session_state.is_wrong = False

st.set_page_config(page_title="영단어 777 정복", page_icon="🎓")
st.title("🎓 영단어 777-3권")

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
correct_pron = st.session_state.words_dict[current_word][0]
correct_mean = st.session_state.words_dict[current_word][1]

# 보기 생성
if st.session_state.prev_idx != st.session_state.current_idx:
    # 뜻만 추출하여 보기 생성
    other_means = [v[1] for k, v in st.session_state.words_dict.items() if v[1] != correct_mean]
    other_means = list(set(other_means))  # 중복 제거
    options = random.sample(other_means, 3)
    options.append(correct_mean)
    random.shuffle(options)
    st.session_state.options = options
    st.session_state.prev_idx = st.session_state.current_idx
    st.session_state.is_wrong = False

# UI 표시
st.write(f"### 문제 {st.session_state.current_idx + 1} / {len(st.session_state.word_list)}")
st.progress((st.session_state.current_idx) / len(st.session_state.word_list))

# 단어와 발음기호 표시
st.info(f"뜻을 고르세요: \n\n ## **{current_word}** \n #### `[{correct_pron}]`")

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
                    st.success(f"🎉 정답입니다! [{correct_pron}]")
                    time.sleep(0.7)
                    st.session_state.current_idx += 1
                    st.rerun()
                else:
                    st.session_state.is_wrong = True
                    st.error(f"❌ 오답입니다! 정답은 '{correct_mean}'입니다.")
                    st.rerun()

# 오답 시 자동 이동
if st.session_state.is_wrong:
    time.sleep(2.5)
    st.session_state.current_idx += 1
    st.session_state.is_wrong = False
    st.rerun()

st.divider()
st.markdown(f"#### 📈 현재 성적: **{st.session_state.score}** 점 / 진행: **{st.session_state.current_idx}** 문제")
