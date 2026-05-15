import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="GiziKu Dashboard",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# CUSTOM CSS
# =====================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');

* { font-family: 'Plus Jakarta Sans', sans-serif; }

[data-testid="stAppViewContainer"] {
    background-color: #F0FDFA;
    padding-top: 0 !important;
    margin-top: 0 !important;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D7C6E 0%, #0A5F57 100%);
    border-right: 1px solid #14B8A6;
}
[data-testid="stSidebar"] * { color: white !important; }

h1, h2, h3, h4, h5, h6 { color: #1E293B !important; }
p, label, div, span { color: #1E293B !important; }

.metric-card {
    background: linear-gradient(135deg, #C1EDE9 0%, #D1F2EB 100%); 
    border: 1px solid #8EDDD9;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    transition: transform 0.2s;
}
.metric-card:hover { transform: translateY(-3px); }
.metric-value {
    font-size: 2rem;
    font-weight: 800;
    color: #0D5C52 !important;
}
.metric-label {
    font-size: 0.85rem;
    color: #0D5C52 !important;
    margin-top: 4px; 
}

.section-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #1E293B !important;
    border-left: 4px solid #10B981;
    padding-left: 12px;
    margin: 24px 0 16px 0;
}

.insight-box {
    background: linear-gradient(135deg, #C1EDE9 0%, #D1F2EB 100%);
    border: 1px solid #8EDDD9;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 12px 0;
}
.insight-box p { color: #0D5C52 !important; margin: 0; }

.stButton > button {
    background: linear-gradient(135deg, #059669, #10B981) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: all 0.3s !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #10B981, #34D399) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 15px rgba(16,185,129,0.4) !important;
}
div[data-testid="stSelectbox"] label { color: #1E293B !important; }
div[data-testid="stSlider"] label { color: #1E293B !important; }
div[data-testid="stRadio"] label { color: #1E293B !important; }
div[data-testid="stTextInput"] label { color: #1E293B !important; }
            
.stSelectbox > div > div { color: #1E293B !important; }
.stSlider > div > div { color: #1E293B !important; }
            
.stTabs [data-baseweb="tab"] {
    color: #94A3B8 !important;
    font-weight: 600 !important;
}
.stTabs [aria-selected="true"] {
    color: #10B981 !important;
    border-bottom-color: #10B981 !important;
}

.stDataFrame { border-radius: 12px; overflow: hidden; }
            
input::placeholder { color: #64748B !important; }
textarea::placeholder { color: #64748B !important; }
            
header[data-testid="stHeader"] {
    background: transparent;
    height: 0px;
}
div[data-testid="stToolbar"] {
    visibility: visible !important;
    height: auto !important;
    position: static !important;
}
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 3rem !important;
    margin-top: 0rem !important;
}
[data-testid="stAppViewContainer"] {
    padding-top: 0rem !important;
    margin-top: 0rem !important;
}
section[data-testid="stSidebar"] > div {
    padding-top: 0rem !important;
}

/* Force semua input/select/dropdown jadi putih */
div[data-baseweb="select"] > div { background-color: #FFFFFF !important; color: #1E293B !important; }
div[data-baseweb="menu"] { background-color: #FFFFFF !important; }
div[data-baseweb="menu"] li { background-color: #FFFFFF !important; color: #1E293B !important; }
div[data-baseweb="tag"] { background-color: #0D9488 !important; }
div[data-baseweb="tag"] span { color: white !important; }
div[data-baseweb="input"] > div { background-color: #FFFFFF !important; }
div[data-baseweb="input"] input { background-color: #FFFFFF !important; color: #1E293B !important; }

/* ========================= */
/* STREAMLIT DATAFRAME WHITE */
/* ========================= */

/* background utama dataframe */
[data-testid="stDataFrame"] {
    background: white !important;
    border-radius: 12px !important;
    border: 1px solid #D1D5DB !important;
    overflow: hidden !important;
}

/* canvas/grid internal */
.glideDataEditor {
    background-color: white !important;
    color: #1E293B !important;
}

/* viewport tabel */
.glideDataEditor div {
    background-color: white !important;
    color: #1E293B !important;
}

/* header */
.glideDataEditor .gdg-header {
    background-color: #CCFBF1 !important;
    color: #065F46 !important;
    font-weight: 700 !important;
}

/* sel tabel */
.glideDataEditor .gdg-cell {
    background-color: white !important;
    color: #1E293B !important;
}

/* scrollbar */
.glideDataEditor::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

.glideDataEditor::-webkit-scrollbar-thumb {
    background: #CBD5E1;
    border-radius: 10px;
}
/* Dropdown popup/popover putih */
[data-baseweb="popover"] * { background-color: #FFFFFF !important; color: #1E293B !important; }
ul[role="listbox"] { background-color: #FFFFFF !important; }
ul[role="listbox"] li { background-color: #FFFFFF !important; color: #1E293B !important; }
li[role="option"] { background-color: #FFFFFF !important; color: #1E293B !important; }
li[role="option"]:hover { background-color: #CCFBF1 !important; }

</style>
""", unsafe_allow_html=True)




# =====================================
# LOAD DATA
# =====================================
@st.cache_data
def load_data():
    gizi = pd.read_csv("data/dataset_nilai_gizi_makanan_final.csv")
    akg = pd.read_csv("data/dataset_akg_final.csv")
    rek = pd.read_csv("data/dataset_rekomendasi_final.csv")

    kolom_gizi = ['Energi (kkal)', 'Protein (g)', 'Lemak (g)', 'Karbohidrat (g)', 'Gula (g)']
    for col in kolom_gizi:
        if col in gizi.columns:
            gizi[col] = pd.to_numeric(gizi[col], errors='coerce')

    return gizi, akg, rek

try:
    df_gizi, df_akg, df_rek = load_data()
    data_loaded = True
except Exception as e:
    data_loaded = False
    st.error(f"❌ Gagal memuat data: {e}")

# =====================================
# SIDEBAR
# =====================================
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 20px 0 10px 0;'>
        <div style='font-size:2.5rem;'>🥗</div>
        <div style='font-size:1.4rem; font-weight:800; color:white;'>GiziKu</div>
        <div style='font-size:0.75rem; color:#94A3B8; margin-top:4px;'>Platform Gizi Cerdas</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### 📌 Menu")

    menu_options = [
        "🏠 Beranda",
        "🍽️ Kandungan Gizi Makanan",
        "📊 Analisis Pengguna",
        "📋 Kebutuhan AKG",
        "🧮 Kalkulator Gizi",
        "💡 Rekomendasi Makanan"
    ]

    if "menu" not in st.session_state:
        st.session_state.menu = "🏠 Beranda"

    for opt in menu_options:
        if st.sidebar.button(opt, use_container_width=True):
            st.session_state.menu = opt

    st.divider()

menu = st.session_state.menu

# =====================================
# HELPER: PLOT LAYOUT
# =====================================
DARK_BG = '#0F172A'
CARD_BG = '#E8F7F5'
ACCENT = '#06B6D4'

def dark_layout(fig, title=""):
    fig.update_layout(
        title=title,
        plot_bgcolor=CARD_BG,
        paper_bgcolor=CARD_BG,

        font_color='#1E293B',
        title_font_color='#1E293B',
        legend_font_color='#1E293B',

        margin=dict(t=50, l=20, r=20, b=20)
    )

    fig.update_xaxes(
        tickfont=dict(color='#1E293B'),
        title_font=dict(color='#1E293B')
    )

    fig.update_yaxes(
        tickfont=dict(color='#1E293B'),
        title_font=dict(color='#1E293B')
    )

    return fig

# =====================================
# 🏠 BERANDA
# =====================================
if menu == "🏠 Beranda":
    st.markdown("# 🥗 GiziKu Dashboard")
    st.markdown("##### Platform interaktif pemantauan gizi dan kesehatan berbasis data")

    st.divider()

    if data_loaded:
        c1, c2, c3, c4 = st.columns(4)
        metrics = [
            (c1, "🍽️", len(df_gizi), "Total Data Makanan"),
            (c2, "👤", len(df_rek), "Total Pengguna"),
            (c3, "🔥", f"{round(df_gizi['Energi (kkal)'].mean(),1)} kkal", "Rata-rata Kalori"),
            (c4, "⚠️", f"{round((df_rek['Risiko_Kesehatan']=='tinggi').mean()*100,1)}%", "Pengguna Risiko Tinggi"),
        ]
        for col, icon, val, label in metrics:
            with col:
                st.markdown(f"""
                <div class='metric-card'>
                    <div style='font-size:1.8rem;'>{icon}</div>
                    <div class='metric-value'>{val}</div>
                    <div class='metric-label'>{label}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<div class='section-title'>📊 Ringkasan Distribusi Gizi</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            fig = px.histogram(df_gizi, x='Energi (kkal)', nbins=30,
                               title='Distribusi Kalori Makanan',
                               color_discrete_sequence=[ACCENT])
            st.plotly_chart(dark_layout(fig), use_container_width=True)

        with col2:
            st.markdown("**Program Diet yang Direkomendasikan**")
            diet_counts = df_rek['Rekomendasi_Diet'].value_counts().reset_index()
            diet_counts.columns = ['Diet', 'Jumlah']
            fig2 = px.pie(diet_counts, names='Diet', values='Jumlah',
                          color_discrete_sequence=['#38BDF8','#818CF8','#34D399'])
            st.plotly_chart(dark_layout(fig2), use_container_width=True)

        st.markdown("""
        <div class='insight-box'>
        <p>💡 <b>Insight Beranda:</b> Sebagian besar makanan memiliki kalori sedang (100–300 kkal/sajian).
        Program diet <b>Balanced</b> paling banyak direkomendasikan, diikuti Low-Carb dan Low-Sodium.</p>
        </div>
        """, unsafe_allow_html=True)

# =====================================
# 🍽️ KANDUNGAN GIZI MAKANAN
# =====================================
elif menu == "🍽️ Kandungan Gizi Makanan":
    st.markdown("# 🍽️ Kandungan Gizi Makanan")
    st.markdown("Eksplorasi distribusi dan perbandingan kandungan gizi makanan.")
    st.divider()

    if data_loaded:
        kolom_gizi = ['Energi (kkal)', 'Protein (g)', 'Lemak (g)', 'Karbohidrat (g)', 'Gula (g)']
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Distribusi", "🏆 Top Makanan", "🔗 Korelasi", "🔍 Cari Makanan"])

        with tab1:
            st.markdown("<div class='section-title'>Distribusi Kandungan Gizi</div>", unsafe_allow_html=True)
            nutrisi = st.selectbox("Pilih Nutrisi", kolom_gizi)
            col1, col2 = st.columns(2)
            with col1:
                fig = px.histogram(df_gizi, x=nutrisi, nbins=30,
                                   title=f'Distribusi {nutrisi}',
                                   color_discrete_sequence=[ACCENT])
                st.plotly_chart(dark_layout(fig), use_container_width=True)
            with col2:
                # Box plot TANPA outlier (points=False)
                fig2 = px.box(df_gizi, y=nutrisi, title=f'Sebaran {nutrisi}',
                              color_discrete_sequence=['#818CF8'])
                st.plotly_chart(dark_layout(fig2), use_container_width=True)

            st.markdown(f"""
            <div class='insight-box'>
            <p>📌 Rata-rata <b>{nutrisi}</b>: <b>{round(df_gizi[nutrisi].mean(),2)}</b> |
            Max: <b>{round(df_gizi[nutrisi].max(),2)}</b> |
            Min: <b>{round(df_gizi[nutrisi].min(),2)}</b></p>
            </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown("<div class='section-title'>Top 10 Makanan Tertinggi per Nutrisi</div>", unsafe_allow_html=True)
            nutrisi_top = st.selectbox("Pilih Nutrisi untuk Top 10", kolom_gizi, key="top")
            top10 = df_gizi[['Nama_Makanan', nutrisi_top]].dropna().sort_values(
                by=nutrisi_top, ascending=False).head(10)
            fig = px.bar(top10, x=nutrisi_top, y='Nama_Makanan', orientation='h',
                         title=f'Top 10 Makanan - {nutrisi_top}',
                         color=nutrisi_top, color_continuous_scale='Blues')
            fig.update_layout(yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(dark_layout(fig), use_container_width=True)

        with tab3:
            st.markdown("<div class='section-title'>Korelasi Antar Kandungan Gizi</div>", unsafe_allow_html=True)
            corr = df_gizi[kolom_gizi].corr()
            fig = px.imshow(corr, text_auto='.2f', color_continuous_scale='RdBu_r',
                            title='Heatmap Korelasi Nutrisi', zmin=-1, zmax=1)
            st.plotly_chart(dark_layout(fig), use_container_width=True)
            st.markdown("""
            <div class='insight-box'>
            <p>💡 Energi berkorelasi kuat dengan Lemak & Karbohidrat. Gula berkorelasi rendah dengan Protein —
            makanan manis tidak selalu tinggi protein.</p>
            </div>
            """, unsafe_allow_html=True)

        with tab4:
            st.markdown("<div class='section-title'>🔍 Cari & Filter Makanan</div>", unsafe_allow_html=True)
            st.markdown("<p style='color: #94A3B8;'>💡 Fitur pencarian makanan ada di sini saja untuk kemudahan akses</p>", unsafe_allow_html=True)
            search = st.text_input("Cari nama makanan", placeholder="contoh: ayam, nasi, tempe...")
            if search:
                hasil = df_gizi[df_gizi['Nama_Makanan'].str.contains(search, case=False, na=False)]
                st.dataframe(hasil[['Nama_Makanan'] + kolom_gizi].head(20), use_container_width=True)
            else:
                st.dataframe(df_gizi[['Nama_Makanan'] + kolom_gizi].head(20), use_container_width=True)

# =====================================
# 📊 ANALISIS PENGGUNA
# =====================================
elif menu == "📊 Analisis Pengguna":
    st.markdown("# 📊 Analisis Pengguna GiziKu")
    st.markdown("Pola, distribusi, dan risiko kesehatan pengguna platform.")
    st.divider()

    if data_loaded:
        tab1, tab2, tab3 = st.tabs(["🏥 Program Diet", "⚖️ BMI & Gender", "❤️ Risiko Kesehatan"])

        with tab1:
            st.markdown("<div class='section-title'>Program Diet yang Dibutuhkan Pengguna</div>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                diet = df_rek['Rekomendasi_Diet'].value_counts().reset_index()
                diet.columns = ['Diet', 'Jumlah']
                fig = px.bar(diet, x='Diet', y='Jumlah', color='Jumlah',
                             color_continuous_scale='Blues',
                             title='Distribusi Program Diet')
                st.plotly_chart(dark_layout(fig), use_container_width=True)
            with col2:
                gender_diet = df_rek.groupby(['Jenis_Kelamin','Rekomendasi_Diet']).size().reset_index(name='Jumlah')
                fig2 = px.bar(gender_diet, x='Rekomendasi_Diet', y='Jumlah',
                              color='Jenis_Kelamin', barmode='group',
                              title='Distribusi Diet per Gender',
                              color_discrete_sequence=['#38BDF8','#F472B6'])
                st.plotly_chart(dark_layout(fig2), use_container_width=True)

            st.markdown("""
            <div class='insight-box'>
            <p>💡 Program <b>Balanced</b> paling banyak dibutuhkan. Distribusi antar gender relatif seimbang —
            risiko bias gender dalam rekomendasi cukup rendah.</p>
            </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown("<div class='section-title'>Distribusi BMI Pengguna</div>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                bmi = df_rek['Kategori_BMI'].value_counts().reset_index()
                bmi.columns = ['BMI', 'Jumlah']
                fig = px.pie(bmi, names='BMI', values='Jumlah',
                             title='Komposisi Kategori BMI',
                             color_discrete_sequence=['#34D399','#FBBF24','#F87171','#818CF8'])
                st.plotly_chart(dark_layout(fig), use_container_width=True)
            with col2:
                fig2 = px.box(df_rek, x='Kategori_BMI', y='Indeks_Massa_Tubuh',
                              color='Jenis_Kelamin',
                              title='Sebaran BMI per Kategori & Gender',
                              color_discrete_sequence=['#38BDF8','#F472B6'])
                st.plotly_chart(dark_layout(fig2), use_container_width=True)

            st.markdown("""
            <div class='insight-box'>
            <p>💡 Pengguna dengan BMI <b>overweight</b> dan <b>obese</b> memerlukan program diet khusus.
            Rekomendasi sudah dipersonalisasi berdasarkan kondisi BMI masing-masing pengguna.</p>
            </div>
            """, unsafe_allow_html=True)

        with tab3:
            st.markdown("<div class='section-title'>Profil Risiko Kesehatan & Klinis</div>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                risiko = df_rek['Risiko_Kesehatan'].value_counts().reset_index()
                risiko.columns = ['Risiko', 'Jumlah']
                colors = {'rendah':'#34D399', 'sedang':'#FBBF24', 'tinggi':'#F87171'}
                fig = px.bar(risiko, x='Risiko', y='Jumlah',
                             color='Risiko', title='Distribusi Risiko Kesehatan',
                             color_discrete_map=colors)
                st.plotly_chart(dark_layout(fig), use_container_width=True)
            with col2:
                # Visualisasi bar chart yang lebih jelas
                diet_health = df_rek.groupby('Rekomendasi_Diet')[['Glukosa_mg/dL', 'Kolesterol_mg/dL']].mean().reset_index()
                fig2 = px.bar(diet_health, x='Rekomendasi_Diet', 
                             y=['Glukosa_mg/dL', 'Kolesterol_mg/dL'],
                             barmode='group',
                             title='Rata-rata Glukosa & Kolesterol per Program Diet',
                             color_discrete_sequence=['#38BDF8', '#818CF8'])
                fig2.update_xaxes(tickangle=0)
                st.plotly_chart(dark_layout(fig2), use_container_width=True)

            tinggi = df_rek[df_rek['Risiko_Kesehatan'] == 'tinggi']
            st.markdown(f"""
            <div class='insight-box'>
            <p>⚠️ Terdapat <b>{len(tinggi)} pengguna ({round(len(tinggi)/len(df_rek)*100,1)}%)</b> dengan risiko
            kesehatan tinggi yang memerlukan intervensi fitur premium seperti monitoring dokter.
            Mayoritas memiliki glukosa & kolesterol di atas rata-rata.</p>
            </div>
            """, unsafe_allow_html=True)

# =====================================
# 📋 KEBUTUHAN AKG
# =====================================
elif menu == "📋 Kebutuhan AKG":
    st.markdown("# 📋 Kebutuhan AKG")
    st.markdown("Angka Kecukupan Gizi (AKG) per kelompok usia dan kondisi.")
    st.divider()

    if data_loaded:
        tab1, tab2, tab3 = st.tabs(["📊 Perbandingan", "🌡️ Heatmap", "🔝 Tertinggi & Terendah"])

        # PERBAIKAN: Tambahkan Gula ke kolom_akg jika ada di data
        kolom_akg = ['Energi (kkal)', 'Protein (g)', 'Lemak (g)', 'Karbohidrat (g)']
        if 'Gula (g)' in df_akg.columns:
            kolom_akg.append('Gula (g)')

        with tab1:
            st.markdown("<div class='section-title'>Perbandingan Kebutuhan Gizi Antar Kategori</div>", unsafe_allow_html=True)
            nutrisi = st.selectbox("Pilih Nutrisi", kolom_akg)
            kategori_filter = st.multiselect("Filter Kategori",
                df_akg['Kategori'].unique().tolist(),
                default=df_akg['Kategori'].unique().tolist())
            filtered = df_akg[df_akg['Kategori'].isin(kategori_filter)]
            fig = px.bar(filtered, x='Label_Umur_Kondisi', y=nutrisi,
                         color='Kategori', barmode='group',
                         title=f'Kebutuhan {nutrisi} per Kelompok',
                         color_discrete_sequence=px.colors.qualitative.Set2)
            fig.update_xaxes(tickangle=45)
            st.plotly_chart(dark_layout(fig), use_container_width=True)

        with tab2:
            st.markdown("<div class='section-title'>Heatmap Kebutuhan Gizi</div>", unsafe_allow_html=True)
            heat_data = df_akg.set_index('Label_Umur_Kondisi')[kolom_akg]
            fig = px.imshow(heat_data, text_auto=True, color_continuous_scale='Blues',
                            title='Heatmap Kebutuhan Gizi per Kelompok Usia & Kondisi',
                            aspect='auto')
            st.plotly_chart(dark_layout(fig), use_container_width=True)
            st.markdown("""
            <div class='insight-box'>
            <p>💡 Kelompok <b>Menyusui</b> dan <b>Hamil</b> memiliki kebutuhan energi tertinggi.
            Kebutuhan gizi meningkat pada masa remaja dan menurun setelah usia 50 tahun.</p>
            </div>
            """, unsafe_allow_html=True)

        with tab3:
            st.markdown("<div class='section-title'>Kelompok Kebutuhan Tertinggi & Terendah</div>", unsafe_allow_html=True)
            nutrisi3 = st.selectbox("Pilih Nutrisi", kolom_akg, key="akgtop")
            col1, col2 = st.columns(2)
            with col1:
                top3 = df_akg.nlargest(5, nutrisi3)[['Label_Umur_Kondisi', 'Kategori', nutrisi3]]
                st.markdown("**🔝 Kebutuhan Tertinggi**")
                st.dataframe(top3, use_container_width=True, hide_index=True)
            with col2:
                bot3 = df_akg.nsmallest(5, nutrisi3)[['Label_Umur_Kondisi', 'Kategori', nutrisi3]]
                st.markdown("**🔻 Kebutuhan Terendah**")
                st.dataframe(bot3, use_container_width=True, hide_index=True)

# =====================================
# 🧮 KALKULATOR GIZI
# =====================================
elif menu == "🧮 Kalkulator Gizi":
    st.markdown("# 🧮 Kalkulator Kebutuhan Gizi")
    st.markdown("Hitung estimasi kebutuhan kalori harian dan bandingkan dengan AKG.")
    st.divider()

    col1, col2 = st.columns([0.95, 1.05])
    with col1:
        st.markdown("<div class='section-title'>Data Diri</div>", unsafe_allow_html=True)
        gender = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"], horizontal=True)
        usia = st.slider("Usia (tahun)", 10, 80, 25)
        berat = st.slider("Berat Badan (kg)", 30, 120, 60)
        tinggi = st.slider("Tinggi Badan (cm)", 120, 210, 165)
        aktivitas = st.selectbox("Tingkat Aktivitas", [
            "Sedentary (jarang olahraga)",
            "Ringan (1-3x/minggu)",
            "Sedang (3-5x/minggu)",
            "Aktif (6-7x/minggu)"
        ])

        aktivitas_factor = {
            "Sedentary (jarang olahraga)": 1.2,
            "Ringan (1-3x/minggu)": 1.375,
            "Sedang (3-5x/minggu)": 1.55,
            "Aktif (6-7x/minggu)": 1.725
        }

        # Rumus Mifflin-St Jeor
        if gender == "Laki-laki":
            bmr = 10 * berat + 6.25 * tinggi - 5 * usia + 5
        else:
            bmr = 10 * berat + 6.25 * tinggi - 5 * usia - 161

        tdee = bmr * aktivitas_factor[aktivitas]
        bmi = berat / ((tinggi/100) ** 2)

        if bmi < 18.5:
            bmi_kat = "⚠️ Underweight"
            bmi_color = "#FBBF24"
        elif bmi < 25:
            bmi_kat = "✅ Normal"
            bmi_color = "#34D399"
        elif bmi < 30:
            bmi_kat = "⚠️ Overweight"
            bmi_color = "#FBBF24"
        else:
            bmi_kat = "🚨 Obesitas"
            bmi_color = "#F87171"

    with col2:
        st.markdown("<div class='section-title'>Hasil Perhitungan</div>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class='metric-card' style='margin-bottom:12px;'>
            <div style='font-size:1rem; color:#94A3B8;'>🔥 Kebutuhan Kalori Harian</div>
            <div class='metric-value'>{round(tdee)} kkal</div>
        </div>
        <div class='metric-card' style='margin-bottom:12px;'>
            <div style='font-size:1rem; color:#94A3B8;'>📏 Body Mass Index (BMI)</div>
            <div class='metric-value' style='color:{bmi_color} !important;'>{round(bmi,1)}</div>
            <div class='metric-label'>{bmi_kat}</div>
        </div>
        """, unsafe_allow_html=True)

        # Gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=tdee,
            gauge={
                'axis': {'range': [1000, 4000], 'tickcolor': 'white'},
                'bar': {'color': ACCENT},
                'steps': [
                    {'range': [1000, 1800], 'color': '#1E293B'},
                    {'range': [1800, 2500], 'color': '#1E3A5F'},
                    {'range': [2500, 4000], 'color': '#162B45'},
                ]
            },
            number={'font': {'color': '#1E293B'}}
        ))
        fig.update_layout(paper_bgcolor=CARD_BG, font_color='#1E293B', height=300,
                          margin=dict(t=80, b=20, l=20, r=20))
        st.markdown("**🔥 Kebutuhan Kalori Harian (kkal)**", unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)

    # Breakdown makronutrien
    st.markdown("<div class='section-title'>Estimasi Kebutuhan Makronutrien</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    protein_g = round((tdee * 0.20) / 4, 1)
    lemak_g = round((tdee * 0.25) / 9, 1)
    karbo_g = round((tdee * 0.55) / 4, 1)

    for col, label, val, unit, icon in [
        (c1, "Protein", protein_g, "g/hari", "💪"),
        (c2, "Lemak", lemak_g, "g/hari", "🥑"),
        (c3, "Karbohidrat", karbo_g, "g/hari", "🍚")
    ]:
        with col:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size:1.5rem;'>{icon}</div>
                <div class='metric-value'>{val}g</div>
                <div class='metric-label'>{label} ({unit})</div>
            </div>
            """, unsafe_allow_html=True)

# =====================================
# 💡 REKOMENDASI MAKANAN
# =====================================
elif menu == "💡 Rekomendasi Makanan":
    st.markdown("# 💡 Rekomendasi Makanan")
    st.markdown("Temukan makanan yang sesuai dengan kebutuhan gizimu.")
    st.divider()

    if data_loaded:
        st.markdown("<div class='section-title'>Filter Preferensi</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            max_kalori = st.slider("Maks. Kalori (kkal)", 50, 600, 300)
        with col2:
            min_protein = st.slider("Min. Protein (g)", 0, 50, 5)
        with col3:
            max_lemak = st.slider("Maks. Lemak (g)", 0, 50, 20)

        hasil = df_gizi[
            (df_gizi['Energi (kkal)'] <= max_kalori) &
            (df_gizi['Protein (g)'] >= min_protein) &
            (df_gizi['Lemak (g)'] <= max_lemak)
        ].dropna(subset=['Energi (kkal)', 'Protein (g)', 'Lemak (g)'])

        st.markdown(f"""
        <div class='insight-box'>
        <p>✅ Ditemukan <b>{len(hasil)} makanan</b> yang sesuai dengan preferensimu!</p>
        </div>
        """, unsafe_allow_html=True)

        if len(hasil) > 0:
            kolom_tampil = ['Nama_Makanan', 'Energi (kkal)', 'Protein (g)', 'Lemak (g)', 'Karbohidrat (g)', 'Gula (g)']
            st.dataframe(
                hasil[kolom_tampil].sort_values('Protein (g)', ascending=False).head(20),
                use_container_width=True,
                hide_index=True
            )

            st.markdown("<div class='section-title'>📈 Visualisasi Makanan Rekomendasi</div>", unsafe_allow_html=True)
            
            # Bar chart: Perbandingan makro nutrisi top makanan
            top_makanan = hasil.nlargest(10, 'Protein (g)')[['Nama_Makanan','Protein (g)', 'Lemak (g)', 'Karbohidrat (g)']].head(10)
            fig2 = px.bar(top_makanan, x='Nama_Makanan', 
                         y=['Protein (g)', 'Lemak (g)', 'Karbohidrat (g)'],
                         barmode='group',
                         color_discrete_sequence=['#38BDF8', '#818CF8', '#34D399'])
            fig2.update_xaxes(tickangle=45)
            st.plotly_chart(dark_layout(fig2), use_container_width=True)
        else:
            st.warning("😕 Tidak ada makanan yang sesuai filter. Coba longgarkan filternya!")