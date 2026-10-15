# Nagpur UHI Integrated Platform

A unified Streamlit platform for Nagpur's Summer 2026 Urban Heat Island (UHI) study.

## Planned modules

- Interactive land surface temperature (LST) prediction using NDVI, NDBI and T2M
- SHAP-based explanations for model predictions
- Date-wise spatial heat maps and UHI zone exploration
- Daily observation analysis and climate-resilience guidance

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
streamlit run app.py
```

## Current status

The prediction app is maintained under `app/app.py`, with its model and daily reference CSV under `model/` and `data/`. Spatial dashboard integration is in progress. The spatial model in the source dashboard uses Git LFS; confirm the full model artifact is accessible before enabling model-dependent spatial features.

## Source projects

- [Nagpur UHI Summer 2026](https://github.com/VidhiSoni3/Nagpur-UHI-Summer-2026)
- [Nagpur UHI Dashboard](https://github.com/Sanskruti1204/nagpur-uhi-dashboard)
