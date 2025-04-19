import streamlit as st
import datetime

st.set_page_config(page_title="Nifty Breakout Signal", layout="wide")

st.title("Nifty Breakout Live Signal")
st.markdown("---")

# Dummy signal data (replace with real-time logic later)
signal_time = datetime.datetime.now().strftime("%H:%M:%S")
pattern = "Flag Breakout"
entry = 23820
target = 23900
stoploss = 23760

st.subheader("Today's Signal:")
st.success(f"**Pattern:** {pattern}")
st.info(f"**Time:** {signal_time}")
st.write(f"**Entry:** {entry}")
st.write(f"**Target:** {target}")
st.write(f"**Stop Loss:** {stoploss}")

st.markdown("---")
st.markdown("This signal is for educational purpose only.")
