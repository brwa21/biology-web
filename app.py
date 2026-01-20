import streamlit as st
import google.generativeai as genai
from PIL import Image

# ١. لێرە کلیلە نوێیەکە دابنێ
genai.configure(api_key="AIzaSyAH_eJ4XHH9MsPI1YaJ9xOFMiKPaDvHZxw")

# ڕێنمایی بۆ ئەوەی وەک مامۆستای بایۆلۆجی قسە بکات
instruction = (
    "You are a professional Biology Teacher. Always answer in Sorani Kurdish. "
    "Be polite, scientific, and helpful. You can analyze images and explain biological terms."
)
# بەکارهێنانی مۆدێلی چاککراو
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash-latest' # وشەی latest دڵنیایی دەدات کە کۆن نییە
)


st.set_page_config(page_title="Bio Teacher Web", page_icon="🧬")
st.title("🧬 مامۆستای بایۆلۆجی (وەشانی وێب)")
st.write("بەخێربێیت! دەتوانیت لێرە پرسیار بکەیت یان وێنەیەک بۆ مامۆستا بنێریت.")

# بەشی بارکردنی وێنە
uploaded_file = st.file_uploader("وێنەیەکی بایۆلۆجی باربکە...", type=["jpg", "png", "jpeg"])

# بەشی نووسینی پرسیار
user_query = st.text_input("پرسیارەکەت بنووسە:")

if user_query:
    with st.spinner('خەریکە وەڵامت بۆ دەنووسم...'):
        if uploaded_file:
            # ئەگەر وێنە هەبوو، Gemini وێنەکە و دەقەکە پێکەوە دەخوێنێتەوە
            img = Image.open(uploaded_file)
            st.image(img, caption='وێنە بارکراوەکە', use_container_width=True)
            response = model.generate_content([user_query, img])
        else:
            # ئەگەر تەنها دەق بوو
            response = model.generate_content(user_query)
            
        st.write("---")
        st.markdown(response.text)