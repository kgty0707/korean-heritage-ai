<div contenteditable="true" translate="no" class="ProseMirror"><h1>🏺 문화유산 해설 AI '뮤즈(Muse)'</h1>
  <p><strong>
    [말평 AI 공모전 사이드](https://korean-heritage-ai-immso9h8m5mkg2ru6hcont.streamlit.app)
  </strong></p>
  <h2>📖 프로젝트 소개</h2>
  <img width="1893" height="840" alt="image" src="https://github.com/user-attachments/assets/457dc2a6-3d70-459b-9a12-8f2ca5cbc801" />


  <p>'뮤즈(Muse)'는 e뮤지엄의 방대한 유물 데이터를 학습하여, 누구나 쉽게 문화유산 정보를 이해할 수 있도록 돕는 AI 해설 서비스입니다. 사용자가 유물 이름을 입력하면, AI가 해당 유물의 역사적 배경, 특징, 가치 등을 알기 쉽게 설명해 줍니다.</p><p>본 프로젝트는 공공데이터포털의 <a href="https://www.data.go.kr/data/15104964/openapi.do" title="null">e뮤지엄 소장품 조회 API</a>를 활용하여 구축될 예정이며, 이 웹페이지는 기능 구현에 앞서 제작된 프로토타입입니다.</p><h2>✨ 주요 기능 (구현 예정)</h2><ul><li><p><strong>자연어 기반 유물 검색</strong>: 키워드만으로 원하는 유물을 쉽게 찾을 수 있습니다.</p></li><li><p><strong>AI 기반 상세 해설</strong>: 유물의 핵심 정보를 요약하고, 역사적 맥락을 더해 깊이 있는 해설을 제공합니다.</p></li><li><p><strong>연관 유물 추천</strong>: 현재 보고 있는 유물과 관련된 다른 유물을 추천하여 학습의 폭을 넓혀줍니다.</p></li><li><p><strong>이미지 분석</strong>: 유물 이미지를 분석하여 시각적 특징에 대한 설명을 제공합니다.</p></li></ul><h2>🚀 로컬에서 실행하기</h2><ol><li><p>저장소를 클론합니다.</p><pre><code>git clone https://github.com/kgty0707/korean-heritage-ai.git
cd korean-heritage-ai
<br class="ProseMirror-trailingBreak"></code></pre></li><li><p>필요한 라이브러리를 설치합니다.</p><pre><code>pip install -r requirements.txt
<br class="ProseMirror-trailingBreak"></code></pre></li><li><p>Streamlit 앱을 실행합니다.</p><pre><code>streamlit run app.py
<br class="ProseMirror-trailingBreak"></code></pre></li></ol></div>
