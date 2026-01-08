import streamlit as st
import random
import time

# 1. 영단어 데이터 (발음기호 + 한글 읽기 포함)
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        "middle [ˈmɪdl] (미들)": "한가운데", "store [stɔː(r)] (스토어)": "가게, 비축하다", 
        "sound [saʊnd] (사운드)": "소리, 들리다, 건전한", "point [pɔɪnt] (포인트)": "요점, 점수, 가리키다", 
        "land [lænd] (랜드)": "땅, 육지, 착륙하다", "clone [kləʊn] (클론)": "복제생물, 복제하다", 
        "turn [tɜːrn] (턴)": "돌다, 차례, 회전", "fly [flaɪ] (플라이)": "날다, 파리", 
        "begin [bɪˈɡɪn] (비긴)": "시작하다", "grow [ɡrəʊ] (그로우)": "성장하다, 기르다, 되다", 
        "believe [bɪˈliːv] (빌리브)": "믿다", "worry [ˈwɜːri] (워리)": "걱정시키다", 
        "save [seɪv] (세이브)": "구하다, 저축하다, 절약하다", "easy [ˈiːzi] (이지)": "쉬운, 편한", 
        "poor [pɔː(r)] (푸어)": "가난한, 불쌍한", "such [sʌtʃ] (서치)": "그러한", 
        "own [əʊn] (오운)": "자신의, 소유하다", "fast [fæst] (패스트)": "빨리, 단단히", 
        "back [bæk] (백)": "뒤, 등", "always [ˈɔːlweɪz] (올웨이즈)": "늘, 언제나", 
        "history [ˈhɪstri] (히스트리)": "역사", "state [steɪt] (스테이트)": "국가, 상태", 
        "soldier [ˈsəʊldʒə(r)] (솔져)": "군인", "village [ˈvɪlɪdʒ] (빌리지)": "마을", 
        "office [ˈɒfɪs] (오피스)": "사무실", "island [ˈaɪlənd] (아일랜드)": "섬", 
        "piece [piːs] (피스)": "조각", "grade [ɡreɪd] (그레이드)": "성적, 등급, 학년", 
        "spring [sprɪŋ] (스프링)": "봄, 용수철", "rock [rɒk] (락)": "바위, 흔들다", 
        "line [laɪn] (라인)": "선, 줄을 서다", "cook [kʊk] (쿡)": "요리사, 요리하다", 
        "fall [fɔːl] (폴)": "떨어지다, 가을", "exercise [ˈeksəsaɪz] (엑서사이즈)": "운동, 연습(하다)", 
        "end [end] (엔드)": "끝(나다)", "front [frʌnt] (프런트)": "앞의", 
        "second [ˈsekənd] (세컨드)": "제2의, 초, 잠깐", "few [fjuː] (퓨)": "소수의, 조금의", 
        "both [bəʊθ] (보스)": "양쪽, 둘 다의", "happen [ˈhæpən] (해픈)": "일어나다, 우연히 ~하다", 
        "leave [liːv] (리브)": "떠나다, 내버려두다", "remember [rɪˈmembə(r)] (리멤버)": "기억하다", 
        "wear [weər] (웨어)": "입다, 쓰다, 착용하다", "move [muːv] (무브)": "움직이다, 감동시키다", 
        "send [send] (샌드)": "보내다", "TRUE [truː] (트루)": "진짜의, 참된", 
        "hot [hɒt] (핫)": "뜨거운, 매운", "early [ˈɜːli] (얼리)": "초기의, 일찍", 
        "often [ˈɒfn] (오픈)": "종종, 자주", "sometimes [ˈsʌmtaɪmz] (썸타임즈)": "때때로", 
        "pet [pet] (펫)": "애완동물", "vegetable [ˈvedʒtəbl] (베지터블)": "채소, 야채", 
        "leaf [liːf] (리프)": "잎", "forest [ˈfɒrɪst] (포레스트)": "숲", 
        "area [ˈeəriə] (에어리어)": "지역, 분야", "neighbor [ˈneɪbə(r)] (네이버)": "이웃", 
        "art [ɑːrt] (아트)": "미술, 예술", "poem [ˈpəʊɪm] (포엠)": "시", 
        "subject [ˈsʌbdʒɪkt] (서브젝트)": "과목, 주제", "bottle [ˈbɒtl] (바틀)": "병", 
        "machine [məˈʃiːn] (머신)": "기계", "fact [fækt] (팩트)": "사실", 
        "rule [ruːl] (룰)": "규칙, 지배(하다)", "break [breɪk] (브레이크)": "깨뜨리다, 휴식", 
        "check [tʃek] (체크)": "점검(하다)", "stay [steɪ] (스테이)": "머무르다, ~인 채로 있다", 
        "cold [kəʊld] (콜드)": "추운, 감기", "bring [brɪŋ] (브링)": "가져(데려)오다", 
        "build [bɪld] (빌드)": "짓다, 건축하다", "join [dʒɔɪn] (조인)": "가입하다", 
        "lose [luːz] (루즈)": "잃다, 지다", "die [daɪ] (다이)": "죽다", 
        "large [lɑːrdʒ] (라지)": "큰, 넓은", "sick [sɪk] (식)": "병든, 아픈", 
        "busy [ˈbɪzi] (비지)": "바쁜, 번화한", "real [ˈriːəl] (리얼)": "진짜의, 현실의", 
        "most [məʊst] (모스트)": "대부분, 가장", "late [leɪt] (레이트)": "늦은, 늦게", 
        "together [təˈɡeðə(r)] (투게더)": "함께, 같이", "even [ˈiːvn] (이븐)": "~조차, 더욱~", 
        "health [helθ] (헬스)": "건강", "holiday [ˈhɒlədeɪ] (할리데이)": "공휴일", 
        "gift [ɡɪft] (기프트)": "선물, 타고난 재능", "field [fiːld] (필드)": "들판, 경기장, 분야", 
        "site [saɪt] (사이트)": "장소, 현장, 웹사이트", "goal [ɡəʊl] (골)": "목표, 골", 
        "effect [ɪˈfekt] (이펙트)": "영향, 결과, 효과", "sign [saɪn] (사인)": "표지, 신호, 서명하다", 
        "report [rɪˈpɔːrt] (리포트)": "보고하다", "order [ˈɔːrdə(r)] (오더)": "순서, 질서, 명령(하다)", 
        "experience [ɪkˈspɪəriəns] (익스피어리언스)": "경험(하다)", "result [rɪˈzʌlt] (리절트)": "결과", 
        "ride [raɪd] (라이드)": "타다, 타기", "wish [wɪʃ] (위시)": "바라다, 소원", 
        "half [hɑːf] (하프)": "절반의", "past [pɑːst] (패스트)": "지나간, 과거", 
        "carry [ˈkæri] (캐리)": "가지고 가다, 나르다", "draw [drɔː] (드로우)": "그리다, 끌다", 
        "spend [spend] (스펜드)": "(시간, 돈을) 쓰다", "wait [weɪt] (웨이트)": "기다리다"
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 초기화 및 UI 로직
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.prev_idx = -1
    st.session_state.is_wrong = False

st.set_page_config(page_title="중학 영단어 퀴즈! (101-200)", page_icon="⭐")
st.title("🎡 매일 영단어 2")

# 완료 화면
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

# 현재 문제 설정
current_word = st.session_state.word_list[st.session_state.current_idx]
correct_mean = st.session_state.words_dict[current_word]

# 보기 생성 (문제 바뀔 때 한 번만)
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
st.markdown(f"#### 📈 실시간 성적: **{st.session_state.score}** / {st.session_state.current_idx}")

