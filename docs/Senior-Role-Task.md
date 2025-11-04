
# Task Definition

> **Note:** This project is based on a realistic business scenario for evaluating advertising effectiveness using data science techniques. All data is synthetic or anonymized.

## Background

You are tasked with analyzing an ad campaign by the company “XYZ” that ran for a couple of weeks. The company wants to evaluate how effectively the advertisement message reached the intended audience. To support this analysis, you have access to a sample dataset representing the population of the entire country where the campaign was active. This dataset includes socio-demographic information and detailed media consumption data for the sampled individuals.

## Objective

Explore the provided datasets, identify patterns in how socio-demographics influence media consumption, build a predictive model to understand drivers of purchases, and present actionable insights. Example questions from the client might include:

- Which age groups generated the highest number of impressions across all channels?

- What socio-demographic trends can be observed in media consumption for different channels?

- Which media channels had the greatest impact on driving purchases?

## Datasets

- `media_contacts` – number of times each individual in the sample was exposed to the advertisement on various media channels. There is also a column indicating if the individual has purchased the advertised product.

- `socio_demos` – socio-demographic information for each individual from the sample. There is also a weight column representing each individual's share of the total population for the country.

Files (in this repository):

- `data/raw/media_contacts.csv`

- `data/raw/socio_demos.csv`

## Additional instructions

1. Perform data cleaning and pre-processing to ensure the datasets are ready for analysis. Handle inconsistencies and anomalies (missing values, odd encodings, duplicates, outliers where appropriate).
2. Perform a thorough exploratory data analysis (EDA) and highlight interesting relationships, correlations, and abnormalities.
3. Create visualizations to support your analysis (distribution plots, channel impressions by demo segments, correlation matrix, etc.).
4. Develop a predictive model to provide deeper insights and answer specific business questions (for example: which factors most strongly predict purchase?).
5. Provide actionable recommendations to optimize advertising performance based on the insights gained.

## Deliverables

- Code — Python or R preferred. Structure code in `src/` and provide runnable notebooks in `notebooks/` (or scripts with a small runner). Keep reproducibility in mind.

- A short written summary (or slide deck) of findings and recommended actions for the client.

- Ready-to-run notebooks or scripts that reproduce the analysis and model training.

- A live presenting of the findings (as part of the interview process).

## Evaluation Criteria

- Coding style, readability, and efficiency.

- Analytical approach and creativity.

- Clarity and quality of insights.

- Ability to communicate the findings effectively.

---
