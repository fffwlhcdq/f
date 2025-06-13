import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='南宁必吃榜')

df = pd.DataFrame({
    "latitude":[22.837742,22.849208,22.814160,22.813641,22.830622],
    "longitude":[108.269605,108.320469,108.321510,108.384087,108.371383]})
df.index.name='序号'

st.subheader('南宁地图')

st.map(df)

st.title('⭐餐厅评分')
data = {
    '门店':['尝不忘', '隆江猪脚饭', '海底捞火锅','肯德基','必胜客'],
    '评分':[4.8, 4.5, 4.7,4.3,4.4],
}
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3,4,5], name='序号')
df.index = index

df_indexed = df.set_index('门店')
st.bar_chart(df_indexed)

st.title('💰不同类型餐厅价格')
data = {
    '月份': ['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'],
    '尝不忘(动物园店)': [20, 15, 18, 46, 56, 43, 59, 55, 44, 77, 88, 95],
    '王记隆江猪脚饭(万秀村店)': [12, 16, 12, 46, 64, 42, 49, 95, 34, 67, 48, 15],
    '海底捞火锅(百盛步行街店)': [110, 100, 120, 46, 54, 43, 49, 55, 124, 77, 86, 75],
    '肯德基(航洋店)': [11, 16, 10, 69, 54, 62, 49, 95, 94, 67, 80, 45],
    '必胜客(WOW青秀万达店)': [10, 19, 60, 66, 54, 32, 49, 46, 64, 70, 81, 75]
}
df = pd.DataFrame(data)
st.line_chart(df, y=['尝不忘(动物园店)','王记隆江猪脚饭(万秀村店)','海底捞火锅(百盛步行街店)','肯德基(航洋店)','必胜客(WOW青秀万达店)'])

st.title('🍲用餐高峰时段')
data = {
    '时间':['9','10','11', '12', '13','14','15'],
    '尝不忘':[97,121,134, 189, 180,177,114],
    '隆江猪脚饭':[76,97,120, 174, 156,144,113],
    '海底捞火锅':[71,81,110, 211, 198,149,97],
    '肯德基':[104,95,140, 178, 190,113,94],
    '必胜客':[111,86,160, 170, 184,99,104],
}
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3,4,5,6,7], name='序号')
df.index = index

df_indexed = df.set_index('时间')
st.area_chart(df_indexed)

st.title('🍽餐厅详情')
with st.expander("海底捞火锅(百盛步行街店)"):
        c1, c2= st.columns(2)
        c1.markdown('## 海底捞火锅(百盛步行街店)')
        c1.markdown('##### 评分')
        c1.markdown('# 4.9/5.0')
        c1.markdown('#### 人均消费')
        c1.markdown('# 35000元')

        c2.markdown('**推荐菜品：**')
        c2.markdown(' • &#8194;蟹棒虾滑肥牛卷')
        c2.markdown(' • &#8194;芝麻白糖年糕')
        c2.markdown(' • &#8194;牛肉豆花')


st.subheader('当前拥挤程度')
st.progress(91,text="91%拥挤")


st.title('😍今日推荐')
st.markdown("<span style='color:red; border:2px solid red; border-radius:8px; padding:4px;'>干饭首选👍</span>", unsafe_allow_html=True)

if 'count' not in st.session_state:
    st.session_state.count = 0

count = 0;
if st.button(' :red[今天吃什么]'):
	st.session_state.count += 1
	if st.session_state.count % 6 == 1:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：尝不忘</span>", unsafe_allow_html=True)
		st.markdown("![尝不忘](https://pic1.zhimg.com/v2-773f82aeb8c3fe64d9b6a9a8aa1c24bc_r.jpg?source=172ae18b)")
	if st.session_state.count % 6 == 2:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：王记隆江猪脚饭</span>", unsafe_allow_html=True)
		st.markdown("![王记隆江猪脚饭](https://tse4-mm.cn.bing.net/th/id/OIP-C.-k_asvs8q7pV6L0SErCCDwHaE8?rs=1&pid=ImgDetMain)")
	if st.session_state.count % 6 == 3:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：海底捞火锅(百盛步行街店)</span>", unsafe_allow_html=True)
		st.markdown("![图片](https://zhongces3.sina.com.cn/product/20221028/0d0599ab2717311cb7d955ac428c42e1.jpeg)")
	if st.session_state.count % 6 == 4:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：肯德基(新阳店)</span>", unsafe_allow_html=True)
		st.markdown("![图片](https://ts1.tc.mm.bing.net/th/id/R-C.7f7abab1305b51bd7d4a4aed9929c27f?rik=QF7KU3Lt0HyAng&riu=http%3a%2f%2fsu.bcebos.com%2fb2b-jiameng%2fonline%2f8be0d455-22f2-4cfd-be79-065fb5ae462a&ehk=vavYn4edBcz1n6BoGMnr2GuqWgkTSpKLMBikBB5J8Fo%3d&risl=&pid=ImgRaw&r=0)")
	if st.session_state.count % 6 == 5:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：必胜客(WOW青秀万达店)</span>", unsafe_allow_html=True)
		st.markdown("![图片](https://tse4-mm.cn.bing.net/th/id/OIP-C.OvojXjmhI5Ll4vaFZaXsPgHaLG?rs=1&pid=ImgDetMain)")
import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它

data = {
    '招牌菜品':['桂林米粉','猪脚饭','火锅','蛋挞','披萨'],
    '用餐高峰':['11--14','12--13','12--14','9-14','12--14'],
    '人均价格':[20,15,75,30,25],
    '评分':[79,83,95,86,81],
    '客流量':[650,314,1130,1430,976],
    '地理x坐标':[22.8330423,22.849208, 22.814160, 22.818192, 22.830622],
    '地理y坐标':[108.403855, 108.320469,108.321510, 108.292848, 108.371383],

}

index = pd.Series(['桂林米粉', '隆江猪脚饭', '海底捞火锅', '肯德基', '必胜客'], name='  ')
df = pd.DataFrame(data, index=index)

st.subheader('热门门店')
st.dataframe(df)
