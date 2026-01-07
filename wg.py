import streamlit as st
import random
import time

# 1. 영단어 데이터 (발음기호 포함)
if 'words_dict' not in st.session_state:
    st.session_state.words_dict = {
        "middle [ˈmɪdl]": "한가운데", "store [stɔː(r)]": "가게, 비축하다", "sound [saʊnd]": "소리, 들리다, 건전한", "point [pɔɪnt]": "요점, 점수, 가리키다", "land [lænd]": "땅, 육지, 착륙하다", "clone [kləʊn]": "복제생물, 복제하다", "turn [tɜːrn]": "돌다, 차례, 회전", "fly [flaɪ]": "날다, 파리", "begin [bɪˈɡɪn]": "시작하다", "grow [ɡrəʊ]": "성장하다, 기르다, 되다", "believe [bɪˈliːv]": "믿다", "worry [ˈwɜːri]": "걱정시키다", "save [seɪv]": "구하다, 저축하다, 절약하다", "easy [ˈiːzi]": "쉬운, 편한", "poor [pɔː(r)]": "가난한, 불쌍한", "such [sʌtʃ]": "그러한", "own [əʊn]": "자신의, 소유하다", "fast [fæst]": "빨리, 단단히", "back [bæk]": "뒤, 등", "always [ˈɔːlweɪz]": "늘, 언제나", "history [ˈhɪstri]": "역사", "state [steɪt]": "국가, 상태", "soldier [ˈsəʊldʒə(r)]": "군인", "village [ˈvɪlɪdʒ]": "마을", "office [ˈɒfɪs]": "사무실", "island [ˈaɪlənd]": "섬", "piece [piːs]": "조각", "grade [ɡreɪd]": "성적, 등급, 학년", "spring [sprɪŋ]": "봄, 용수철", "rock [rɒk]": "바위, 흔들다", "line [laɪn]": "선, 줄을 서다", "cook [kʊk]": "요리사, 요리하다", "fall [fɔːl]": "떨어지다, 가을", "exercise [ˈeksəsaɪz]": "운동, 연습(하다)", "end [end]": "끝(나다)", "front [frʌnt]": "앞의", "second [ˈsekənd]": "제2의, 초, 잠깐", "few [fjuː]": "소수의, 조금의", "both [bəʊθ]": "양쪽, 둘 다의", "happen [ˈhæpən]": "일어나다, 우연히 ~하다", "leave [liːv]": "떠나다, 내버려두다", "remember [rɪˈmembə(r)]": "기억하다", "wear [weər]": "입다, 쓰다, 착용하다", "move [muːv]": "움직이다, 감동시키다", "send [send]": "보내다", "TRUE [truː]": "진짜의, 참된", "hot [hɒt]": "뜨거운, 매운", "early [ˈɜːli]": "초기의, 일찍", "often [ˈɒfn]": "종종, 자주", "sometimes [ˈsʌmtaɪmz]": "때때로", "pet [pet]": "애완동물", "vegetable [ˈvedʒtəbl]": "채소, 야채", "leaf [liːf]": "잎", "forest [ˈfɒrɪst]": "숲", "area [ˈeəriə]": "지역, 분야", "neighbor [ˈneɪbə(r)]": "이웃", "art [ɑːrt]": "미술, 예술", "poem [ˈpəʊɪm]": "시", "subject [ˈsʌbdʒɪkt]": "과목, 주제", "bottle [ˈbɒtl]": "병", "machine [məˈʃiːn]": "기계", "fact [fækt]": "사실", "rule [ruːl]": "규칙, 지배(하다)", "break [breɪk]": "깨뜨리다, 휴식", "check [tʃek]": "점검(하다)", "stay [steɪ]": "머무르다, ~인 채로 있다", "cold [kəʊld]": "추운, 감기", "bring [brɪŋ]": "가져(데려)오다", "build [bɪld]": "짓다, 건축하다", "join [dʒɔɪn]": "가입하다", "lose [luːz]": "잃다, 지다", "die [daɪ]": "죽다", "large [lɑːrdʒ]": "큰, 넓은", "sick [sɪk]": "병든, 아픈", "busy [ˈbɪzi]": "바쁜, 번화한", "real [ˈriːəl]": "진짜의, 현실의", "most [məʊst]": "대부분, 가장", "late [leɪt]": "늦은, 늦게", "together [təˈɡeðə(r)]": "함께, 같이", "even [ˈiːvn]": "~조차, 더욱~", "health [helθ]": "건강", "holiday [ˈhɒlədeɪ]": "공휴일", "gift [ɡɪft]": "선물, 타고난 재능", "field [fiːld]": "들판, 경기장, 분야", "site [saɪt]": "장소, 현장, 웹사이트", "goal [ɡəʊl]": "목표, 골", "effect [ɪˈfekt]": "영향, 결과, 효과", "sign [saɪn]": "표지, 신호, 서명하다", "report [rɪˈpɔːrt]": "보고하다", "order [ˈɔːrdə(r)]": "순서, 질서, 명령(하다)", "experience [ɪkˈspɪəriəns]": "경험(하다)", "result [rɪˈzʌlt]": "결과", "ride [raɪd]": "타다, 타기", "wish [wɪʃ]": "바라다, 소원", "half [hɑːf]": "절반의", "past [pɑːst]": "지나간, 과거", "carry [ˈkæri]": "가지고 가다, 나르다", "draw [drɔː]": "그리다, 끌다", "spend [spend]": "(시간, 돈을) 쓰다", "wait [weɪt]": "기다리다"
    }
    st.session_state.word_list = list(st.session_state.words_dict.keys())
    random.shuffle(st.session_state.word_list)

# 2. 초기화 및 UI 로직 (이전과 동일)
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.prev_idx = -1
    st.session_state.is_wrong = False

st.set_page_config(page_title="중학 영단어 퀴즈! (101-200)", page_icon="⭐")
st.title("🎡 매일 영단어 (101-200)")

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

st.write(f"### 문제 {st.session_state.current_idx + 1} / {len(st.session_state.word_list)}")
st.progress((st.session_state.current_idx) / len(st.session_state.word_list))
st.info(f"다음 단어의 뜻은? \n\n ## **[ {current_word} ]**")

col1, col2 = st.columns(2)
for i, option in enumerate(st.session_state.options):
    with col1 if i % 2 == 0 else col2:
        if st.session_state.is_wrong:
            if option == correct_mean:
                st.markdown(f"""<div style="background-color: #ff4b4b; color: white; padding: 10px; border-radius: 5px; text-align: center; border: 2px solid #b22222; font-weight: bold; margin-bottom: 10px;">🎯 {option} (정답)</div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""<div style="background-color: #f0f2f6; color: #a3a8b4; padding: 10px; border-radius: 5px; text-align: center; border: 1px solid #dcdde1; margin-bottom: 10px;">{option}</div>""", unsafe_allow_html=True)
        else:
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

if st.session_state.is_wrong:
    time.sleep(2.0)
    st.session_state.current_idx += 1
    st.session_state.is_wrong = False
    st.rerun()

st.divider()
st.markdown(f"#### 📈 실시간 성적: **{st.session_state.score}** / {st.session_state.current_idx}")
