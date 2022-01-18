import streamlit as st
import pandas as pd

YM_CHOICES = {0: "2021年12月", 1: "2021年11月", 2: "2021年10月", 3: "2021年09月", 4: "2021年08月"}
SALES_LIST = [[1200000,500000,700000], [1150000,550000,600000], [900000,360000,540000], [800000,300000,500000], [1100000,500000,600000]]

# sidebar
st.sidebar.write("検証ストアレポート")

with open("blankpage.pdf", "rb") as file:
    btn = st.sidebar.download_button(
        label="PDFをダウンロード",
        data=file,
        file_name="report.pdf",
        mime="application/pdf"
    )

def format_func(option):
    return YM_CHOICES[option]

st.sidebar.write("#")
option = st.sidebar.selectbox("年月を選択", options=list(YM_CHOICES.keys()), format_func=format_func)
st.sidebar.write("#")

st.sidebar.write("よくある質問")
expander1 = st.sidebar.expander('質問1')
expander1.write('質問1の回答')
expander2 = st.sidebar.expander('質問2')
expander2.write('質問2の回答')
expander3 = st.sidebar.expander('質問3')
expander3.write('質問3の回答')

# main
st.title('検証ストア レポート')
st.caption(f"{format_func(option)}分")
col1, col2, col3 = st.columns(3)
sales_values = SALES_LIST[option]
total_sales = "¥{:,}".format(sales_values[0])
domestic_sales = "¥{:,}".format(sales_values[1])
overseas_sales = "¥{:,}".format(sales_values[2])
col1.metric("総額", total_sales, "1.2%")
col2.metric("国内", domestic_sales, "-8%")
col3.metric("海外", overseas_sales, "4%")
st.write("#")

"""
### ● 売上データ
"""
df = pd.DataFrame(
    data = SALES_LIST,
    index = list(YM_CHOICES.values()),
    columns = ["総額", "国内", "海外"]
)
st.line_chart(df)
st.write("#")

"""
### ● 個別販売データ
"""
item_list = [[1,2,3,6000], [2,2,4,7000], [3,3,6,9000], [3,3,6,9000], [3,3,6,9000]]
item_index = ['商品A','商品B','商品C', '商品D', '商品E']
item_columns = ["国内", "海外", "販売数", "販売代金"]
df = pd.DataFrame(
    data = item_list,
    index = item_index,
    columns = item_columns
)
st.table(df)
