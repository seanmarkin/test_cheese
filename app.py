import streamlit as st
import sqlite3

# Setting up the database
def setup_database():
    conn = sqlite3.connect('researchers.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS researchers 
                 (name TEXT PRIMARY KEY, contribution TEXT)''')
    conn.commit()
    conn.close()

setup_database()

def add_researcher(name, contribution):
    conn = sqlite3.connect('researchers.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO researchers (name, contribution) VALUES (?, ?)", (name, contribution))
    conn.commit()
    conn.close()

def generate_statement():
    conn = sqlite3.connect('researchers.db')
    c = conn.cursor()
    researchers = c.execute("SELECT * FROM researchers").fetchall()
    conn.close()
    
    statement = ""
    for researcher in researchers:
        statement += researcher[0] + " " + researcher[1] + "\n"
    return statement

# Streamlit app
st.title('Researcher Contributions')

name = st.text_input("Researcher's Name")

contributions = ["Contribution 1", "Contribution 2", "Contribution 3", "Other"]
contribution = st.selectbox("Select Contribution", contributions)

if contribution == "Other":
    contribution = st.text_input("Enter the new contribution:")

if st.button("Add Researcher"):
    if name and contribution:
        add_researcher(name, contribution)
        st.success(f"Added {name} with contribution {contribution}")

if st.button("Generate Statement"):
    statement = generate_statement()
    st.text_area("Researchers and Contributions:", value=statement, height=300)

st.write("Note: Refresh the page to add more researchers.")