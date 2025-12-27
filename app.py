# -*- coding: utf-8 -*-


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



st.set_page_config(
    page_title="Nesli Tükenen Hayvanlar Analizi",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🐾"
)


st.markdown("""
    <style>
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
   
    .stApp {
        background: linear-gradient(to bottom right, #f8f9fa, #e9ecef);
    }
    
    
    [data-testid="stMetricValue"] {
        font-size: 28px;
        color: #1f77b4;
        font-weight: 600;
    }
    
    
    h1 {
        color: #2c3e50;
        font-weight: 700;
        padding: 20px 0;
        text-align: center;
        background: linear-gradient(120deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    h2 {
        color: #34495e;
        font-weight: 600;
        border-left: 5px solid #667eea;
        padding-left: 15px;
        margin-top: 30px;
    }
    
    h3 {
        color: #34495e;
        font-weight: 500;
    }
    
    
    .dataframe {
        border: 2px solid #667eea !important;
        border-radius: 10px;
        overflow: hidden;
    }
    
    
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        padding: 10px 30px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        transform: translateY(-2px);
    }
    
    
    .stAlert {
        border-radius: 10px;
        border-left: 5px solid #667eea;
    }
    
    
    .stSlider {
        padding: 10px 0;
    }
    
    
    [data-testid="stFileUploader"] {
        border: 2px dashed #667eea;
        border-radius: 10px;
        padding: 20px;
        background: rgba(102, 126, 234, 0.05);
    }
    
   
    .stRadio > label {
        font-weight: 600;
        color: #34495e;
    }
    
    
    hr {
        margin: 30px 0;
        border: 1px solid #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🐼 Nesli Tükenen Hayvanlar Veri Analizi")

st.markdown("""
<div style='background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%); 
            padding: 25px; border-radius: 15px; color: white; text-align: center; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.2); margin-bottom: 30px;'>
    <h3 style='color: white; margin: 0;'>Dünya Üzerindeki Nesli Tükenme Tehlikesi Altında Olan Hayvanlar</h3>
    <p style='margin: 10px 0 0 0; font-size: 16px;'>
        Koruma statüleri, popülasyon verileri ve tehdit seviyeleri ile kapsamlı analiz
    </p>
</div>
""", unsafe_allow_html=True)


@st.cache_data
def load_default_data():
    """Varsayılan veri setini GitHub'dan yükler"""
    default_url = "https://raw.githubusercontent.com/iremkay/veri-analizi-projesi/main/endangered_animals.csv"
    try:
        return pd.read_csv(default_url), True
    except:
        try:
            return pd.read_csv("endangered_animals.csv"), True
        except:
            return None, False



df, default_loaded = load_default_data()


with st.sidebar:
    st.header("Ayarlar")
    
    if default_loaded:
        st.success("✅ Veri seti yüklendi")
        st.caption(f"Toplam {len(df)} Hayvan Türü")
    else:
        st.error("❌ Veri seti yüklenemedi")

if df is not None:
    
    
    st.header("1. 📈 Veri Seti Genel Bakış")
    
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📋 Toplam Satır",
            value=f"{df.shape[0]:,}",
            delta="Veri Noktası"
        )
    
    with col2:
        st.metric(
            label="📊 Toplam Sütun",
            value=df.shape[1],
            delta="Özellik"
        )
    
    with col3:
        numeric_count = len(df.select_dtypes(include=['int64', 'float64']).columns)
        st.metric(
            label="🔢 Sayısal Sütun",
            value=numeric_count,
            delta="Numerik"
        )
    
    with col4:
        missing_percentage = (df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100)
        st.metric(
            label="⚠️ Eksik Veri",
            value=f"{missing_percentage:.1f}%",
            delta="Toplam",
            delta_color="inverse"
        )
    
    st.markdown("---")
    
    # ==============================
    # Pasta Grafikleri (Kategorik Dağılımlar)
    # ==============================
    st.header("1.5. Kategorik Veri Dağılımları")
    
    col1, col2, col3 = st.columns(3)
    
    # Koruma Statüsü Dağılımı
    with col1:
        if 'conservation_status' in df.columns:
            st.subheader("Koruma Statüsü")
            status_counts = df['conservation_status'].value_counts()
            
            fig, ax = plt.subplots(figsize=(8, 8))
            colors = ['#e74c3c', '#e67e22', '#f39c12']
            ax.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%',
                   colors=colors, startangle=90, textprops={'fontsize': 10})
            ax.set_title('Koruma Statüsü Dağılımı', fontsize=12, fontweight='bold', pad=20)
            st.pyplot(fig)
            plt.close()
    
    # Kıta Dağılımı
    with col2:
        if 'continent' in df.columns:
            st.subheader("Kıta Dağılımı")
            continent_counts = df['continent'].value_counts()
            
            fig, ax = plt.subplots(figsize=(8, 8))
            colors = plt.cm.Set3(range(len(continent_counts)))
            ax.pie(continent_counts.values, labels=continent_counts.index, autopct='%1.1f%%',
                   colors=colors, startangle=90, textprops={'fontsize': 10})
            ax.set_title('Kıtalara Göre Dağılım', fontsize=12, fontweight='bold', pad=20)
            st.pyplot(fig)
            plt.close()
    
    # Beslenme Türü Dağılımı
    with col3:
        if 'diet_type' in df.columns:
            st.subheader("Beslenme Türü")
            diet_counts = df['diet_type'].value_counts()
            
            fig, ax = plt.subplots(figsize=(8, 8))
            colors = ['#3498db', '#2ecc71', '#9b59b6']
            ax.pie(diet_counts.values, labels=diet_counts.index, autopct='%1.1f%%',
                   colors=colors, startangle=90, textprops={'fontsize': 10})
            ax.set_title('Beslenme Türü Dağılımı', fontsize=12, fontweight='bold', pad=20)
            st.pyplot(fig)
            plt.close()
    
    st.markdown("---")
    
    # Sütun İsimleri ve Tipleri
    with st.expander("📝 Sütun İsimleri ve Tipleri"):
        col_info = pd.DataFrame({
            'Sütun Adı': df.columns,
            'Veri Tipi': df.dtypes.astype(str),
            'Benzersiz Değer': [df[col].nunique() for col in df.columns],
            'Örnek Değer': [str(df[col].iloc[0]) if len(df) > 0 else 'N/A' for col in df.columns]
        })
        st.dataframe(col_info, use_container_width=True, height=300)
    
   
    st.header("2. 🔍 Ham Veri Önizleme")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        rows_to_show = st.slider(
            "Gösterilecek satır sayısını seçin:",
            min_value=5,
            max_value=min(50, len(df)),
            value=min(10, len(df))
        )
    
    with col2:
        view_option = st.selectbox(
            "Görünüm Seç",
            ["İlk Satırlar", "Son Satırlar", "Rastgele Örnek"]
        )
    
    st.markdown("")
    
    if view_option == "İlk Satırlar":
        st.dataframe(df.head(rows_to_show), use_container_width=True, height=400)
    elif view_option == "Son Satırlar":
        st.dataframe(df.tail(rows_to_show), use_container_width=True, height=400)
    else:
        st.dataframe(df.sample(min(rows_to_show, len(df))), use_container_width=True, height=400)
    
    
    st.header("3. İstatistiksel Özet")
    
    tab1, tab2 = st.tabs(["Sayısal Özellikler", "Tüm Özellikler"])
    
    with tab1:
        numeric_df = df.select_dtypes(include=['int64', 'float64'])
        if len(numeric_df.columns) > 0:
            st.dataframe(numeric_df.describe(), use_container_width=True, height=350)
        else:
            st.info("Bu veri setinde sayısal sütun bulunmamaktadır.")
    
    with tab2:
        describe_all = df.describe(include="all")
        st.dataframe(describe_all, use_container_width=True, height=350)
    
    
    st.header("4. 🏷️ Veri Tipleri ve Detaylar")
    
    dtypes_df = pd.DataFrame({
        "Sütun": df.columns,
        "Veri Tipi": df.dtypes.astype(str),
        "Null Sayısı": df.isnull().sum().values,
        "Null %": (df.isnull().sum() / len(df) * 100).round(2).values,
        "Benzersiz Değer": [df[col].nunique() for col in df.columns],
        "Hafıza (KB)": (df.memory_usage(deep=True).values[1:] / 1024).round(2)
    })
    
    st.dataframe(
        dtypes_df.style.background_gradient(subset=['Null %'], cmap='Reds'),
        use_container_width=True,
        height=350
    )
    
   
    st.header("5. ⚠️ Eksik Değer Analizi")
    
    total_missing = df.isnull().sum().sum()
    
    if total_missing == 0:
        st.success("🎉 Harika! Veri setinizde hiç eksik değer bulunmamaktadır.")
    else:
        st.warning(f"⚠️ Toplam {total_missing} eksik değer tespit edildi.")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            missing_df = pd.DataFrame({
                "Sütun": df.columns,
                "Eksik Değer": df.isnull().sum(),
                "Yüzde (%)": (df.isnull().sum() / len(df) * 100).round(2)
            })
            missing_df = missing_df[missing_df['Eksik Değer'] > 0].sort_values('Eksik Değer', ascending=False)
            
            if len(missing_df) > 0:
                st.dataframe(
                    missing_df.style.background_gradient(subset=['Yüzde (%)'], cmap='YlOrRd'),
                    use_container_width=True,
                    height=300
                )
        
        with col2:
            if len(missing_df) > 0:
                fig, ax = plt.subplots(figsize=(8, 6))
                colors = plt.cm.RdYlGn_r(missing_df['Yüzde (%)'] / 100)
                ax.barh(missing_df['Sütun'], missing_df['Eksik Değer'], color=colors)
                ax.set_xlabel('Eksik Değer Sayısı', fontsize=11, fontweight='bold')
                ax.set_title('Sütunlara Göre Eksik Değer Dağılımı', fontsize=13, fontweight='bold')
                ax.grid(axis='x', alpha=0.3, linestyle='--')
                plt.tight_layout()
                st.pyplot(fig)
                plt.close()
    
    
    st.markdown("---")
    
   
    numeric_features = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    
    if len(numeric_features) > 0:
        st.header("6. Sayısal Özellikler ve Korelasyon Analizi")
        
        with st.expander("Tespit Edilen Sayısal Özellikler", expanded=False):
            cols = st.columns(min(len(numeric_features), 4))
            for idx, feature in enumerate(numeric_features):
                with cols[idx % 4]:
                    st.markdown(f"""
                    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                padding: 10px; border-radius: 8px; text-align: center;
                                color: white; margin: 5px;'>
                        <b>{feature}</b>
                    </div>
                    """, unsafe_allow_html=True)
        
      
        st.subheader("Korelasyon Isı Haritası")
        
        corr_matrix = df[numeric_features].corr()
        
       
        fig, ax = plt.subplots(figsize=(12, 10))
        
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)
        
        sns.heatmap(
            corr_matrix,
            annot=True,
            fmt=".2f",
            cmap="RdBu_r",
            linewidths=1,
            ax=ax,
            center=0,
            mask=mask,
            square=True,
            cbar_kws={"shrink": 0.8, "label": "Korelasyon Katsayısı"},
            vmin=-1,
            vmax=1
        )
        
        ax.set_title("Sayısal Özelliklerin Korelasyon Isı Haritası", fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        
        with st.expander("En Yüksek Korelasyonlar", expanded=False):
            corr_pairs = corr_matrix.unstack()
            corr_pairs = corr_pairs[corr_pairs < 1.0].abs().sort_values(ascending=False)
            top_corr = corr_pairs.head(10)
            
            for idx, (pair, value) in enumerate(top_corr.items(), 1):
                st.markdown(f"**{idx}.** `{pair[0]}` ↔ `{pair[1]}`: **{value:.3f}**")
        
       
        st.header("7. Sayısal Özelliklerin Standartlaştırılması")
        
       
        scaler = StandardScaler()
        
        standardized_values = scaler.fit_transform(df[numeric_features])
        
        df_standardized = pd.DataFrame(
            standardized_values,
            columns=numeric_features
        )
        
        
        comparison_option = st.radio(
            "Görüntüleme Modu:",
            ["Standartlaştırılmış Veri", "Orijinal vs Standartlaştırılmış Karşılaştırma"],
            horizontal=True
        )
        
        rows_to_show_std = st.slider(
            "Gösterilecek satır sayısını seçin:",
            min_value=5,
            max_value=min(50, len(df)),
            value=min(10, len(df)),
            key="std_rows"
        )
        
        if comparison_option == "Standartlaştırılmış Veri":
            st.dataframe(df_standardized.head(rows_to_show_std), use_container_width=True, height=350)
        else:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**📄 Orijinal Veri**")
                st.dataframe(df[numeric_features].head(rows_to_show_std), use_container_width=True, height=350)
            with col2:
                st.markdown("**⚖️ Standartlaştırılmış Veri**")
                st.dataframe(df_standardized.head(rows_to_show_std), use_container_width=True, height=350)
        
     
        if len(numeric_features) >= 2:
            st.header("8. Temel Bileşen Analizi (PCA)")
            
            
            pca = PCA(n_components=2)
            pca_components = pca.fit_transform(df_standardized)
            
            pca_df = pd.DataFrame(
                pca_components,
                columns=["PC1", "PC2"]
            )
            
           
            explained_variance = pca.explained_variance_ratio_
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    label="🟦 PC1 Varyans",
                    value=f"{explained_variance[0]:.1%}",
                    delta="Birinci Bileşen"
                )
            
            with col2:
                st.metric(
                    label="🟩 PC2 Varyans",
                    value=f"{explained_variance[1]:.1%}",
                    delta="İkinci Bileşen"
                )
            
            with col3:
                st.metric(
                    label="🎯 Toplam Varyans",
                    value=f"{explained_variance.sum():.1%}",
                    delta="PC1 + PC2"
                )
            
            st.markdown("---")
            
            
            st.subheader("PCA Dağılım Grafiği (PC1 vs PC2)")
            
            fig, ax = plt.subplots(figsize=(10, 7))
            
            scatter = ax.scatter(
                pca_df["PC1"],
                pca_df["PC2"],
                alpha=0.7,
                c=range(len(pca_df)),
                cmap='viridis',
                edgecolors='black',
                linewidth=0.5,
                s=100
            )
            
            ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5, linewidth=1)
            ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5, linewidth=1)
            
            ax.set_xlabel(f"Birinci Temel Bileşen (PC1) - {explained_variance[0]:.1%} Varyans",
                         fontsize=12, fontweight='bold')
            ax.set_ylabel(f"İkinci Temel Bileşen (PC2) - {explained_variance[1]:.1%} Varyans",
                         fontsize=12, fontweight='bold')
            ax.set_title("İlk İki Temel Bileşenin Dağılım Grafiği", fontsize=14, fontweight='bold', pad=15)
            ax.grid(True, alpha=0.3, linestyle='--')
            
            plt.colorbar(scatter, ax=ax, label='Veri Noktası İndeksi')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
            
            
            st.header("9. Sayısal Özelliklerin Kutu Grafikleri ve Aykırı Değer Analizi")
            
            
            selected_features = st.multiselect(
                "Görselleştirmek istediğiniz özellikleri seçin:",
                numeric_features,
                default=numeric_features[:min(4, len(numeric_features))]
            )
            
            if selected_features:
                
                num_cols = min(2, len(selected_features))
                num_rows = (len(selected_features) + num_cols - 1) // num_cols
                
                fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))
                
                if num_rows == 1 and num_cols == 1:
                    axes = [axes]
                elif num_rows == 1 or num_cols == 1:
                    axes = axes.flatten()
                else:
                    axes = axes.flatten()
                
                colors = plt.cm.Set3(range(len(selected_features)))
                
                for idx, feature in enumerate(selected_features):
                    if idx < len(axes):
                        box_plot = axes[idx].boxplot(
                            df[feature].dropna(),
                            vert=True,
                            patch_artist=True,
                            widths=0.6,
                            boxprops=dict(facecolor=colors[idx], alpha=0.7),
                            medianprops=dict(color='red', linewidth=2),
                            whiskerprops=dict(color='black', linewidth=1.5),
                            capprops=dict(color='black', linewidth=1.5)
                        )
                        
                        axes[idx].set_title(f'{feature} - Kutu Grafiği', fontsize=12, fontweight='bold')
                        axes[idx].set_ylabel(feature, fontsize=11, fontweight='bold')
                        axes[idx].grid(axis='y', alpha=0.3, linestyle='--')
                        axes[idx].set_facecolor('#f8f9fa')
                
               
                for idx in range(len(selected_features), len(axes)):
                    axes[idx].axis('off')
                
                plt.tight_layout()
                st.pyplot(fig)
                plt.close()
                
                
                with st.expander("Aykırı Değer İstatistikleri", expanded=False):
                    outlier_stats = []
                    for feature in selected_features:
                        Q1 = df[feature].quantile(0.25)
                        Q3 = df[feature].quantile(0.75)
                        IQR = Q3 - Q1
                        outliers = df[(df[feature] < Q1 - 1.5 * IQR) | (df[feature] > Q3 + 1.5 * IQR)][feature]
                        
                        outlier_stats.append({
                            'Özellik': feature,
                            'Aykırı Değer Sayısı': len(outliers),
                            'Aykırı Değer Yüzdesi': f"{len(outliers) / len(df) * 100:.2f}%",
                            'Alt Sınır': f"{Q1 - 1.5 * IQR:.2f}",
                            'Üst Sınır': f"{Q3 + 1.5 * IQR:.2f}"
                        })
                    
                    outlier_df = pd.DataFrame(outlier_stats)
                    st.dataframe(outlier_df, use_container_width=True)
            else:
                st.info("👆 Lütfen en az bir özellik seçin.")
            
            
            if len(numeric_features) <= 6 and len(numeric_features) >= 2:
                st.header("10. Sayısal Özelliklerin Dağılım Grafikleri (Pair Plot)")
                
                if st.button("🎨 Pair Plot Oluştur", key="pairplot_btn"):
                    with st.spinner('Pair plot oluşturuluyor...'):
                        try:
                            sample_features = numeric_features[:6]
                            plot_data = df[sample_features].dropna()
                            
                            if len(plot_data) > 0:
                                fig = sns.pairplot(
                                    plot_data,
                                    diag_kind='kde',
                                    corner=False,
                                    plot_kws={'alpha': 0.6, 's': 50, 'edgecolor': 'k'},
                                    diag_kws={'alpha': 0.7}
                                )
                                fig.fig.suptitle('Sayısal Özelliklerin Pair Plot Analizi', y=1.01, fontsize=16, fontweight='bold')
                                st.pyplot(fig)
                                plt.close()
                            else:
                                st.warning("Pair plot oluşturmak için yeterli veri yok.")
                        except Exception as e:
                            st.error(f"Pair plot oluşturulurken hata: {str(e)}")
    
    else:
        st.warning("⚠️ Veri setinde sayısal özellik bulunamadı!")
    
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
                border-radius: 15px; margin-top: 50px;'>
        <p style='color: white; margin: 0; font-size: 14px;'>
            <b>Nesli Tükenen Hayvanlar Veri Analizi</b><br>
            Dünya Üzerindeki Koruma Statüleri ve Popülasyon Verileri<br>
            Doğayı Koruyalım
        </p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error("❌ Veri seti yüklenemedi. Lütfen sidebar'dan farklı bir veri seti yükleyin.")
    st.info("💡 Sidebar'dan (sol menü) farklı bir veri seti yükleyebilirsiniz.")
