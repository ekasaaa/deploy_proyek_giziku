import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="GiziKu Dashboard",
    page_icon="🥗",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-color: #111827;
}

[data-testid="stSidebar"] {
    background-color: #6487A3;
}

h1, h2, h3, h4, h5, h6, p, label, div {
    color: white;
}

.stMetric {
    background-color: #1F2937;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #374151;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD DATA
# =====================================

@st.cache_data
def load_data():
    df = pd.read_csv("data/dataset_gizi_final.csv")

    # UBAH KOLOM MENJADI NUMERIK
    df['energy_kcal'] = pd.to_numeric(df['energy_kcal'], errors='coerce')
    df['protein_g'] = pd.to_numeric(df['protein_g'], errors='coerce')
    df['fat_g'] = pd.to_numeric(df['fat_g'], errors='coerce')
    df['carbohydrate_g'] = pd.to_numeric(df['carbohydrate_g'], errors='coerce')

    return df

try:
    df = load_data()
    st.sidebar.success("✅ Dataset berhasil dimuat")

except:
    st.error("❌ Dataset gagal dimuat")

# =====================================
# SIDEBAR MENU
# =====================================

st.sidebar.markdown("""
<h1 style='text-align: center; color: white;'>
🥗 GiziKu
</h1>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 📌 Navigasi")

if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Dashboard Utama"

# BUTTON MENU
if st.sidebar.button("🏠 Dashboard Utama", use_container_width=True):
    st.session_state.menu = "🏠 Dashboard Utama"

if st.sidebar.button("🥗 Kandungan Gizi", use_container_width=True):
    st.session_state.menu = "🥗 Kandungan Gizi Makanan"

if st.sidebar.button("📈 Analisis Gizi", use_container_width=True):
    st.session_state.menu = "📈 Analisis Kebutuhan Gizi"

if st.sidebar.button("💡 Insight & Rekomendasi", use_container_width=True):
    st.session_state.menu = "💡 Insight & Rekomendasi"

menu = st.session_state.menu

st.sidebar.divider()

st.sidebar.info("""
✨ Dashboard interaktif untuk membantu memahami
kandungan gizi dan pola makan sehat.
""")

# =====================================
# CUSTOM CSS
# =====================================
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-color: #111827;
}

[data-testid="stSidebar"] {
    background-color: #6487A3;
}

h1, h2, h3, h4, h5, h6, p, label, div {
    color: white;
}

.stMetric {
    background-color: #1F2937;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #374151;
}

/* BUTTON SIDEBAR */
.stButton > button {
    background-color: #4B6B88;
    color: white;
    border-radius: 12px;
    height: 50px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #7DA2C3;
    transform: scale(1.03);
    box-shadow: 0px 0px 10px rgba(255,255,255,0.3);
}

</style>
""", unsafe_allow_html=True)

# =====================================
# DASHBOARD UTAMA
# =====================================
if menu == "🏠 Dashboard Utama":

    st.title("🥗 GiziKu Dashboard")
    st.write("Dashboard pemantauan gizi makanan berbasis data interaktif")

    st.info("""
    Dashboard ini membantu pengguna memahami kandungan nutrisi makanan,
    kebutuhan gizi harian, dan rekomendasi pola makan sehat.
    """)

    # METRICS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🍽 Total Data Makanan",
            len(df)
        )

    with col2:
        st.metric(
            "🔥 Rata-rata Kalori",
            round(df['energy_kcal'].mean(), 2)
        )

    with col3:
        st.metric(
            "💪 Rata-rata Protein",
            round(df['protein_g'].mean(), 2)
        )

    st.divider()

    # CHART INTERAKTIF
    st.subheader("📊 Distribusi Kalori Makanan")

    fig = px.histogram(
        df,
        x='energy_kcal',
        nbins=30,
        title='Distribusi Kandungan Kalori',
        color_discrete_sequence=['#60A5FA']
    )

    fig.update_layout(
        plot_bgcolor='#111827',
        paper_bgcolor='#111827',
        font_color='white'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("Sebagian besar makanan memiliki kandungan kalori sedang hingga tinggi.")

# =====================================
# KANDUNGAN GIZI
# =====================================
elif menu == "🥗 Kandungan Gizi Makanan":

    st.title("🥗 Kandungan Gizi Makanan")

    st.write("Analisis kandungan nutrisi pada makanan dalam dataset")

    nutrisi = st.selectbox(
        "Pilih Nutrisi",
        ['energy_kcal', 'protein_g', 'fat_g', 'carbohydrate_g']
    )

    col1, col2 = st.columns(2)

    with col1:
        fig_bar = px.bar(
            df.head(15),
            x=df.head(15).index,
            y=nutrisi,
            color=nutrisi,
            title=f'Top Kandungan {nutrisi}'
        )

        fig_bar.update_layout(
            plot_bgcolor='#111827',
            paper_bgcolor='#111827',
            font_color='white'
        )

        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        fig_box = px.box(
            df,
            y=nutrisi,
            title=f'Sebaran {nutrisi}'
        )

        fig_box.update_layout(
            plot_bgcolor='#111827',
            paper_bgcolor='#111827',
            font_color='white'
        )

        st.plotly_chart(fig_box, use_container_width=True)

    st.success(f"Analisis menunjukkan distribusi {nutrisi} cukup bervariasi antar makanan.")

# =====================================
# ANALISIS KEBUTUHAN GIZI
# =====================================
elif menu == "📈 Analisis Kebutuhan Gizi":

    st.title("📈 Analisis Kebutuhan Gizi")

    st.write("Hitung estimasi kebutuhan kalori harian pengguna")

    usia = st.slider("Usia", 10, 70, 20)
    berat = st.slider("Berat Badan (kg)", 30, 120, 55)
    tinggi = st.slider("Tinggi Badan (cm)", 120, 210, 165)

    aktivitas = st.selectbox(
        "Tingkat Aktivitas",
        [
            "Rendah",
            "Sedang",
            "Tinggi"
        ]
    )

    # SIMULASI PERHITUNGAN
    bmr = 10 * berat + 6.25 * tinggi - 5 * usia

    if aktivitas == "Rendah":
        kebutuhan = bmr * 1.2
    elif aktivitas == "Sedang":
        kebutuhan = bmr * 1.5
    else:
        kebutuhan = bmr * 1.8

    st.metric(
        "🔥 Estimasi Kebutuhan Kalori Harian",
        f"{round(kebutuhan)} kkal"
    )

    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = kebutuhan,
        title = {'text': "Kebutuhan Kalori"},
        gauge = {
            'axis': {'range': [0, 4000]},
            'bar': {'color': '#60A5FA'}
        }
    ))

    fig_gauge.update_layout(
        paper_bgcolor='#111827',
        font_color='white'
    )

    st.plotly_chart(fig_gauge, use_container_width=True)

    st.info("Kebutuhan kalori dipengaruhi oleh usia, berat badan, tinggi badan, dan aktivitas.")

# =====================================
# INSIGHT & REKOMENDASI
# =====================================
elif menu == "💡 Insight & Rekomendasi":

    st.title("💡 Insight & Rekomendasi")

    st.write("Rekomendasi sederhana berdasarkan data nutrisi")

    protein_tinggi = df[df['protein_g'] > df['protein_g'].mean()]

    kalori_rendah = df[df['energy_kcal'] < df['energy_kcal'].mean()]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💪 Makanan Protein Tinggi")
        st.dataframe(protein_tinggi.head(10))

    with col2:
        st.subheader("🥗 Makanan Kalori Rendah")
        st.dataframe(kalori_rendah.head(10))

    st.success("""
    Rekomendasi:

    ✅ Perbanyak makanan tinggi protein
    ✅ Kurangi makanan tinggi kalori berlebih
    ✅ Konsumsi nutrisi seimbang setiap hari
    """)
