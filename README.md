# 🇪🇺 European Macroeconomic Panel Data Dashboard

A professional panel data analysis and econometric visualization tool built with **Python**, **Streamlit**, and the **World Bank API**. This web application automates data fetching, processing, and advanced panel econometric modeling (Fixed Effects) for major European economies.

---

## 🚀 Key Features
* **Live Data Integration:** Automatically fetches macroeconomic indicators (GDP Growth, Inflation) directly from the World Bank API for selected European countries (Italy, Germany, France, Spain) spanning from 2010 to 2023.
* **Panel Data Processing:** Structures raw API responses into a clean Multi-Index panel dataset (`Country`, `Year`) using `pandas`.
* **Econometric Modeling:** Implements rigorous panel data regression via `linearmodels` and `statsmodels` to run **Panel Fixed Effects (`PanelOLS`)** estimations with entity and time effects.
* **Interactive UI:** Built with **Streamlit** to provide a clean, browser-based dashboard interface.

---

## 🛠️ Tech Stack & Libraries
* **Python** (Core Programming)
* **Streamlit** (Web Application Framework)
* **Pandas & NumPy** (Data Wrangling & Transformation)
* **Requests** (API Data Extraction)
* **Linearmodels & Statsmodels** (Econometric Panel Regression)

---

## 📂 Project Structure
```text
├── app.py              # Main Streamlit application and econometric pipeline
└── requirements.txt    # Required Python packages and dependencies
⚙️ Installation & Running Locally
Clone the repository:

Bash
git clone [https://github.com/Maryam676-awais/EU-Macroeconomic-Panel-Dashboard.git](https://github.com/Maryam676-awais/EU-Macroeconomic-Panel-Dashboard.git)
cd EU-Macroeconomic-Panel-Dashboard
Install dependencies:

Bash
pip install -r requirements.txt
Run the Streamlit app:

Bash
streamlit run app.py
Developed with a focus on Applied Econometrics and Data Science.
