from enum import auto
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit Traial') 
'''
## HP作成練習
### 表の表示
'''
left_column,center_column,right_column=st.columns(3)
df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
#動的
#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0),width=200,height=200)
# 静的
# st.table(df.style.highlight_max(axis=0)) 

left_column.write('left_chart')
left_column.write(df)
center_column.write('center_chart')
center_column.dataframe(df.style.highlight_max(axis=0),width=200,height=200)
right_column.write('right_chart')
right_column.table(df.style.highlight_max(axis=0)) 

st.write('code表示')
'''
```python
left_column.write('left_chart')
left_column.write(df)
center_column.write('center_chart')
center_column.dataframe(df.style.highlight_max(axis=0),width=200,height=200)
right_column.write('right_chart')
right_column.table(df.style.highlight_max(axis=0)) 
```
'''

'''
### グラフの表示

'''
df=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

st.write('code表示')
'''
```Python
df=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
```
'''

'''
### Mapチャートの表示
'''

df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

st.map(df)

st.write('code表示')
'''
```Python
df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

st.map(df)
```
'''

'''
### 画像の表示
'''

'''
#### 表示
'''
#Grid layout
#https://www.youtube.com/watch?v=clFrWjiwxL0
#https://pythonwife.com/layout-streamlit-application/
num=5
lcol=[]
col= st.columns(num)

for i in list(range(0,num,1)):
    with col[i]:
        #st.header("Chord_wheel_"+str(i+1))
        st.image("Chord_wheel_"+str(i+1)+".jpg",caption="Chord_wheel_"+str(i+1), use_column_width=True)

import streamlit as st
from itertools import cycle

filteredImages = [] # your images here
caption = [] # your caption here
cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(filteredImages):
    next(cols).image(filteredImage, width=150, caption=caption[idx])

# st.write('Displey Image')
# img1=Image.open('Chord_wheel.jpg')
# left_column.write('left_picture')
# left_column.image(img1,caption='Chord_wheel',use_column_width=auto)
# img2=Image.open('Chord_wheel_2.jpg')
# center_column.write('center_picture')
# center_column.image(img2,caption='Chord_whee2',use_column_width=auto)
# img3=Image.open('Chord_wheel_3.jpg')
# right_column.write('right_picture')
# right_column.image(img3,caption='Chord_whee2',use_column_width=auto)
# if st.checkbox('Show Image'):
#     img4=Image.open('Chord_wheel_4.jpg')
#     st.image(img4,caption='cloth',use_column_width=True)

# # 章
# ## 節
# ### 項

# ```python 
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# '''



# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df=pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )

# st.map(df)

# st.write('Displey Image')

# if st.checkbox('Show Image'):
#     img=Image.open('Chord_wheel.jpg')
#     st.image(img,caption='cloth',use_column_width=True)

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、',option,'です。'



# left_column.write('interactive Wedgets')

# text=st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は：',text,'です。'

# condition=st.slider('あなたの今の調子は？',0,100,75)
# 'コンディション:',right_column.condition

# left_column,right_column=st.columns(2)
# button=left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')
    



# st.write('プログレスバー')

# 'Start!'

# latest_iteratipn=st.empty()
# bar=st.progress(0)

# for i in range(100):
#     latest_iteratipn.text(f'Iterration{i+1}')
#     bar.progress(i+1)
#     time.sleep(0.05)

# 'Done!!!!'
    
# button=left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')
    
# expander = st.expander('問い合わせ1')
# expander.write('問い合わせ1の解答を書く')
# expander = st.expander('問い合わせ2')
# expander.write('問い合わせ2の解答を書く')
# expander = st.expander('問い合わせ3')
# expander.write('問い合わせ3の解答を書く')


import numpy as np
import requests
import streamlit as st

ENDPOINT = "H:\MyPythonProject\streamlit"

with st.sidebar:
    st.header("Configuration")
    with st.form(key="grid_reset"):
        n_photos = st.slider("Number of  photos:", 4, 128, 16)
        n_cols = st.number_input("Number of columns", 2, 8, 4)
        st.form_submit_button(label="Reset images and layout")
    with st.expander("About this app"):
        st.markdown("It's about cats :cat:!")
    st.caption("Source: https://cataas.com/#/")

st.title("Choose your favorite cat :cat:")
st.caption(
    "You can display the image in full size by hovering it and clicking the double arrow"
)

# cat_images = [
#     requests.get(f"{ENDPOINT}?width=1200&height=1200").content for i in range(n_photos)
# ]

images = ["Chord_wheel_1.jpg",
          "Chord_wheel_2.jpg",
          "Chord_wheel_3.jpg",
          "Chord_wheel_4.jpg",
          "Chord_wheel_5.jpg",
          "cloth.jpg"
]

captions = ["Chord_wheel_1.jpg",
          "Chord_wheel_2.jpg",
          "Chord_wheel_3.jpg",
          "Chord_wheel_4.jpg",
          "Chord_wheel_5.jpg",
          "cloth.jpg"
]
n_rows = 1 + len(images) // int(n_cols)
rows = [st.container() for _ in range(n_rows)]
cols_per_row = [r.columns(n_cols) for r in rows]
cols = [column for row in cols_per_row for column in row]

for image_index, image in enumerate(images):
    cols[image_index].image(image,caption=captions[image_index])