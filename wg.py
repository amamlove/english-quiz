import streamlit as st
import random
import time

# 1. 단어 데이터 (단어: [발음기호, 한글읽기, 뜻])
if 'words_dict' not in st.session_state:
    # 발음기호에서 슬러시(/) 기호를 미리 제거하여 저장하거나 
    # 표시할 때 제거하도록 처리합니다.
    st.session_state.words_dict = {
        # --- PAGE 1 ---
        "spoon": ["spuːn", "스푼", "숟가락"], "beauty": ["ˈbjuːti", "뷰티", "아름다움, 미"], 
        "honesty": ["ˈɒnɪsti", "어니스티", "정직"], "peace": ["piːs", "피스", "평화"],
        "America": ["əˈmerɪkə", "어메리카", "미국"], "bottle": ["ˈbɒtl", "바틀", "(유리)병"], 
        "earring": ["ˈɪərɪŋ", "이어링", "귀걸이"], "clock": ["klɒk", "클락", "시계"],
        "city": ["ˈsɪti", "시티", "도시"], "dish": ["dɪʃ", "디쉬", "접시, 음식"], 
        "lady": ["ˈleɪdi", "레이디", "숙녀"], "strawberry": ["ˈstrɔːbəri", "스트로베리", "딸기"],
        "deer": ["dɪə", "디어", "사슴"], "sheep": ["ʃiːp", "쉽", "양"], 
        "movie": ["ˈmuːvi", "무비", "영화"], "air": ["eə", "에어", "공기, 대기"],
        "light": ["laɪt", "라이트", "빛"], "speaker": ["ˈspiːkə", "스피커", "화자, 연설가"], 
        "stick": ["stɪk", "스틱", "막대기"], "stage": ["steɪdʒ", "스테이지", "무대"], 
        "fancy": ["ˈfænsi", "팬시", "고급의"], "take a picture": ["teɪk ə ˈpɪktʃə", "테이크 어 픽처", "사진을 찍다"], 
        "enjoy": ["ɪnˈdʒɔɪ", "인조이", "즐기다"], "novel": ["ˈnɒvl", "나블", "소설"], 
        "burn": ["bɜːn", "번", "(햇볕에) 타다"], "excited": ["ɪkˈsaɪtɪd", "익사이티드", "신이 난"], 
        "dream": ["driːm", "드림", "꿈"], "around": ["əˈraʊnd", "어라운드", "사방에"], 
        "favorite": ["ˈfeɪvərɪt", "페이보릿", "가장 좋아하는"], "actress": ["ˈæktrəs", "액트리스", "여배우"], 
        "vegetable": ["ˈvedʒtəbl", "베지터블", "채소"], "meat": ["miːt", "미트", "고기"], 
        "present": ["ˈpreznt", "프레전트", "선물"], "get a prize": ["ɡet ə praɪz", "겟 어 프라이즈", "상을 받다"], 
        "follow": ["ˈfɒləʊ", "팔로우", "따라가다"], "turn off": ["tɜːn ɒf", "턴 오프", "~을 끄다"], 
        "heater": ["ˈhiːtə", "히터", "난방기"], "message": ["ˈmesɪdʒ", "메시지", "메시지"], 
        "scientist": ["ˈsaɪəntɪst", "사이언티스트", "과학자"], "niece": ["niːs", "니스", "여자 조카"], 
        "guest": ["ɡest", "게스트", "손님"], "classmate": ["ˈklɑːsmeɪt", "클래스메이트", "급우, 반 친구"], 
        "become": ["bɪˈkʌm", "비컴", "~이 되다"], "subway station": ["ˈsʌbweɪ ˈsteɪʃn", "서브웨이 스테이션", "지하철역"], 
        "every day": ["ˈevri deɪ", "에브리 데이", "매일"], "honest": ["ˈɒnɪst", "어니스트", "정직한"], 
        "call": ["kɔːl", "콜", "~을 ...라고 부르다"], "comb": ["kəʊm", "콤", "빗"], 
        "take": ["teɪk", "테이크", "~을 데려가다"], "ZOO": ["zuː", "주", "동물원"], 
        "remember": ["rɪˈmembə", "리멤버", "기억하다"], "forget": ["fəˈɡet", "포겟", "잊어버리다"], 
        "closely": ["ˈkləʊsli", "클로슬리", "면밀히, 꼼꼼하게"], "wallet": ["ˈwɒlɪt", "월릿", "지갑"], 
        "engineer": ["ˌendʒɪˈnɪə", "엔지니어", "엔지니어, 기사"], "music": ["ˈmjuːzɪk", "뮤직", "음악"], 
        "after school": ["ˈɑːftə skuːl", "애프터 스쿨", "방과 후(에)"], "rule": ["ruːl", "룰", "규칙"], 
        "library": ["ˈlaɪbrəri", "라이브러리", "도서관"], "there": ["ðeə", "데어", "거기에, 그곳에"], 
        "Chinese": ["ˌtʃaɪˈniːz", "차이니즈", "중국어/중국인의"], "leave": ["liːv", "리브", "떠나다"], 
        "draw": ["drɔː", "드로", "~을 그리다"], "take a shower": ["teɪk ə ˈʃaʊə", "테이크 어 샤워", "샤워하다"], 
        "go fishing": ["ɡəʊ ˈfɪʃɪŋ", "고 피싱", "낚시하러 가다"], "pet": ["pet", "펫", "애완동물"],
        "speak": ["spiːk", "스피크", "말하다"], "taste": ["teɪst", "테이스트", "맛보다"], 
        "turtle": ["ˈtɜːtl", "터틀", "거북이"], "get up": ["ɡet ʌp", "겟 업", "일어나다"],
        "wear": ["weə", "웨어", "(옷을) 입다"], "delicious": ["dɪˈlɪʃəs", "딜리셔스", "맛있는"], 
        "very": ["ˈveri", "베리", "매우"], "hard": ["hɑːd", "하드", "열심히"], 
        "perfect": ["ˈpɜːfɪkt", "퍼펙트", "완벽한"], "painting": ["ˈpeɪntɪŋ", "페인팅", "그림"], 
        "well": ["wel", "웰", "잘"], "bank": ["bæŋk", "뱅크", "은행"], 
        "park": ["pɑːk", "파크", "공원"], "train": ["treɪn", "기차"], "miss": ["mɪs", "미스", "놓치다"],

        # --- PAGE 2 ---
        "late": ["leɪt", "레이트", "늦은"], "sleepy": ["ˈsliːpi", "슬리피", "졸린"], 
        "winner": ["ˈwɪnə", "위너", "우승자, 승리자"], "lucky": ["ˈlʌki", "럭키", "운이 좋은"], 
        "stay": ["steɪ", "스테이", "머무르다"], "angry": ["ˈæŋɡri", "앵그리", "화난"], 
        "rich": ["rɪtʃ", "리치", "부유한"], "visit": ["ˈvɪzɪt", "비지트", "방문하다"], 
        "princess": ["ˌprɪnˈses", "프린세스", "공주"], "warm": ["wɔːm", "웜", "따뜻한"], 
        "Japanese": ["ˌdʒæpəˈniːz", "재패니즈", "일본어/일본인의"], "office": ["ˈɒfɪs", "오피스", "사무실"],
        "cheap": ["tʃiːp", "칩", "저렴한, 싼"], "laugh at": ["lɑːf æt", "래프 앳", "~을 비웃다"], 
        "fair": ["feə", "페어", "공정한"], "scared": ["skeəd", "스케어드", "겁먹은"], 
        "cello": ["ˈtʃeləʊ", "첼로", "첼로"], "wish": ["wɪʃ", "위시", "바라다"], 
        "learn": ["lɜːn", "런", "배우다"], "cover": ["ˈkʌvə", "커버", "~로 덮다"], 
        "turn": ["tɜːn", "턴", "돌다"], "finish": ["ˈfɪnɪʃ", "피니시", "끝나다, 끝내다"], 
        "pass": ["pɑːs", "패스", "지나가다"], "find": ["faɪnd", "파인드", "~을 찾다"], 
        "thief": ["θiːf", "피프", "도둑"], "lose": ["luːz", "루즈", "잃어버리다"], 
        "backpack": ["ˈbækpæk", "백팩", "책가방"], "summer vacation": ["ˈsʌmə veɪˈkeɪʃn", "썸머 베케이션", "여름 방학"], 
        "sit": ["sɪt", "시트", "앉다"], "make": ["meɪk", "메이크", "~을 ...하게 만들다"], 
        "over": ["ˈəʊvə", "오버", "~위로"], "blanket": ["ˈblæŋkɪt", "블랭킷", "담요"], 
        "go to bed": ["ɡəʊ tu bed", "고 투 베드", "잠자리에 들다"], "toy": ["tɔɪ", "토이", "장난감"], 
        "much": ["mʌtʃ", "머치", "많은"], "French": ["frentʃ", "프렌치", "프랑스의, 프랑스어의"],

        # --- PAGE 3 ---
        "rain": ["reɪn", "레인", "비가 내리다"], "choose": ["tʃuːz", "추즈", "고르다"], 
        "gloves": ["ɡlʌvz", "글러브스", "장갑(복수형)"], "wake up": ["weɪk ʌp", "웨이크 업", "~을 깨우다"], 
        "hold": ["həʊld", "홀드", "잡고 있다, 들고 있다"], "sell": ["sel", "셀", "팔다"], 
        "blow": ["bləʊ", "블로우", "불다"], "candle": ["ˈkændl", "캔들", "초, 양초"], 
        "homework": ["ˈhəʊmwɜːk", "홈워크", "숙제"], "movie star": ["ˈmuːvi stɑː", "무비 스타", "영화배우"], 
        "jog": ["dʒɒɡ", "조그", "조깅하다"], "poem": ["ˈpəʊɪm", "포엠", "시"], 
        "bake": ["beɪk", "베이크", "~을 굽다"], "newspaper": ["ˈnjuːzpeɪpə", "뉴스페이퍼", "신문"], 
        "horror": ["ˈhɒrə", "호러", "공포"], "work": ["wɜːk", "워크", "직장"], 
        "grow": ["ɡrəʊ", "그로우", "키우다"], "look for": ["lʊk fə", "룩 포", "~을 찾다"], 
        "way": ["weɪ", "웨이", "길"], "museum": ["mjuˈziːəm", "뮤지엄", "박물관"],
        "water": ["ˈwɔːtə", "워터", "물을 주다"], "island": ["ˈaɪlənd", "아일랜드", "섬"], 
        "catch": ["kætʃ", "캐치", "잡다"], "spinach": ["ˈspɪnɪtʃ", "시금치", "시금치"], 
        "build": ["bɪld", "빌드", "짓다"], "bridge": ["brɪdʒ", "브릿지", "다리"], 
        "ask": ["ɑːsk", "애스크", "묻다, 질문하다"], "classical": ["ˈklæsɪkl", "클래시컬", "고전의"], 
        "December": ["dɪˈsembə", "디셈버", "12월"], "science": ["ˈsaɪəns", "사이언스", "과학"], 
        "have dinner": ["hæv ˈdɪnə", "해브 디너", "저녁을 먹다"], "hate": ["heɪt", "헤이트", "미워하다"], 
        "fly": ["flaɪ", "플라이", "~을 날리다"], "kite": ["kaɪt", "카이트", "연"], 
        "push": ["pʊʃ", "푸쉬", "밀다"], "wash the dishes": ["wɒʃ ðə dɪʃɪz", "와쉬 더 디쉬즈", "설거지하다"], 
        "do the laundry": ["duː ðə ˈlɔːndri", "두 더 론드리", "빨래를 하다"], "bark": ["bɑːk", "바크", "짖다"], 
        "carry": ["ˈkæri", "캐리", "나르다"], "magazine": ["ˌmæɡəˈziːn", "매거진", "잡지"], 
        "go shopping": ["ɡəʊ ˈʃɒpɪŋ", "고 쇼핑", "쇼핑하러 가다"], "touch": ["tʌtʃ", "터치", "만지다"], 
        "top": ["tɒp", "탑", "꼭대기, 맨 위"], "hide": ["haɪd", "하이드", "숨기다"], 
        "treasure": ["ˈtreʒə", "트레저", "보물"], "pick up": ["pɪk ʌp", "픽 업", "~을 줍다"],
        "check": ["tʃek", "체크", "점검하다"], "chopsticks": ["ˈtʃɒpstɪks", "찹스틱스", "젓가락"], 
        "climb up": ["klaɪm ʌp", "클라임 업", "위로 올라가다"], "ladder": ["ˈlædə", "래더", "사다리"], 
        "in the future": ["ɪn ðə ˈfjuːtʃə", "인 더 퓨처", "미래에"], "ticket": ["ˈtɪkɪt", "티켓", "표"], 
        "tonight": ["təˈnaɪt", "투나잇", "오늘밤(에)"], "cartoon": ["kɑːˈtuːn", "카툰", "만화"], 
        "grape": ["ɡreɪp", "그레이프", "포도"], "front door": ["frʌnt dɔː", "프런트 도어", "현관, 정문"], 
        "have a party": ["hæv ə ˈpɑːti", "해브 어 파티", "파티를 열다"], "great": ["ɡreɪt", "그레이트", "멋진, 좋은"], 
        "fantastic": ["fænˈtæstɪk", "판타스틱", "환상적인"], "people": ["ˈpiːpl", "피플", "사람들"], 
        "wrong": ["rɒŋ", "롱", "잘못된"], "weather": ["ˈweðə", "웨더", "날씨"], 
        "melon": ["ˈmelən", "멜론", "멜론"], "dark": ["dɑːk", "다크", "어두운"], 
        "cloud": ["klaʊd", "클라우드", "구름"], "smart": ["smɑːt", "스마트", "영리한, 똑똑한"], 
        "pink": ["pɪŋk", "핑크", "분홍의"], "sour": ["ˈsaʊə", "사워", "신, 시큼한"], 
        "need": ["niːd", "니드", "필요로 하다"], "windy": ["ˈwɪndi", "윈디", "바람이 부는"], 
        "poor": ["pɔː", "푸어", "가난한"], "wise": ["waɪz", "와이즈", "현명한, 지혜로운"], 
        "soft": ["sɒft", "소프트", "부드러운"],

        # --- PAGE 4 ---
        "soap": ["səʊp", "소프", "비누"], "fresh": ["freʃ", "프레쉬", "신선한"], 
        "cheese stick": ["tʃiːz stɪk", "치즈 스틱", "치즈스틱"], "easy": ["ˈiːzi", "이지", "쉬운"], 
        "police officer": ["pəˈliːs ˈɒfɪsə", "폴리스 오피서", "경찰관"], "tired": ["ˈtaɪəd", "타이어드", "피곤한"], 
        "amazing": ["əˈmeɪzɪŋ", "어메이징", "놀라운"], "silk": ["sɪlk", "실크", "비단"], 
        "writer": ["ˈraɪtə", "라이터", "작가"], "angel": ["ˈeɪndʒl", "엔젤", "천사"], 
        "terrible": ["ˈterəbl", "테러블", "끔찍한, 안 좋은"], "singer": ["ˈsɪŋə", "싱어", "가수"],
        "often": ["ˈɒfn", "오픈", "자주, 종종"], "go to the movies": ["ɡəʊ tu ðə ˈmuːviz", "고 투 더 무비즈", "영화 보러 가다"], 
        "wonderful": ["ˈwʌndəfl", "원더풀", "근사한, 멋진"], "curious": ["ˈkjʊəriəs", "큐리어스", "궁금한"], 
        "whale": ["weɪl", "웨일", "고래"], "club": ["klʌb", "클럽", "동아리, 클럽"], 
        "president": ["ˈprezɪdənt", "프레지던트", "대통령, 사장"], "among": ["əˈmʌŋ", "어망", "~ 사이에"], 
        "spend": ["spend", "스펜드", "(시간을) 보내다"], "because of": ["bɪˈkɒz əv", "비코즈 오브", "~ 때문에"], 
        "runner": ["ˈrʌnə", "러너", "주자, 달리는 사람"], "mountain": ["ˈmaʊntən", "마운틴", "산"], 
        "subject": ["ˈsʌbdʒɪkt", "서브젝트", "과목"], "restaurant": ["ˈrestrɒnt", "레스토랑", "식당"], 
        "neighborhood": ["ˈneɪbəhʊd", "네이버후드", "이웃, 동네"], "bright": ["braɪt", "브라이트", "밝은"],
        "carefully": ["ˈkeəfəli", "케어풀리", "조심해서, 주의하여"], "by car": ["baɪ kɑː", "바이 카", "자동차로"], 
        "on weekends": ["ɒn ˌwiːkˈendz", "온 위켄즈", "주말에"], "answer": ["ˈɑːnsə", "앤서", "대답하다"], 
        "wisely": ["ˈwaɪzli", "와이즐리", "지혜롭게"], "clear": ["klɪə", "클리어", "명확한"], 
        "different": ["ˈdɪfrənt", "디퍼런트", "다른"], "silent": ["ˈsaɪlənt", "사일런트", "조용한"],
        "careful": ["ˈkeəfl", "케어풀", "조심하는"], "quiet": ["ˈkwaɪət", "콰이어트", "조용한"], 
        "quick": ["kwɪk", "퀵", "빠른, 빨리"], "trust": ["trʌst", "트러스트", "믿다, 신뢰하다"], 
        "important": ["ɪmˈpɔːtnt", "임포턴트", "중요한"], "dangerous": ["ˈ데인저러스", "데인저러스", "위험한"], 
        "soon": ["suːn", "순", "곧, 머지않아"], "near": ["nɪə", "니어", "근처의"],
        "popular": ["ˈpɒpjələ", "파퓰러", "인기 있는"], "interesting": ["ˈɪntrəstɪŋ", "인터레스팅", "흥미로운"], 
        "exciting": ["ɪkˈsaɪtɪŋ", "익사이팅", "흥미진진한"], "voice": ["vɔɪs", "보이스", "목소리"], 
        "acting": ["ˈæktɪŋ", "액팅", "행동"], "saying": ["ˈ세잉", "세잉", "말"]
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 초기화 및 UI 로직
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.prev_idx = -1
    st.session_state.is_wrong = False

st.set_page_config(page_title="영단어 777 발음 마스터", page_icon="📖")
st.title("🎓 영단어 777-3권")

# 완료 화면
if st.session_state.current_idx >= len(st.session_state.word_list):
    st.balloons()
    st.header(f"🎊 모든 단어 학습 완료!")
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
word_data = st.session_state.words_dict[current_word]
# 표시할 때 슬러시가 있다면 제거
correct_ipa = word_data[0].replace("/", "")   
correct_pron = word_data[1]  
correct_mean = word_data[2]  

# 보기 생성
if st.session_state.prev_idx != st.session_state.current_idx:
    other_means = [v[2] for k, v in st.session_state.words_dict.items() if v[2] != correct_mean]
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

# 문제 박스 (단어 색상 변경 및 발음기호 슬러시 제거)
st.markdown(f"""
<div style="background-color: #ffffff; padding: 40px; border-radius: 20px; text-align: center; border: 2px solid #e0e4e8; box-shadow: 4px 4px 15px rgba(0,0,0,0.05);">
    <h1 style="margin: 0; color: #E67E22; font-size: 4rem; font-family: 'Arial';">{current_word}</h1>
    <div style="margin-top: 20px;">
        <span style="font-size: 1.6rem; color: #7F8C8D; background-color: #F4F6F7; padding: 5px 12px; border-radius: 8px; margin-right: 10px; border: 1px solid #D5DBDB;">
            [{correct_ipa}]
        </span>
        <span style="font-size: 1.6rem; color: #2E86C1; background-color: #EBF5FB; padding: 5px 12px; border-radius: 8px; border: 1px solid #AED6F1;">
            [{correct_pron}]
        </span>
    </div>
</div>
""", unsafe_allow_html=True)
st.write("")

# 버튼 배치
col1, col2 = st.columns(2)
for i, option in enumerate(st.session_state.options):
    with col1 if i % 2 == 0 else col2:
        if st.session_state.is_wrong:
            if option == correct_mean:
                st.markdown(f"""<div style="background-color: #27ae60; color: white; padding: 18px; border-radius: 12px; text-align: center; border: 1px solid #1e8449; font-weight: bold; margin-bottom: 12px; font-size: 1.2rem;">🎯 {option}</div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""<div style="background-color: #f4f6f7; color: #bdc3c7; padding: 18px; border-radius: 12px; text-align: center; border: 1px solid #e5e8e8; margin-bottom: 12px; font-size: 1.2rem;">{option}</div>""", unsafe_allow_html=True)
        else:
            if st.button(option, key=f"btn_{st.session_state.current_idx}_{i}", use_container_width=True):
                if option == correct_mean:
                    st.session_state.score += 1
                    st.success(f"🎉 정답입니다!")
                    time.sleep(0.6)
                    st.session_state.current_idx += 1
                    st.rerun()
                else:
                    st.session_state.is_wrong = True
                    st.error(f"❌ 오답입니다!")
                    st.rerun()

# 오답 시 자동 이동
if st.session_state.is_wrong:
    time.sleep(2.0)
    st.session_state.current_idx += 1
    st.session_state.is_wrong = False
    st.rerun()

st.divider()
st.markdown(f"#### 📊 현재 학습 통계")
c1, c2 = st.columns(2)
c1.metric("현재 점수", f"{st.session_state.score}점")
c2.metric("진행도", f"{st.session_state.current_idx}/{len(st.session_state.word_list)}")
