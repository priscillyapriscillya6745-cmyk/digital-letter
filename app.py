import streamlit as st
import base64
import time

st.set_page_config(page_title="Untuk Kamu 💌", page_icon="💌", layout="centered")

# ====== CSS CUSTOM ======
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400&display=swap');

/* Background gradient romantis */
.stApp {
    background: linear-gradient(135deg, #ffe0ec 0%, #ffc2d1 50%, #ffb3c6 100%);
    background-attachment: fixed;
}

/* Sembunyikan header & footer Streamlit */
#MainMenu, header, footer {visibility: hidden;}

/* Judul */
h1 {
    font-family: 'Dancing Script', cursive !important;
    color: #d6336c !important;
    text-align: center;
    font-size: 4rem !important;
    text-shadow: 2px 2px 8px rgba(214,51,108,0.2);
    animation: fadeIn 2s ease-in;
}

/* Teks paragraf */
p, .stMarkdown {
    font-family: 'Poppins', sans-serif;
    color: #7a2e4a;
    text-align: center;
    font-size: 1.1rem;
    line-height: 1.8;
}

/* Tombol cantik */
.stButton > button {
    background: linear-gradient(135deg, #ff6b9d, #d6336c);
    color: white;
    border: none;
    border-radius: 50px;
    padding: 14px 40px;
    font-size: 1.1rem;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    box-shadow: 0 8px 20px rgba(214,51,108,0.3);
    transition: all 0.3s ease;
    display: block;
    margin: 0 auto;
}
.stButton > button:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 12px 28px rgba(214,51,108,0.5);
}

/* Kartu surat */
.letter-card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    border-radius: 24px;
    padding: 40px;
    margin: 30px auto;
    max-width: 600px;
    box-shadow: 0 20px 50px rgba(214,51,108,0.2);
    animation: slideUp 1s ease-out;
    border: 1px solid rgba(255,255,255,0.6);
}

/* Animasi */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Hati berjatuhan */
.heart {
    position: fixed;
    top: -10%;
    color: #ff6b9d;
    font-size: 1.5rem;
    animation: fall linear infinite;
    z-index: 0;
    opacity: 0.7;
}
@keyframes fall {
    to { transform: translateY(110vh) rotate(360deg); }
}
</style>

<!-- Hati berjatuhan -->
<div class="heart" style="left:10%; animation-duration:6s;">💗</div>
<div class="heart" style="left:25%; animation-duration:8s; animation-delay:1s;">💕</div>
<div class="heart" style="left:45%; animation-duration:7s; animation-delay:2s;">💖</div>
<div class="heart" style="left:65%; animation-duration:9s; animation-delay:0.5s;">💗</div>
<div class="heart" style="left:85%; animation-duration:6.5s; animation-delay:3s;">💕</div>
""", unsafe_allow_html=True)

# ====== MUSIK (opsional) ======
# Taruh file lagu.mp3 di folder yang sama
def autoplay_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        pass

# autoplay_audio("lagu.mp3")  # uncomment kalau ada musik

# ====== KONTEN ======
st.markdown("<h1>💌 </h1>", unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)

# Tombol buka surat
if st.button("Buka  💖"):
    st.balloons()
    time.sleep(0.5)
    
    st.markdown("""
    <div class="letter-card">
        <p style="font-family:'Dancing Script',cursive; font-size:2rem; color:#d6336c; margin-bottom:20px;">
            untuk jessie,
        </p>
        <p>
            Thank you ya uda mau percaya cerita cerita gua sama nahan ua sering yapping atau ga ngajak ribut hehe.
        </p>
        <p>
           Lain kali kalo ada masalah cerita aja yaa jangan dipendem mulu sendirian kalo malu anggap aja gua tembok yang bisa ngomong ajaa.
        </p>
        <p style="font-size:1.3rem; font-weight:500; color:#d6336c; margin-top:25px;">
             🌷
        </p>
        <p style="margin-top:20px; font-style:italic;">
            — dari zosimo 😝😝😝
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.snow()  # efek salju (opsional, bisa diganti)
