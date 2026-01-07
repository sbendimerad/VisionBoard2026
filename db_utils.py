import psycopg2
from psycopg2.extras import RealDictCursor
import streamlit as st

def get_db_connection():
    return psycopg2.connect(st.secrets["DATABASE_URL"], sslmode='require')

def get_cursor(conn):
    return conn.cursor(cursor_factory=RealDictCursor)