# Weather and Air Quality Analysis in Ho Chi Minh City

## Project Overview
This project aims to analyze the relationship between weather conditions and air quality in Ho Chi Minh City, Vietnam. By leveraging real-world data, the goal is to uncover insights that can help improve understanding of the factors influencing air pollution in the city. From there, we can implement health protection measures for the local population against the effects of air quality.

## Objectives
1. Collect relevant data on weather and air quality for Ho Chi Minh City.
2. Preprocess and clean the data for analysis.
3. Conduct exploratory data analysis to understand trends and patterns.
4. Build predictive models to quantify the impact of weather on air quality.
5. Identify key factors contributing to poor air quality and provide mitigation recommendations.

## Data Sources
- Weather and AQ datasets: [Open-Meteo](https://open-meteo.com/)

## Methodology
1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis
4. Predictive Modeling
5. Interpretation and Recommendations

## Project Organization
- `data/`: Collected and preprocessed data
- `notebooks/`: Jupyter notebooks for analysis
- `model/`: Store the models' weights
- `img`: Store the plot images
- `requirements.txt`: list of Python libraries needed for project

## Getting Started

To set up and run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mtue04/HCMC-WAQ-Analysis.git
    cd HCMC-WAQ-Analysis
    ```

2. **Set up the environment**:

- Set up virtual environment:
    ```bash
    conda create -n venv python=3.9 -y
    conda activate venv
    ```

- Create GROQ API Key to run the app.ipynb file:
    - Go to [groq website](https://console.groq.com/keys)
    - Sign in to your account, or create one if you don't already have an account.
    - Once logged in, navigate to the **API Keys** section in your GROQ dashboard.
    - Click on **Create API Key** to generate a new API Key.
    - Create a file named **.env** and write:   
    ```bash
    GROQ_API_KEY = "Your generated API Key"
    ```

3. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the notebooks**:
    - Open the Jupyter notebooks in the `notebooks/` folder to view and run.
        - `1 - collecting_data.ipynb`: Data collection
        - `2 - preprocessing_data.ipynb`: Data preprocessing
        - `3.1 - eda.ipynb`: EDA
        - `3.2 - questioning.ipynb`: Question Analyzing for key insights
        - `4.1 - us_aqi_prediction.ipynb`: US AQI Prediction model
        - `4.2 - weather_status_classification.ipynb`: Weather Status Classification model
        - `5 - app.ipynb`: The Web Demo for project

- **Tip**: Make sure to run all cells in each notebook in the correct order, from top to bottom, to ensure that variables, functions, and models are defined properly.
    - If you encounter issues with running notebooks in sequence, check if any dependencies or variables are not defined due to skipped cells or errors.

## How to Contribute
If you want to contribute to this project, follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Create a pull request with a detailed explanation of your changes.

## Group's Resources (Timeline, Meeting notes, Docs)
- [Project Drive](https://drive.google.com/drive/folders/11HrSxnZGHwgdIZdofiF2Ajjw2VtPV388).

## Contributors
This project is done by the Capydata group, class CLC2425HK1_CSC14119_22KHDL1, University of Science, VNU-HCM.

| Student ID | Name                   |
|------------|------------------------|
| 22127234   | Cao Hoàng Lộc          |
| 22127360   | Võ Nguyễn Phương Quỳnh |
| 22127440   | Phan Võ Minh Tuệ       |
| 22127450   | Phạm Anh Văn           |