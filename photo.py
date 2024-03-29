import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
import pathlib
import glob
import os

#カレントの下のtempディレクトリを指定
image_dir = pathlib.Path(r'./台湾アクセサリ')

#st.title('つやこ') 
#st.write('<span style="color:purple"><big>つやこ</big></span>',
#              unsafe_allow_html=True)
original_title = '<p style="font-family:Courier; color:blue; font-size: 40px;">つやこ</p>'
st.markdown(original_title, unsafe_allow_html=True)
'''
### Taiwanese Accessory
'''
#Grid layout
#https://www.youtube.com/watch?v=clFrWjiwxL0
#https://github.com/andfanilo/s4a_cats_grid/blob/main/app.py
#https://pythonwife.com/layout-streamlit-application/

# import streamlit as st
# from itertools import cycle
# filteredImages = [] # your images here
# caption = [] # your caption here
# cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
# for idx, filteredImage in enumerate(filteredImages):
#     next(cols).image(filteredImage, width=150, caption=caption[idx])

# file upload 
#https://zenn.dev/ohtaman/articles/streamlit_tips

@st.cache
def get_images(image_dir):
    # # globでディレクトリ内のjpgファイルをリストで取得
    images = [str(p) for p in list(image_dir.glob(r'*.jpg'))]
    return images


with st.sidebar:
    st.header("Configuration")
    with st.form(key="grid_reset"):
        #n_photos = st.slider("Number of  photos:", 4, 128, 16)
        n_cols = st.number_input("Number of columns", 2, 8, 4)
        st.form_submit_button(label="Reset images and layout")
    
    st.markdown('#### 画像を保存する')
    file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])
    if file:
        st.markdown(f'{file.name} をアップロードしました.')
        img_dir = os.path.join(image_dir, file.name)
        # 画像を保存する
        with open(img_dir, 'wb') as f:
            f.write(file.read())
        images=get_images(image_dir)
        
    with st.expander("About this app"):
        st.markdown("It's about accessory :smile:!")
    #st.caption("Source: https://cataas.com/#/")
    
    

st.subheader("Choose your favorite accessory :smile:! ")
st.caption(
    "You can display the image in full size by hovering it and clicking the double arrow"
)


#https://qiita.com/Tak3315/items/c0dc8b4d81ed2a582f22
#カレントの下のtempディレクトリを指定
image_dir = pathlib.Path(r'./台湾アクセサリ')
# # globでディレクトリ内のHEICファイルをリストで取得
images=get_images(image_dir)
 
captions = [str(p.name) for p in list(image_dir.glob(r'*.jpg'))]

n_rows = 1 + len(images) // int(n_cols)
rows = [st.container() for _ in range(n_rows)]
cols_per_row = [r.columns(n_cols) for r in rows]
cols = [column for row in cols_per_row for column in row]

for image_index, image in enumerate(images):
    cols[image_index].image(image,caption=captions[image_index])
