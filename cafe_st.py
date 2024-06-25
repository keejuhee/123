import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

# 데이터 불러오기
file_path = 'cafe.xlsx'
cafe_data = pd.read_excel(file_path)

# order_date를 datetime 형식으로 변환
cafe_data['order_date'] = pd.to_datetime(cafe_data['order_date'])

# 연도와 월 컬럼 추가
cafe_data['year'] = cafe_data['order_date'].dt.year
cafe_data['month'] = cafe_data['order_date'].dt.month

# Streamlit 대시보드 설정
st.title('카페 매출 대시보드')

# 사이드바에서 연도와 제품 선택
selected_year = st.sidebar.selectbox(
                  '연도 선택', sorted(cafe_data['year'].unique()))
selected_product = st.sidebar.selectbox(
                  '제품 선택', sorted(cafe_data['item'].unique()))

# 선택된 연도와 제품에 따라 데이터 필터링
filtered_data = cafe_data[(cafe_data['year'] == selected_year) & 
                          (cafe_data['item'] == selected_product)]

# 월별 매출 데이터 계산
monthly_sales = filtered_data.groupby('month')['price'].sum().reset_index()

# 매출 표 출력
st.write(f'{selected_year}년 {selected_product} 매출 데이터')
st.write(filtered_data)

# 막대 그래프 그리기
st.write(f'{selected_year}년 {selected_product} 월별 매출')
st.bar_chart(monthly_sales.set_index('month'))

# pip install matplotlib
# pip install openpyxl