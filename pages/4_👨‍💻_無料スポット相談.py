import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(layout="wide")

# ページタイトル
st.title('60分無料スポット相談の予約')

# 説明テキスト
# カスタムCSSを定義
custom_css = """
<style>
    .tighter {
        line-height: 1.3; /* 行間を狭めるための値。適宜調整してください */
    }
</style>
"""

# カスタムCSSを適用する
st.markdown(custom_css, unsafe_allow_html=True)

# カスタムCSSを適用したテキストを表示
text = '''
<p class="tighter">
SAKIYOMI 投稿作成AIをご契約された方は、専門スタッフによるスポット相談を毎月1回まで無料でご利用いただけます。(1回60分)<br><br>
「操作がよくわからない」<br>
「思ったような台本が生成されない」<br>
「自分のアカウントだったら、どういう生成指示が適切かわからない」<br><br>
こういったお悩みを解決いたします。<br>
上記にないお悩みも幅広く対応させていただきます。<br><br>
下記のカレンダーよりご都合の良い日時を1つご選択ください。<br><br>
※毎月1回のコンサル回数は繰り越されず、次月1日にリセットされます。
</p>
'''

st.markdown(text, unsafe_allow_html=True)

st.markdown('<hr style="border: 0; border-top: 3px solid #EFF2F6;">', unsafe_allow_html=True)

# Timerexの埋め込みコードをここに貼り付ける
timerex_widget_code = '''
<!-- Begin TimeRex Widget -->
<div id="timerex_calendar" data-url="https://timerex.net/s/ai.cs_5bad/48fc91f8"></div>

<script id="timerex_embed" src="https://asset.timerex.net/js/embed.js"></script>

<script type="text/javascript">
  TimerexCalendar();
</script>
<!-- End TimeRex Widget -->
'''

# Streamlitページにウィジェットを埋め込む
html(timerex_widget_code, height=1000)

st.markdown('<hr style="border: 0; border-top: 3px solid #EFF2F6;">', unsafe_allow_html=True)
