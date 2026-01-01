import streamlit as st
import plotly.graph_objects as go
from sir_model import SIRModel


st.set_page_config(page_title="COVID-19 SIR Simulator", layout="wide")
st.title("🦠 COVID-19 SIR Simulator (OOP & Euler)")

# Sidebar
st.sidebar.header("⚙️ Settings")
N = st.sidebar.number_input("Population (N)", 1000, 1000000, 10000)
I0 = st.sidebar.number_input("Initial Infected", 1, 1000, 5)
beta = st.sidebar.slider("Infection Rate (Beta)", 0.0, 1.0, 0.3)
gamma = st.sidebar.slider("Recovery Rate (Gamma)", 0.0, 1.0, 0.1)
days = st.sidebar.slider("Days", 30, 600, 180)

# Run Logic
model = SIRModel(N, I0, 0, beta, gamma)
t, S, I, R = model.run_simulation(days)

# Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=S, name='Susceptible', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=t, y=I, name='Infected', line=dict(color='red')))
fig.add_trace(go.Scatter(x=t, y=R, name='Recovered', line=dict(color='green')))
fig.update_layout(title="SIR Model Projections", xaxis_title="Days")

st.plotly_chart(fig, use_container_width=True)