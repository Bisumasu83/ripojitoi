import streamlit as st

# 素数判定関数
def is_prime(n):
    # 1以下の数は素数ではない
    if n <= 1:
        return False
    # 2からnの平方根までの数で割り切れるかチェック
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# アプリケーションのタイトル
st.title("素数判定アプリケーション")

# ユーザー入力
number = st.number_input("判定したい数を入力してください", min_value=0, step=1)

# 素数判定
if number:
    if number == 57:
        st.write("57 はグロタンディーク素数です！")
    elif is_prime(number):
        st.write(f"{number} は素数です！")
    else:
        st.write(f"{number} は素数ではありません。")
