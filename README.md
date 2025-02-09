
## How to Run the Project

1. **Data Cleaning:**  
   Run the `01_XYZ_campaign_data_cleaning.ipynb` notebook to clean the raw data. The processed data is saved in the `data/` folder.

2. **Feature Engineering:**  
   Execute `02_XYZ_campaign_feature_engineering.ipynb` to apply feature engineering techniques and detect outliers using Isolation Forest. The resulting dataset is stored in the `data/` folder.

3. **Exploratory Data Analysis (EDA):**  
   Open and run `03_XYZ_campaign_EDA.ipynb` to explore data distributions, campaign reach, and key sociodemographic insights.

4. **Predictive Modeling:**  
   Run `04_XYZ_campaign_predictive_modeling.ipynb` for model selection, evaluation, tuning, and feature selection. Trained models are saved in the `models/` folder.

## Data Sources

- **Raw Data:** Located in the `data/raw/` directory.
- **Refined Data:** Cleaned and feature engineered data is available in the `data/` directory.

## Models

All trained predictive models are saved in the `models/` directory for further analysis and potential deployment:
- Random Forrest is trained to aggressivly target the positive class and is best suited for aiding an aggressive marketing approach;
- Gradient Booster is the most accurate option but it struiggles with the positive class (recall especially);
- LinearSVC sacrifices a bot of accuracy for a more balanced performace across both classes;

## Dependencies

This project is implemented in Python 3.x. Key libraries include:
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib
- Jupyter Notebook
- dill

A complete list of dependencies and their versions is available in the `requirements.txt` file.

## Task Instructions

For detailed project requirements and guidelines, please refer to the [task instructions](<Senior Role Task.docx>) file located in the root directory.