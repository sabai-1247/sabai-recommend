import streamlit as st

st.set_page_config(
    page_title="りらっくすサバーイ - お悩み別おすすめコース診断",
    page_icon="🌿",
)

# --- リンク設定 ---
SQUARE_URL = "https://book.squareup.com/appointments/2ucwqsu1n3gd92/location/NTCS8DNYBQTPS/services"
LINE_URL = "https://lin.ee/NC5Kp1j"


# --- UI表示 ---
st.title("🌿 りらっくすサバーイ")
st.subheader("あなたにピッタリの施術コース診断")
st.write(
    "本日のお身体の状態やお悩みにチェックを入れると、最適なおすすめコースをご提案します（約10秒）。"
)

st.markdown("---")

st.markdown("### 1. 本日のお辛い箇所や気になるところ（複数選択可）")

c1 = st.checkbox("首・肩のガチガチなコリ・だるさ")
c2 = st.checkbox("頭痛・目の疲れ・睡眠の浅さ")
c3 = st.checkbox("背中の張り・腰の重み・深部の疲労")
c4 = st.checkbox("足のむくみ・冷え・立ち仕事による疲労")
c5 = st.checkbox("手・腕の疲れ・デスクワークによる負担")
c6 = st.checkbox("とにかく全身をじっくりほぐして贅沢に癒やされたい")

st.markdown("---")

if st.button("✨ おすすめコースを診断する", type="primary", use_container_width=True):
    selected_count = sum([c1, c2, c3, c4, c5, c6])

    if selected_count == 0:
        st.warning("お悩み項目を1つ以上選択してください。")
    else:
        st.success("🎉 あなたに最適なおすすめコースが決定しました！")

        # 判定ロジック
        if c6 or (c3 and c1 and (c2 or c4)):
            course_name = "【極上ご褒美】タイ古式 60分 ＋ アロマオイル全身 60分（計120分）"
            desc = "ストレッチで全身の筋膜と関節をゆるめた後、極上アロマオイルで流す完全オーダーメイドの贅沢コースです。日頃の溜まりきった疲労を根本からクリアにしたい方に最適です。"
        elif c2 and not c4 and not c5:
            course_name = "【頭スッキリセット】タイ古式マッサージ ＋ ヘッドマッサージ"
            desc = "全身をストレッチでしっかりほぐしながら、温かいヘッドケアで頭部〜目元をじっくり解放します。頭重感や目の疲れ、ストレスを感じている方におすすめです。"
        elif c3 and not c2 and not c4:
            course_name = "【背中集中ケア】タイ古式マッサージ ＋ 背中アロマオイル"
            desc = "タイ古式のストレッチで背骨まわりをゆるめ、オイルで背中全体の滞りを流します。慢性的な腰の重みや背中の張りが気になる方にピッタリです。"
        elif (c4 or c5) and not c2 and not c3:
            course_name = "【末端リフレッシュ】タイ古式マッサージ ＋ フットまたはハンドリフレ"
            desc = "全身のタイ古式に加え、足裏〜膝下、または手〜肘にかけて重点的にアプローチ。むくみや冷え、デスクワークでの手腕の疲労をスッキリ和らげます。"
        else:
            course_name = "【一番人気・当店イチオシ】タイ古式マッサージ 90分コース"
            desc = "うつ伏せ・仰向け・横向き・座り姿勢まで、全身の筋肉をくまなく伸ばし切る90分。70本以上のセン（エネルギーライン）に働きかけ、驚くほどの身体の軽さを実感いただけます。"

        # 診断結果カード
        st.markdown(
            f"""
            <div style="
                background-color: #f0f7f4;
                border: 2px solid #2e7d32;
                border-radius: 12px;
                padding: 20px;
                margin-top: 10px;
                margin-bottom: 20px;
            ">
                <h3 style="color: #2e7d32; margin-top:0;">💡 おすすめコース</h3>
                <h4 style="color: #1b5e20;">{course_name}</h4>
                <p style="color: #333; line-height: 1.6;">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # 予約・クーポン導線
        st.markdown("### 📅 ご予約・お得な特典")

        st.markdown(
            f"""
            <a href="{SQUARE_URL}" target="_blank" style="
                display: block;
                width: 100%;
                padding: 14px;
                background-color: #2e7d32;
                color: white;
                text-align: center;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
                text-decoration: none;
                margin-bottom: 12px;
            ">📅 このコースをSquareでネット予約する ➔</a>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <a href="{LINE_URL}" target="_blank" style="
                display: block;
                width: 100%;
                padding: 14px;
                background-color: #06C755;
                color: white;
                text-align: center;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
                text-decoration: none;
            ">💬 公式LINE登録でお得なクーポンを取得する ➔</a>
            """,
            unsafe_allow_html=True,
        )
