
# XYZ Marketing Campaign Analysis

A comprehensive data science project analyzing advertising campaign effectiveness through exploratory data analysis, feature engineering, and predictive modeling. This project identifies patterns in socio-demographic influence on media consumption and provides actionable recommendations for optimizing advertising performance.

> **Note:** This project is based on a realistic business scenario with synthetic or anonymized data.

---

## 📊 Project Overview

### Problem Statement

- Which socio-demographic groups were most responsive to advertisements?
- Which media channels had the greatest impact on driving purchases?
- How can media exposure patterns optimize future marketing spend?

### Approach

1. **Exploratory Data Analysis** – Uncovered relationships between socio-demographics, media exposure, and purchase behavior
2. **Feature Engineering** – Created derived features (media exposure aggregations, outlier detection) to enhance model interpretability
3. **Predictive Modeling** – Trained and compared multiple classification models to identify purchase drivers
4. **Business Insights** – Generated actionable recommendations based on statistical findings

---

## 🔍 Key Findings

- **Age Demographics:** Older age groups (35+) showed 40-60% purchase rates; younger audiences (18-34) significantly underperformed at 37.3%
- **Media Dominance:** Traditional TV was the strongest channel by reach and effectiveness; digital media (YouTube) showed lower impact but better cost-efficiency for younger segments
- **Exposure Impact:** High media exposure increased purchase rates from 30% (low exposure) to 80% (high exposure) – a strong driver of conversions
- **Gender Neutrality:** Campaign performed equally well across genders (~50% purchase rate each), indicating balanced messaging
- **Household Factors:** Children and household size had minimal influence on purchase decisions

**See [Campaign Findings & Recommendations](./reports/FINDINGS.md) for detailed insights.**

---

## 📁 Project Structure

```text
├── data/
│   ├── raw/                          # Original datasets
│   │   ├── media_contacts.csv       # Media exposure by individual
│   │   └── socio_demos.csv          # Socio-demographic information
│   ├── 01_clean_data.csv            # Cleaned dataset
│   └── 02_engineered_data.csv       # Feature-engineered dataset
├── notebooks/
│   ├── 01_XYZ_campaign_data_cleaning.ipynb           # Data cleaning & preparation
│   ├── 02_XYZ_campaign_feature_engineering.ipynb     # Feature creation & outlier detection
│   ├── 03_XYZ_campaign_EDA.ipynb                      # Exploratory analysis & visualizations
│   └── 04_XYZ_campaign_predictive_modeling.ipynb     # Model selection, tuning & evaluation
├── src/
│   ├── utils.py                     # Reusable utilities (save/load data & models)
│   └── __init__.py
├── models/                          # Trained model artifacts
├── reports/
│   └── FINDINGS.md                  # Executive summary & recommendations
├── pyproject.toml                   # Project dependencies (uv)
└── README.md                        # This file
```

---

## 🚀 Quick Start

### Prerequisites

- Python >=3.11
- `uv` package manager ([install here](https://docs.astral.sh/uv/))

### Setup

```bash
# Clone the repository
git clone <repo-url>
cd XYZ-Marketing-Campaign

# Install dependencies
uv sync

# Activate environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Run the Analysis Pipeline

Execute the notebooks in order:

1. **Data Cleaning** – Standardize formats, handle missing values, remove inconsistencies

```bash
jupyter notebook notebooks/01_XYZ_campaign_data_cleaning.ipynb
```

1. **Feature Engineering** – Create derived features, detect outliers using Isolation Forest

```bash
jupyter notebook notebooks/02_XYZ_campaign_feature_engineering.ipynb
```

1. **Exploratory Data Analysis** – Visualize distributions, correlations, and campaign insights

```bash
jupyter notebook notebooks/03_XYZ_campaign_EDA.ipynb
```

1. **Predictive Modeling** – Train, tune, and compare classification models

```bash
jupyter notebook notebooks/04_XYZ_campaign_predictive_modeling.ipynb
```

Processed data and trained models are automatically saved to `data/` and `models/` directories.

---

## 🤖 Models Trained

All models are evaluated on F1-score and class-balanced metrics (due to class imbalance in purchase outcomes):

| Model | Purpose | Strengths |
|-------|---------|-----------|
| **Random Forest** | Aggressive targeting | Maximizes true positives; best for growth-focused campaigns |
| **Gradient Boosting** | Balanced performance | Highest overall accuracy; best for minimizing total errors |
| **LinearSVC** | Conservative targeting | Best class balance; recommended for cost-aware spending |

Models are saved as `.pkl` files in `models/` and can be loaded for inference using `src.utils.load_model()`.

---

## 📈 Technologies Used

- **Data Processing:** pandas, numpy, scikit-learn
- **Modeling:** scikit-learn, XGBoost
- **Experiment Tracking:** MLflow
- **Visualization:** matplotlib, seaborn
- **Utilities:** dill, tabulate, pyprojroot

---

## 📝 Documentation

- **[Task Definition](./docs/Senior-Role-Task.md)** – Original business requirements and acceptance criteria
- **[Campaign Findings & Recommendations](./reports/FINDINGS.md)** – Executive summary with actionable insights

---

## 💡 Key Takeaways

This project demonstrates a complete end-to-end data science workflow: from raw data exploration and cleaning, through feature engineering and EDA, to model selection and business recommendation generation. The analysis provides clear, data-driven guidance for optimizing future advertising campaigns by targeting high-value demographics and media channels efficiently.
