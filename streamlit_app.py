# encoding=utf-8
from kg_demo_movie.KB_query.query_main import QAInterface
import streamlit as st


@st.cache(allow_output_mutation=True)
def get_interface():
    interface = QAInterface()
    return interface


qa_interface = get_interface()

st.title("电影KBQA Demo")

st.text_area('Demo支持的问题类型', """1. 某演员演了什么电影
2. 某电影有哪些演员出演
3. 演员A和演员B合作出演了哪些电影
4. 某演员参演的评分大于X的电影有哪些
5. 某演员出演过哪些类型的电影
6. 某演员出演的XX类型电影有哪些。
7. 某演员出演了多少部电影。
8. 某演员是喜剧演员吗。
9. 某演员的生日/出生地/英文名/简介
10. 某电影的简介/上映日期/评分""", height=270)

question = st.text_input("请输入你的问题：")
if question != "":
    st.text(qa_interface.answer(question))
    # st.write(qa_interface.answer(question))
