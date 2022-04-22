import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Ali Mi'raaj S.E.
##### *Resume* 
''')

image = Image.open('ali.png')
st.image(image, width=250)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Seorang **Data Enthusiast** di bidang yang berkaitan dengan manajemen bisnis dan pemasaran. Memiliki semangat yang tinggi untuk belajar *data science* dan *data analytics*. 
- Memiliki pengetahun dalam **pengolahan data** `(Python, Pandas)` dan **Data Visualization** `(Matplotlib, Seaborn, dan Data Studio Google)` untuk menunjang pengambilan keputusan bisnis di tingkat manajemen.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://github.com/alimiraajal" target="_blank">Ali Mi'raaj</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#pendidikan">Pendidikan</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#pengalaman-kerja">Pengalaman Kerja</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#pengalaman-organisasi">Pengalaman Organisasi</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#prestasi-dan-penghargaan">Prestasi dan Penghargaan</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#pelatihan">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Pelatihan</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Sosial Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Pendidikan
''')

txt('**Sarjana Ekonomi** (Manajemen Pemasaran), Universitas Negeri Semarang, Indonesia',
'**2017-2022**')
st.markdown('''
- IPK: `3.77`
- Judul Skripsi `Pengaruh Word of Mouth dalam Memediasi Service Quality dan Customer Satisfaction Terhadap Switching Intention : Studi pada Taksi Bluebird di Kota Semarang`.
''')

#####################
st.markdown('''
## Pengalaman Kerja
''')

txt('**Customer Success Freelancer**, DQLab - Universitas Multimedia Nusantara',
'**2022-Sekarang**')
st.markdown('''
- `Menangani komplain` yang disampaikan oleh member DQLab dan menjawab pertanyaan terkait kursus DQLab. 
- Memandu `sesi konsultasi` member Prakerja yang mengambil kursus di DQLab.
- Melakukan `prospek` terhadap pelanggan yang potensial menjadi member premium DQLab.
- `Mencatat dan melaporkan` pertanyaan yang sering ditanyakan oleh member DQLab.
''')

txt('**Magang Seksi Komersial**, Perum BULOG Kantor Cabang Semarang',
'**2021-2021**')
st.markdown('''
- Input data penawaran dan penjualan ke dalam `laporan rincian transaksi harian` dalam bentuk excel.
- Membuat `dokumen penjualan` (*purchase order*, surat perintah setor, *delivery order*, dan berita acara).
- Rekapitulasi `data pelanggan` (RPK) dan *maintenance* data melalui sistem informasi manajemen.
''')

txt('**Pramuniaga**, PT Indomarco Prismatama',
'**2016-2017**')
st.markdown('''
- Melakukan *display* produk dan menjaga ketersediaan `produk` di rak.
- Melakukan *stock opname* per-kategori rak dan mencocokkan *data* dengan jumlah sebenarnya.
''')

#####################
st.markdown('''
## Pengalaman Organisasi
''')

txt('**Koordinator**, Student Staff Pusat Karir dan Bimbingan Konseling LP3 UNNES',
'**2019-2020**')
st.markdown('''
- `Mengoordinasi` program kerja yang telah disusun bersama staff akademik dan Kepala Pusat Karir dan BK LP3 UNNES.
- Menjadi `perantara komunikasi` antara HRD perusahaan dan staff akademik dalam penyelenggaraan campus hiring maupun magang.
- Menyususn laporan pelaksanaan program kerja dan `visualisasi data` untuk keperluan laporan tahunan.
''')

txt('**Staff Public Relation**, Student Staff Pusat Karir dan Bimbingan Konseling LP3 UNNES',
'**2018-2019**')
st.markdown('''
- Membuat *content plan* dalam bentuk Google sheet (isi konten, *copywriting, schedule post*, dan *hastag*).
- Melakukan `analisis` tipe konten populer untuk Instagram.
''')

txt('**Ketua**, Ikatan Mahasiswa Bidikmisi',
'**2018-2019**')
st.markdown('''
- Melakukan `koordiasi` dan pengawasan terhadap program kerja yang telah dirancang.
- Melakukan evalusi terhadap `capaian kinerja` selama pelaksanaan program kerja.
''')

txt('**Staff Education & Research**, Marketing Club on Teaching',
'**2017-2019**')
st.markdown('''
- Melakukan `riset` mengenai viral marketing dan update informasi perkembangan marketing terbaru.
- Mengadakan diskusi dan pembahasan mengenai topik dasar `marketing`.
''')

#####################
st.markdown('''
## Prestasi dan Penghargaan
''')
txt4('Juara 3', 'National Business Plan GITA Erasmusplus Project – Erasmus+ Programme of European Union', '**2021**')
txt4('Penerima Hibah', 'Pekan Kreativitas Mahasiswa – Kemendikbudristek', '**2021**')
txt4('Juara 3', 'Marketing festival – STIE Perbanas Surabaya','**2020**')
txt4('Finalis', 'Business Case Competition Pegadaian – Universitas Syiah Kuala Aceh', '**2020**')
txt4('FInalis', 'Marketing Fest – Universitas Diponegoro Semarang','**2020**')
txt4('Penerima Hibah', 'Kompetisi Bisnis Mahasiswa Indonesia – Kemendikbud', '**2020**')
txt4('Juara 1', 'Karya Tulis Ilmiah Kandungan AL Quran MTQ – Universitas Negeri Semarang', '**2019**')

#####################
st.markdown('''
## Pelatihan
''')
txt4('Udemy', 'Data Science Course 2022: Complete Data Science Bootcamp', '**2022**')
txt4('DQLab', 'Data Analyst Project: Business Decision Research', '**2022**')
txt4('DQLab', 'Data Analyst Python Track','**2022**')
txt4('Udemy', 'SQL - MySQL for Data Analytics and Business Intelligence', '**2022**')
txt4('SkillUp', 'Business Analytics with Excel','**2020**')
txt4('MarkPlus', 'Certificate in Sales Operation', '**2020**')
txt4('Certiport', 'Microsoft Office Specialist - Microsoft Power Point 2013', '**2018**')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`')
txt3('Data processing/wrangling', '`SQL`, `Pandas`')
txt3('Data visualization', '`Matplotlib`, `Seaborn`, `Google Data Studio`')
txt3('Machine Learning', '`scikit-learn`')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/alimiraaj')
txt2('Instagram', 'https://instagram.com/alimiraaj_')
txt2('GitHub', 'https://github.com/alimiraajal/')
