import streamlit as st
from db_utils import get_db_connection, get_cursor
from core_logic import YEAR, TAGS
import ui_pages

st.set_page_config(page_title="Vision 2026", layout="wide")

# --- SHARED STATE ---
if "user" not in st.session_state:
    st.session_state.user = None

conn = get_db_connection()
cur = get_cursor(conn)

# --- LANDING PAGE (EXACT HERO LAYOUT) ---
if st.session_state.user is None:
    col_img, col_text = st.columns([1.2, 1], gap="large")
    with col_img:
        st.image("https://images.unsplash.com/photo-1493612276216-ee3925520721?q=80&w=2000&auto=format&fit=crop", 
                 caption="Strategy is the art of closing the gap between vision and reality.")
    with col_text:
        st.title("🎯 Vision 2026")
        st.subheader("The Behavioral Feedback System")
        st.markdown("""
        Fix your integrity by tracking behaviors, not just results.
        * **🚀 Execution Grid:** Goal-centric daily matrix.
        * **🗓️ ISO-Week Logic:** Fair, mathematical accountability.
        * **📊 Strategic Reflection:** Automated long-term health checks.
        """)
        st.divider()

        auth_tab1, auth_tab2 = st.tabs(["🔒 Secure Login", "✨ Join Vision 2026"])
        with auth_tab1:
            email = st.text_input("Email", key="login_email")
            pw = st.text_input("Password", type="password", key="login_pw")
            if st.button("Enter Workspace", use_container_width=True, type="primary"):
                cur.execute("SELECT * FROM users WHERE email=%s AND password_hash=%s", (email, pw))
                u = cur.fetchone()
                if u: 
                    st.session_state.user = u
                    st.rerun()
                else: st.error("Invalid credentials.")
        with auth_tab2:
            reg_email = st.text_input("New Email", key="reg_email")
            reg_pw = st.text_input("New Password", type="password", key="reg_pw")
            if st.button("Create My System", use_container_width=True):
                try:
                    cur.execute("INSERT INTO users (email, password_hash) VALUES (%s, %s)", (reg_email, reg_pw))
                    conn.commit()
                    st.success("Account created! Log in above.")
                except: st.error("Email already exists.")

    st.markdown("---")
    st.caption("“We are what we repeatedly do. Excellence, then, is not an act, but a habit.” — Aristotle")

# --- MAIN APP UI ---
else:
    u_id = st.session_state.user['id']
    with st.sidebar:
        st.write(f"Logged in: **{st.session_state.user['email']}**")
        nav = st.radio("Menu", ["🏗️ Setup", "📅 Execution", "📊 Reports"])
        if st.button("Logout"):
            st.session_state.user = None
            st.rerun()

    if nav == "🏗️ Setup":
        ui_pages.render_setup(u_id, cur, conn)
    elif nav == "📅 Execution":
        ui_pages.render_execution(u_id, cur, conn)
    elif nav == "📊 Reports":
        ui_pages.render_reports(u_id, cur)

cur.close()
conn.close()