import streamlit as st
import random
import time

# 1. 단어 데이터 세션 관리 (4권 전체단어.pdf 내용 반영)
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        # PAGE 1
        "bring": ["brɪŋ", "브링", "가지고 가다"], "stop by": ["stɒp baɪ", "스탑 바이", "~에 들르다"],
        "for a minute": ["fɔːr ə ˈmɪnɪt", "포 어 미닛", "잠시 동안"], "wait": ["weɪt", "웨이트", "기다리다"],
        "phone number": ["fəʊn ˈnʌmbə", "폰 넘버", "전화번호"], "watch": ["wɒtʃ", "와치", "지켜보다"],
        "pass": ["pɑːs", "패스", "건네주다"], "ball": ["bɔːl", "볼", "공"],
        "lend": ["lend", "렌드", "빌려주다"], "mall": ["mɔːl", "몰", "상가, 상점"],
        "fix": ["fɪks", "픽스", "고치다"], "loud": ["laʊd", "라우드", "크게"],
        "quiet": ["ˈkwaɪət", "콰이어트", "조용한"], "late": ["leɪt", "레이트", "늦게"],
        "coin": ["kɔɪn", "코인", "동전"], "change": ["tʃeɪndʒ", "체인지", "잔돈"],
        "take care of": ["teɪk keər əv", "테이크 케어 오브", "~을 보살피다"], "throw": ["θrəʊ", "드로우", "던지다"],
        "turn off": ["tɜːn ɒf", "턴 오프", "끄다"], "first": ["fɜːst", "퍼스트", "우선"],
        # PAGE 2
        "pool": ["puːl", "풀", "수영장"], "meeting": ["ˈmiːtɪŋ", "미팅", "회의"],
        "pick up": ["pɪk ʌp", "픽 업", "~을 태우러 가다"], "steak": ["steɪk", "스테이크", "스테이크"],
        "laundry": ["ˈlɔːndri", "론드리", "빨래"], "order": ["ˈɔːdə", "오더", "주문하다"],
        "meat": ["miːt", "미트", "고기"], "fry": ["fraɪ", "프라이", "튀기다"],
        "office": ["ˈɒfɪs", "오피스", "사무실"], "break": ["breɪk", "브레이크", "휴식"],
        "passport": ["ˈpɑːspɔːt", "패스포트", "여권"], "business card": ["ˈbɪznəs kɑːd", "비즈니스 카드", "명함"],
        "laptop": ["ˈlæptɒp", "랩탑", "노트북 컴퓨터"], "check": ["tʃek", "체크", "검사하다, 체크하다"],
        "something": ["ˈsʌmθɪŋ", "썸씽", "어떤 것, 무엇"], "outside": ["ˌaʊtˈsaɪd", "아웃사이드", "밖에서"],
        "see a doctor": ["siː ə ˈdɒktə", "씨 어 닥터", "진찰을 받다"], "skip": ["skɪp", "스킵", "빠지다"],
        "respect": ["rɪˈspekt", "리스펙트", "존경하다"], "by yourself": ["baɪ jɔːˈself", "바이 유어셀프", "너 혼자서"],
        "by": ["baɪ", "바이", "~까지"], "keep": ["kiːp", "킵", "지키다, 준수하다"],
        "rule": ["ruːl", "룰", "규칙, 규정"], "hate": ["heɪt", "헤이트", "미워하다"],
        "cross": ["krɒs", "크로스", "건너다"], "take a shower": ["teɪk ə ˈʃaʊə", "테이크 어 샤워", "샤워하다"],
        # PAGE 3
        "player": ["ˈpleɪə", "플레이어", "선수"], "shelf": ["ʃelf", "쉘프", "선반"],
        "bowl": ["bəʊl", "보울", "그릇, 사발"], "language": ["ˈlæŋɡwɪdʒ", "랭귀지", "언어"],
        "waste": ["weɪst", "웨이스트", "낭비하다"], "pepper": ["ˈpepə", "페퍼", "후추"],
        "cousin": ["ˈkʌzn", "커즌", "사촌"], "bake": ["beɪk", "베이크", "빵을 굽다"],
        "ant": ["ænt", "앤트", "개미"], "hole": ["həʊl", "홀", "구멍"],
        "beer": ["bɪə", "비어", "맥주"], "phone": ["fəʊn", "폰", "전화기"],
        "coke": ["kəʊk", "코크", "콜라"], "close friend": ["kləʊs frend", "클로스 프렌드", "절친한 친구"],
        "honey": ["ˈhʌni", "허니", "꿀"], "refrigerator": ["rɪˈfrɪdʒəreɪtə", "리프리지레이터", "냉장고"],
        "rice": ["raɪs", "라이스", "쌀밥"], "sunlight": ["ˈsʌnlaɪt", "썬라이트", "햇빛"],
        "nephew": ["ˈnefjuː", "네퓨", "남자 조카"], "oil": ["ɔɪl", "오일", "기름"],
        # PAGE 4
        "dish": ["dɪʃ", "디쉬", "음식"], "ticket": ["ˈtɪkɪt", "티켓", "표, 티켓"],
        "trouble": ["ˈtrʌbl", "트러블", "문제"], "advice": ["ədˈvaɪs", "어드바이스", "충고, 조언"],
        "bought": ["bɔːt", "보트", "샀다"], "hope": ["həʊp", "호프", "희망"],
        "medicine": ["ˈmedsn", "메디슨", "약"], "dessert": ["dɪˈzɜːt", "디저트", "후식"],
        "help": ["help", "헬프", "도움"], "plan": ["plæn", "플랜", "계획"],
        "wine": ["waɪn", "와인", "포도주, 와인"], "tower": ["ˈtaʊə", "타워", "탑, 타워"],
        "postcard": ["ˈpəʊstkɑːd", "포스트카드", "엽서"], "family number": ["ˈfæmɪli ˈnʌmbə", "패밀리 넘버", "식구, 가족 구성원"],
        "take": ["teɪk", "테이크", "(수업 등을) 듣다"], "magazine": ["ˌmæɡəˈziːn", "매거진", "잡지"],
        "need": ["niːd", "니드", "필요하다"], "cloud": ["klaʊd", "클라우드", "구름"],
        "robot": ["ˈrəʊbɒt", "로봇", "로봇"], "liter": ["ˈliːtə", "리터", "리터"],
        # PAGE 5
        "exercise": ["ˈeksəsaɪz", "엑서사이즈", "운동하다"], "science": ["ˈsaɪəns", "사이언스", "과학"],
        "miss": ["mɪs", "미스", "놓치다"], "prefer": ["prɪˈfɜː", "프리퍼", "~을 더 좋아하다"],
        "bacon": ["ˈbeɪkən", "베이컨", "베이컨"], "sleepy": ["ˈsliːpi", "슬리피", "졸린"],
        "still": ["stɪl", "스틸", "여전히"], "be born": ["bi bɔːn", "비 본", "태어나다"],
        "have fun": ["hæv fʌn", "해브 펀", "재미있게 놀다"], "noon": ["nuːn", "눈", "정오"],
        "go skiing": ["ɡəʊ ˈskiːɪŋ", "고 스키잉", "스키 타러 가다"], "end": ["end", "엔드", "끝나다"],
        "swam": ["swæm", "스웸", "수영했다"], "be done": ["bi dʌn", "비 던", "끝나다"],
        "midnight": ["ˈmɪdnaɪt", "미드나잇", "자정"], "go on a trip": ["ɡəʊ ɒn ə trɪp", "고 온 어 트립", "여행가다"],
        "return": ["rɪˈtɜːn", "리턴", "돌려주다"],
        # PAGE 6
        "concert": ["ˈkɒnsət", "콘서트", "음악회"], "music hall": ["ˈmjuːzɪk hɔːl", "뮤직 홀", "음악당"],
        "bee": ["biː", "비", "벌"], "butterfly": ["ˈbʌtəflaɪ", "버터플라이", "나비"],
        "country": ["ˈkʌntri", "컨트리", "나라, 국가"], "hide": ["haɪd", "하이드", "숨다"],
        "garden": ["ˈɡɑːdn", "가든", "정원"], "cafeteria": ["ˌkæfəˈtɪəriə", "카페테리아", "구내식당"],
        "fire station": ["ˈfaɪə ˌsteɪʃn", "파이어 스테이션", "소방서"], "convenience store": ["kənˈviːniəns stɔː", "컨비니언스 스토어", "편의점"],
        "gym": ["dʒɪm", "짐", "체육관"], "suddenly": ["ˈsʌdənli", "써든리", "갑자기"],
        "each other": ["iːtʃ ˈʌðə", "이치 아더", "서로"], "mouse": ["maʊs", "마우스", "생쥐"],
        "hang": ["hæŋ", "행", "걸다, 매달다"], "road": ["rəʊd", "로드", "길"],
        "stairs": ["steəz", "스테어즈", "계단"], "dolphin": ["ˈdɒlfɪn", "돌핀", "돌고래"],
        "famous": ["ˈfeɪməs", "페이머스", "유명한"], "climb": ["klaɪm", "클라임", "오르다, 올라가다"],
        "rode": ["rəʊd", "로드", "탔다"], "hill": ["hɪl", "힐", "언덕"],
        "nest": ["nest", "네스트", "둥지"], "flow": ["fləʊ", "플로우", "흐르다"],
        "pocket": ["ˈpɒkɪt", "포켓", "주머니"], "beach": ["biːtʃ", "비치", "해변"],
        "people": ["ˈpiːpl", "피플", "사람들"],
        # PAGE 7
        "backpack": ["ˈbækpæk", "백팩", "배낭"], "stage": ["steɪdʒ", "스테이지", "무대"],
        "near": ["nɪə", "니어", "~ 근처에"], "pillow": ["ˈpɪləʊ", "필로우", "베개"],
        "flour": ["ˈflaʊə", "플라워", "밀가루"], "pot": ["pɒt", "팟", "냄비"],
        "backyard": ["ˌbækˈjɑːd", "백야드", "뒷마당"], "plate": ["pleɪt", "플레이트", "접시"],
        "subway station": ["ˈsʌbweɪ ˈsteɪʃn", "서브웨이 스테이션", "지하철역"], "onion": ["ˈʌnjən", "어니언", "양파"],
        "doughnut": ["ˈdəʊnʌt", "도넛", "도넛"], "jar": ["dʒɑː", "자", "단지, 병"],
        "vegetable": ["ˈvedʒtəbl", "베지터블", "채소"]
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 초기 세션 상태 설정
if 'score' not in st.session_state: st.session_state.score = 0
if 'current_idx' not in st.session_state: st.session_state.current_idx = 0
if 'is_wrong' not in st.session_state: st.session_state.is_wrong = False
if 'options' not in st.session_state: st.session_state.options = []

st.set_page_config(page_title="영단어 777", page_icon="📖")
st.title("🎓 영단어 777-4권")

# 완료 화면
if st.session_state.current_idx >= len(st.session_state.word_list):
    st.balloons()
    st.header(f"🎊 모든 학습 완료!")
    st.subheader(f"최종 점수: {st.session_state.score} / {len(st.session_state.word_list)}")
    if st.button("처음부터 다시 하기"):
        st.session_state.score = 0
        st.session_state.current_idx = 0
        random.shuffle(st.session_state.word_list)
        st.session_state.options = []
        st.rerun()
    st.stop()

# 현재 단어 데이터 추출
current_word = st.session_state.word_list[st.session_state.current_idx]
word_data = st.session_state.words_dict[current_word]
ipa = word_data[0]
pronunciation = word_data[1]
correct_meaning = word_data[2]

# 보기 생성
if not st.session_state.options:
    other_meanings = [v[2] for k, v in st.session_state.words_dict.items() if v[2] != correct_meaning]
    st.session_state.options = random.sample(list(set(other_meanings)), 3) + [correct_meaning]
    random.shuffle(st.session_state.options)

# UI 레이아웃
st.write(f"### 문제 {st.session_state.current_idx + 1} / {len(st.session_state.word_list)}")
st.progress((st.session_state.current_idx) / len(st.session_state.word_list))

# 문제 박스
st.markdown(f"""
<div style="background-color: #f0f7ff; padding: 40px; border-radius: 20px; text-align: center; border: 2px solid #3498db; box-shadow: 4px 4px 15px rgba(0,0,0,0.05);">
    <h1 style="margin: 0; color: #2980b9; font-size: 4rem; font-family: 'Arial';">{current_word}</h1>
    <div style="margin-top: 20px;">
        <span style="font-size: 1.6rem; color: #5d6d7e; background-color: #ffffff; padding: 5px 12px; border-radius: 8px; margin-right: 10px; border: 1px solid #d5dbdb;">
            [{ipa}]
        </span>
        <span style="font-size: 1.6rem; color: #2980b9; background-color: #e3f2fd; padding: 5px 12px; border-radius: 8px; border: 1px solid #bbdefb;">
            {pronunciation}
        </span>
    </div>
</div>
""", unsafe_allow_html=True)
st.write("")

# 보기 버튼
col1, col2 = st.columns(2)
for i, option in enumerate(st.session_state.options):
    with col1 if i % 2 == 0 else col2:
        if st.session_state.is_wrong:
            if option == correct_meaning:
                st.markdown(f'<div style="background-color: #27ae60; color: white; padding: 18px; border-radius: 12px; text-align: center; font-weight: bold; margin-bottom: 12px;">🎯 {option}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="background-color: #f4f6f7; color: #bdc3c7; padding: 18px; border-radius: 12px; text-align: center; margin-bottom: 12px;">{option}</div>', unsafe_allow_html=True)
        else:
            if st.button(option, key=f"btn_{i}", use_container_width=True):
                if option == correct_meaning:
                    st.session_state.score += 1
                    st.success("🎉 정답!")
                    time.sleep(0.8)
                    st.session_state.current_idx += 1
                    st.session_state.options = []
                    st.rerun()
                else:
                    st.session_state.is_wrong = True
                    st.error("❌ 오답!")
                    st.rerun()

# 오답 시 지연 후 다음 문제로 이동
if st.session_state.is_wrong:
    time.sleep(2.0)
    st.session_state.current_idx += 1
    st.session_state.is_wrong = False
    st.session_state.options = []
    st.rerun()

st.divider()
st.metric("현재 점수", f"{st.session_state.score} / {st.session_state.current_idx}")
