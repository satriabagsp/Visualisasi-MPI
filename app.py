import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

# Fullscreen
st.set_page_config(
        page_title="PERENCANAAN X MODEL",
        layout="wide",
    )

# Remove Whitespace
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 2rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)



## Main Page

# Read Data
df = pd.read_csv('Data/Data Awal.csv', sep=';')
df = df[df['provinsi'] != 'Indonesia']

# Cleaning
df['mpi'] = df['mpi'].str.replace(',','.')
df['kemiskinan_moneter'] = df['kemiskinan_moneter'].str.replace(',','.').replace(' ','')
df['ipm'] = df['ipm'].str.replace(',','.').replace(' ','')
df['jumlah_penduduk'] = df['jumlah_penduduk'].str.replace(' ','')
df['jumlah_penduduk'] = df['jumlah_penduduk'].str.replace(',','.').replace(' ','')
df[['mpi', 'kemiskinan_moneter', 'ipm', 'jumlah_penduduk']] = df[['mpi', 'kemiskinan_moneter', 'ipm', 'jumlah_penduduk']].astype(float)

st.title('MPI x PMI (2019-2021)')

pil_c1, pil_c2, pil_c3 = st.columns(3)

with pil_c1:
    pilihan_x = st.selectbox(
        'Pilih Variabel X:',
        ['Multidimensional Poverty Index', 'Indeks Pembangunan Manusia','Jumlah Penduduk'],
        index=0)

    if pilihan_x == 'Multidimensional Poverty Index':
        pilihan_x = 'mpi'
    elif pilihan_x == 'Indeks Pembangunan Manusia':
        pilihan_x = 'ipm'
    elif pilihan_x == 'Jumlah Penduduk':
        pilihan_x = 'jumlah_penduduk'
    
with pil_c2:
    pilihan_y = st.selectbox(
        'Pilih Variabel Y:',
        ['Multidimensional Poverty Index', 'Indeks Pembangunan Manusia', 'Jumlah Penduduk'],
        index=1)

    if pilihan_y == 'Multidimensional Poverty Index':
        pilihan_y = 'mpi'
    elif pilihan_y == 'Indeks Pembangunan Manusia':
        pilihan_y = 'ipm'
    elif pilihan_y == 'Jumlah Penduduk':
        pilihan_y = 'jumlah_penduduk'

with pil_c3:
    pilihan_size = st.selectbox(
        'Pilih Variabel Size:',
        ['Multidimensional Poverty Index', 'Indeks Pembangunan Manusia', 'Jumlah Penduduk'],
        index=2)

    if pilihan_size == 'Multidimensional Poverty Index':
        pilihan_size = 'mpi'
    elif pilihan_size == 'Indeks Pembangunan Manusia':
        pilihan_size = 'ipm'
    elif pilihan_size == 'Jumlah Penduduk':
        pilihan_size = 'jumlah_penduduk'

st.write('---')

# Show Fig
fig = px.scatter(df, x=pilihan_x, y=pilihan_y, color="provinsi", size=pilihan_size, animation_frame="tahun", hover_data=['mpi'], width=750, height=800,
        labels=dict(mpi="MPI", ipm="IPM", provinsi="Provinsi", tahun="Tahun", jumlah_penduduk="Jumlah Penduduk"))

fig.add_annotation(text='Luas Lingkaran = Jumlah Penduduk', 
                    align='left',
                    showarrow=False,
                    xref='paper',
                    yref='paper',
                    x=0.02,
                    y=0.02,
                    bordercolor='black',
                    borderwidth=1)

st.plotly_chart(fig, use_container_width=True)