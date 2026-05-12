import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================
st.set_page_config(
    page_title="GiziKu Dashboard",
    page_icon="🥗",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3, h4 {
    color: white;
}

p, label, div {
    color: white;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #1e293b, #334155);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
    text-align: center;
}

[data-testid="stMetricValue"] {
    color: #38bdf8;
    font-size: 35px;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

.stDataFrame {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================
st.title("🥗 GiziKu Dashboard")
st.caption("Dashboard Pemantauan Gizi Real-time Berbasis Data")

st.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================
@st.cache_data
def load_data():

    # =========================
    # LOAD CSV
    # =========================
    df_gizi = pd.read_csv("data/dataset_gizi_final.csv")
    df_akg = pd.read_csv("data/dataset_akg_final.csv")
    df_rekom = pd.read_csv("data/dataset_rekomendasi_final.csv")

    # =========================
    # FIX TIPE DATA NUMERIK
    # =========================
    kolom_gizi = [
        'energy_kcal',
        'protein_g',
        'fat_g',
        'carbohydrate_g',
        'sugar_g'
    ]

    for col in kolom_gizi:
        if col in df_gizi.columns:
            df_gizi[col] = pd.to_numeric(df_gizi[col], errors='coerce')

    # Dataset AKG
    for col in df_akg.columns:
        try:
            df_akg[col] = pd.to_numeric(df_akg[col])
        except:
            pass

    # Dataset rekomendasi
    for col in df_rekom.columns:
        try:
            df_rekom[col] = pd.to_numeric(df_rekom[col])
        except:
            pass

    return df_gizi, df_akg, df_rekom


# =====================================================
# TRY LOAD DATA
# =====================================================
try:
    df_gizi, df_akg, df_rekom = load_data()
    st.sidebar.success("✅ Semua dataset berhasil dimuat")

except Exception as e:
    st.error(f"❌ ERROR LOAD DATA: {e}")
    st.stop()

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.title("📌 Menu Dashboard")

menu = st.sidebar.radio(
    "Pilih Halaman",
    [
        "🏠 Overview",
        "📊 Distribusi Kandungan Gizi Makanan",
        "🍽️ Pemenuhan Angka Kecukupan Gizi (AKG)",
        "👥 Perbandingan Kebutuhan Gizi",
        "⚖️ Kesenjangan Nutrisi",
        "🩺 Pola Hubungan Nutrisi & Kondisi Medis"
    ]
)

# =====================================================
# OVERVIEW
# =====================================================
if menu == "🏠 Overview":

    st.header("📌 Ringkasan Dataset")

    # =========================================
    # METRIC CARD
    # =========================================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Jumlah Data Gizi",
            f"{len(df_gizi):,}"
        )

    with col2:
        st.metric(
            "Jumlah Data AKG",
            f"{len(df_akg):,}"
        )

    with col3:
        st.metric(
            "Jumlah Data Rekomendasi",
            f"{len(df_rekom):,}"
        )

    st.markdown("---")

    # =========================================
    # INFORMASI SEMUA DATASET
    # =========================================
    st.subheader("📋 Informasi Semua Dataset")

    info_df = pd.DataFrame({
        "Dataset": [
            "Dataset Gizi",
            "Dataset AKG",
            "Dataset Rekomendasi"
        ],
        "Jumlah Baris": [
            len(df_gizi),
            len(df_akg),
            len(df_rekom)
        ],
        "Jumlah Kolom": [
            df_gizi.shape[1],
            df_akg.shape[1],
            df_rekom.shape[1]
        ]
    })

    st.dataframe(
        info_df,
        use_container_width=True
    )

    st.markdown("---")

    # =========================================
    # PREVIEW DATASET GIZI
    # =========================================
    st.subheader("🥗 Preview Dataset Gizi")

    st.dataframe(
        df_gizi.head(10),
        use_container_width=True
    )

    st.markdown("---")

    # =========================================
    # PREVIEW DATASET AKG
    # =========================================
    st.subheader("🍽️ Preview Dataset AKG")

    st.dataframe(
        df_akg.head(10),
        use_container_width=True
    )

    st.markdown("---")

    # =========================================
    # PREVIEW DATASET REKOMENDASI
    # =========================================
    st.subheader("🩺 Preview Dataset Rekomendasi")

    st.dataframe(
        df_rekom.head(10),
        use_container_width=True
    )


# =====================================================
# PERTANYAAN BISNIS 1
# =====================================================
elif menu == "📊 Distribusi Kandungan Gizi Makanan":

    st.header("📊 Distribusi Kandungan Gizi Makanan")

    st.write("""
    ###
    Bagaimana distribusi kandungan gizi 
    (energi, protein, lemak, karbohidrat) 
    pada makanan dalam database?
    """)

    nutrisi = st.selectbox(
        "Pilih Nutrisi",
        [
            "energy_kcal",
            "protein_g",
            "fat_g",
            "carbohydrate_g",
            "sugar_g"
        ]
    )

    # =========================================
    # HAPUS NULL
    # =========================================
    data_nutrisi = df_gizi[nutrisi].dropna()

    # =========================================
    # METRIK
    # =========================================
    mean_val = data_nutrisi.mean()
    median_val = data_nutrisi.median()
    std_val = data_nutrisi.std()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Mean", f"{mean_val:.4f}")

    with col2:
        st.metric("Median", f"{median_val:.4f}")

    with col3:
        st.metric("Std Dev", f"{std_val:.4f}")

    st.markdown("---")

    # =========================================
    # VISUALISASI
    # =========================================
    col1, col2 = st.columns(2)

    # HISTOGRAM
    with col1:

        fig, ax = plt.subplots(figsize=(8,5))

        sns.histplot(
            data_nutrisi,
            kde=True,
            ax=ax
        )

        ax.set_title(f"Distribusi {nutrisi}")
        ax.set_xlabel(nutrisi)
        ax.set_ylabel("Frekuensi")

        st.pyplot(fig)

    # BOXPLOT
    with col2:

        fig2, ax2 = plt.subplots(figsize=(8,5))

        sns.boxplot(
            x=data_nutrisi,
            ax=ax2
        )

        ax2.set_title(f"Boxplot {nutrisi}")

        st.pyplot(fig2)

    st.markdown("---")

    st.subheader("📋 Statistik Deskriptif")

    st.dataframe(
        data_nutrisi.describe(),
        use_container_width=True
    )

# =====================================================
# PERTANYAAN BISNIS 2
# =====================================================
elif menu == "🍽️ Pemenuhan Angka Kecukupan Gizi (AKG)":

    st.header("🍽️ Pemenuhan Angka Kecukupan Gizi (AKG)")

    st.write("""
    ###
    Apakah asupan kalori harian pengguna 
    sudah memenuhi AKG?
    """)

    col1, col2 = st.columns(2)

    with col1:
        target_akg = st.number_input(
            "Target AKG Harian",
            min_value=1000,
            max_value=5000,
            value=2150
        )

    with col2:
        asupan = st.number_input(
            "Asupan Kalori Harian",
            min_value=0,
            max_value=5000,
            value=1800
        )

    persen = (asupan / target_akg) * 100

    st.markdown("---")

    st.metric(
        "Persentase Pemenuhan AKG",
        f"{persen:.2f}%"
    )

    st.progress(min(int(persen), 100))

    fig, ax = plt.subplots(figsize=(7,5))

    kategori = ["Asupan", "AKG"]
    nilai = [asupan, target_akg]

    sns.barplot(
        x=kategori,
        y=nilai,
        ax=ax
    )

    ax.set_title("Perbandingan Asupan vs AKG")
    ax.set_ylabel("Kalori")

    st.pyplot(fig)

# =====================================================
# PERTANYAAN BISNIS 3
# =====================================================
elif menu == "👥 Perbandingan Kebutuhan Gizi":

    st.header("👥 Perbandingan Kebutuhan Gizi")

    st.write("""
    ###
    Kelompok mana yang memiliki kebutuhan 
    gizi paling tinggi dan paling rendah?
    """)

    numeric_df = df_akg.select_dtypes(include='number')

    if numeric_df.shape[1] > 0:

        fig, ax = plt.subplots(figsize=(12,6))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap="coolwarm",
            ax=ax
        )

        ax.set_title("Heatmap Korelasi AKG")

        st.pyplot(fig)

    else:
        st.warning("Tidak ada kolom numerik di dataset AKG")

    st.markdown("---")

    st.dataframe(
        df_akg.head(10),
        use_container_width=True
    )

# =====================================================
# PERTANYAAN BISNIS 4
# =====================================================
elif menu == "⚖️ Kesenjangan Nutrisi":

    st.header("⚖️ Kesenjangan Nutrisi")

    st.write("""
    ###
    Seberapa besar kesenjangan antara 
    kandungan gizi makanan dengan target AKG?
    """)

    col1, col2 = st.columns(2)

    with col1:
        target = st.number_input(
            "Target Kalori",
            min_value=1000,
            max_value=5000,
            value=2200
        )

    with col2:
        makanan = st.number_input(
            "Total Kalori Makanan",
            min_value=0,
            max_value=5000,
            value=1500
        )

    selisih = target - makanan
    persen = (makanan / target) * 100

    st.metric(
        "Selisih Kalori",
        f"{selisih:.0f} kcal"
    )

    st.progress(min(int(persen), 100))

    st.write(f"Pemenuhan kebutuhan harian: **{persen:.2f}%**")

# =====================================================
# PERTANYAAN BISNIS 5
# =====================================================
elif menu == "🩺 Pola Hubungan Nutrisi & Kondisi Medis":

    st.header("🩺 Pola Hubungan Nutrisi & Kondisi Medis")

    st.write("""
    ###
    Bagaimana hubungan kondisi medis, 
    aktivitas fisik, dan ketidakseimbangan nutrisi?
    """)

    numeric_df = df_rekom.select_dtypes(include='number')

    if numeric_df.shape[1] > 0:

        fig, ax = plt.subplots(figsize=(12,7))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap="viridis",
            ax=ax
        )

        ax.set_title("Heatmap Korelasi Nutrisi")

        st.pyplot(fig)

    else:
        st.warning("Tidak ada kolom numerik pada dataset rekomendasi")

    st.markdown("---")

    st.dataframe(
        df_rekom.head(10),
        use_container_width=True
    )

