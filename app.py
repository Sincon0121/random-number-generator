import streamlit as st
import random

def generate_random_numbers(min_value: int, max_value: int, count: int):
    if count < 1 or count > 10:
        raise ValueError("난수 개수는 1개 이상, 10개 이하로 설정해야 합니다.")
    if min_value > max_value:
        raise ValueError("최소값은 최대값보다 작거나 같아야 합니다.")
    
    return [random.randint(min_value, max_value) for _ in range(count)]

st.set_page_config(page_title="난수 생성기", page_icon="🎲")

st.title("🎲 메르센 트위스터 기반 난수 생성기")
st.write("정수 범위를 설정하고, 최대 10개의 난수를 생성해보세요!")

# ✅ input() 대신 Streamlit UI 사용
min_val = st.number_input("난수 최소값", value=1, step=1)
max_val = st.number_input("난수 최대값", value=100, step=1)
count = st.slider("몇 개의 난수를 생성할까요?", 1, 10, 5)

if st.button("난수 생성"):
    try:
        result = generate_random_numbers(int(min_val), int(max_val), int(count))
        st.success(f"🎉 생성된 난수: {result}")
    except ValueError as e:
        st.error(f"오류: {e}")
