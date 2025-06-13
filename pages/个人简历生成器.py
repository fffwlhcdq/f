import streamlit as st
st.set_page_config(page_title='📧个人简历生成器',layout='wide')
st.title('📦个人简历生成器',)
st.text('使用streamlit创建您的个性化简历')

#把页面分成1:2的两份
c1,c2=st.columns([1,2])

with c1:
    #设置文本输入框
    st.text('个人信息表单')
    st.text_input('姓名',)
    st.text_input('职位')
    st.text_input('电话')
    st.text_input('邮箱')
    st.text_input('出生日期')
    xb=st.radio('性别',['男','女','其他'],horizontal=True)#设置单选按钮
    
    jn=st.selectbox('学历',['文盲','小学','初中','高中','本科','硕士','博士'])
    yy=st.selectbox('语言',['中文','语言','其他语种'])
    jn=st.multiselect('技能（可多选）',['c','c++','python','java','本科',])#设置多选框
    gzjy = st.slider('工作经验', 0, 60)#设置滑块
    values = st.slider('期望薪资范围（元）',0.0,100000.0,(50000.0,70000.0))
    st.text_area(label='个人简介', height=150, max_chars=200)
    st.time_input('每日最佳联系时段')
    #文件上传组件
    uploaded_file = st.file_uploader(
    "Drag and drop file here",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False,
    help="Limit 200MB per file · JPG, JPEG, PNG")


with c2:
    st.text('简历实时预览')
    b1,b2=st.columns(2)#把页面分成两份
    #左半部分预览
    with b1:
        st.text('姓名:梁伍菲')
        st.text('电话:195000000')
        st.text('邮箱:000@qq.com')
        st.text('出生日期:2004.9.01')
        #右半部分预览
    with b2:
        st.text('性别:男')
        st.text('学历:本科')
        st.text('工作经验:0年')
        st.text('期望薪资:50000-70000')
        st.text('最佳联系时间:20:00')
        st.text('语言能力:中文')
    st.text('个人简介:\n这个人很神秘，没有简介')
