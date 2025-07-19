import streamlit as st
import pandas as pd
import time

# -------------------- 페이지 기본 설정 --------------------
st.set_page_config(
    page_title="문화유산 해설 AI '뮤즈'",
    page_icon="🏺",
    layout="wide",
)

# -------------------- 예시 데이터 --------------------
mock_data = {
    '유물 고유 ID': 'PS0100200100100384000000',
    '유물 명칭': '청자 상감운학문 매병',
    '소장 기관': '간송미술관',
    '시대 정보': '고려',
    '재질 정보': '청자',
    '크기 정보': '높이 42.1cm, 입지름 6.2cm, 밑지름 17.0cm',
    '지정문화재': '국보',
    '대표 이미지': './data/2020-AP-1-019-007-청자상감운학문매병-0002.jpg', # 예시 이미지 URL
    '유물 설명': (
        "고려 상감청자의 정수로 꼽히는 작품입니다. "
        "유려한 S자 곡선을 그리는 형태와 전면에 가득 찬 구름과 학 무늬가 특징입니다. "
        "학은 하늘을 향해 날아오르는 모습과 아래를 향하는 모습을 교차로 배치하여 "
        "생동감과 공간감을 극대화했습니다. 이러한 정교하고 아름다운 상감 기법은 "
        "고려청자 중에서도 최고의 수준을 보여주는 명품으로 평가받고 있습니다."
    )
}

# -------------------- 사이드바 --------------------
with st.sidebar:
    st.title("🖼️ 문화유산 해설 AI")
    st.header("뮤즈 (Muse)")
    st.markdown("---")
    st.write(
        """
        **'말평 AI 공모전' 출품작**

        e뮤지엄의 방대한 유물 데이터를 학습한
        문화유산 전문 AI 해설 서비스입니다.
        """
    )
    st.markdown("---")
    st.info("궁금한 유물의 이름을 검색해 보세요!")


# -------------------- 메인 화면 --------------------
st.title("🏺 문화유산 정보를 AI가 알기 쉽게 설명해 드려요")
st.write("") # 공백

# --- 검색창 ---
query = st.text_input(
    label="**유물 이름을 입력하세요**",
    placeholder="예시) 청자 상감운학문 매병",
    value="청자 상감운학문 매병" # 기본값으로 예시 입력
)

if st.button("✨ AI 설명 보기"):
    if query:
        with st.spinner('AI가 유물 정보를 검색하고 설명을 생성하는 중입니다...'):
            time.sleep(2) # 2초 동안 대기

        st.markdown("---")
        st.header(f"'{query}'에 대한 AI 해설")
        
        col1, col2 = st.columns([1, 1.5]) # 화면을 두 개의 열로 분할

        with col1:
            st.image(mock_data['대표 이미지'], caption=mock_data['유물 명칭'])

        with col2:
            st.subheader("기본 정보")
            # DataFrame을 사용하여 기본 정보를 표로 깔끔하게 표시
            info_df = pd.DataFrame({
                "항목": ["소장 기관", "시대", "재질", "크기", "지정문화재"],
                "내용": [
                    mock_data['소장 기관'],
                    mock_data['시대 정보'],
                    mock_data['재질 정보'],
                    mock_data['크기 정보'],
                    mock_data['지정문화재']
                ]
            })
            st.table(info_df.set_index("항목"))

            st.subheader("AI가 생성한 유물 해설")
            st.write(mock_data['유물 설명'])
    else:
        st.warning("유물 이름을 입력해주세요!")
