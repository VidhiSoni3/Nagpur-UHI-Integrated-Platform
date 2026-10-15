"""Entry point for the integrated Nagpur UHI Streamlit platform."""
from pathlib import Path
import runpy

PROJECT_ROOT = Path(__file__).resolve().parent
PREDICTION_APP = PROJECT_ROOT / "app" / "app.py"

if not PREDICTION_APP.exists():
    import streamlit as st
    st.set_page_config(page_title="Nagpur UHI Integrated Platform", page_icon="🌡️", layout="wide")
    st.error("The prediction application file is missing.")
    st.caption("Expected file: app/app.py")
else:
    runpy.run_path(str(PREDICTION_APP), run_name="__main__")
