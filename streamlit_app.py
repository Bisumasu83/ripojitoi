import streamlit as st

# 歴史的出来事のデータ
history_events = [
    {"year": 1945, "location": "日本", "event": "第二次世界大戦の終結", "description": "日本は第二次世界大戦で敗戦し、ポツダム宣言を受け入れて降伏。"},
    {"year": 1868, "location": "日本", "event": "明治維新", "description": "日本が江戸時代から近代国家に転換するための政治改革が始まった。"},
    {"year": 1776, "location": "アメリカ", "event": "アメリカ独立宣言", "description": "アメリカがイギリスから独立を宣言し、アメリカ合衆国が誕生。"},
    {"year": 1914, "location": "ヨーロッパ", "event": "第一次世界大戦の勃発", "description": "ヨーロッパで起こった戦争で、列強が対立し、世界規模の戦争に発展した。"},
    {"year": 1861, "location": "アメリカ", "event": "アメリカ南北戦争の開始", "description": "アメリカ合衆国が南北の対立により内戦に突入。"},
    {"year": 1949, "location": "中国", "event": "中華人民共和国の成立", "description": "中国で共産党が勝利し、毛沢東が新しい政府を樹立。"},
    {"year": 1919, "location": "ヨーロッパ", "event": "ヴェルサイユ条約締結", "description": "第一次世界大戦後の講和条約として、ドイツに厳しい制裁を課した。"},
    {"year": 1603, "location": "日本", "event": "江戸時代の開始", "description": "徳川家康が江戸幕府を開き、約260年間の平和な時代が始まった。"},
]

# タイトル
st.title("歴史解説アプリケーション")

# ユーザー入力を取得
year = st.number_input("西暦を入力してください", min_value=1000, max_value=2024, step=1)
location = st.text_input("場所を入力してください（例: 日本, アメリカ, ヨーロッパ）")

# 出力ボタンを押したとき
if st.button("歴史的出来事を検索"):
    # 入力値に基づいて出来事をフィルタリング
    filtered_events = [
        event for event in history_events 
        if event["year"] == year and location in event["location"]
    ]
    
    # 出力
    if filtered_events:
        # 最大3つの出来事を表示
        st.write(f"西暦 {year}年、場所: {location} で起こった歴史的出来事:")
        for i, event in enumerate(filtered_events[:3]):
            st.write(f"{i+1}. {event['event']}: {event['description']}")
    else:
        st.write("該当する歴史的出来事は見つかりませんでした。")
