import streamlit as st



# 在内存中初始化一个ind,当内存中没有'ind'的时候，才初始化
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 图片数组-装很多的图片

video_obj = [
    {
        'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title': '蝴蝶被砸'
    },
    {
        'url': 'https://www.w3schools.com/html/movie.mp4',
        'title': '黑熊捕食'
    },
    {
        'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title': '悲惨人生'
    }
    ]


current_video = video_obj[st.session_state['ind']]
st.write(current_video['title']) # 单独显示标题
st.video(current_video['url']) # 只传入URL参数



def adove():
    # 点击上一个按钮要做的事
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(video_obj)
def nextImg():
    # 点击下一张按钮要做的事
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(video_obj)
c1, c2 = st.columns(2)



with c1:
    st.button('上一个',on_click=adove, use_container_width=True)

with c2:
    st.button('下一个', on_click=nextImg, use_container_width=True)

