import streamlit as st
# カスタムCSSを定義
custom_css = """
<style>
    .tighter {
        line-height: 1.3; /* 行間を狭めるための値。適宜調整してください */
    }
</style>
"""

st.title('お問い合わせ')

st.markdown('#')

text = '''
<p class="tighter">
お問い合わせは以下の公式ラインに「お問い合わせ」とメッセージをお送りください。<br>
「お問合せフォーム」が送信されますので、そちらにご回答いただくと、<br>
1~2営業日で担当の者より折り返し連絡いたします。<br><br>
</p>
'''

st.markdown(text, unsafe_allow_html=True)

# カラムを作成（左、中央、右）
left, center, right = st.columns([1,2,1])

# 画像のURL
image_url = "https://qr-official.line.me/gs/M_576wzpqr_GW.png?oat__id=3591290&oat_content=qr"

# URL
url = "https://lin.ee/OADYhnz"

# 中央のカラムに画像を表示
with left:
    # カスタムHTMLとCSSを使用して画像を中央寄せにする
    st.markdown("""
        <style>
            .centered-image {
                display: flex;
                justify-content: center;
            }
        </style>
        <div class="centered-image">
            <img src="https://qr-official.line.me/gs/M_576wzpqr_GW.png?oat__id=3591290&oat_content=qr" width="200px">
        </div>
        """, unsafe_allow_html=True)
    
    # URLも中央寄せで表示
    st.markdown("""
        <div style="text-align: center;">
            <a href="https://lin.ee/OADYhnz" target="_blank">https://lin.ee/OADYhnz</a>
        </div>
        """, unsafe_allow_html=True)
