# Diabetes Prediction App

This project is a web application for predicting diabetes based on various health parameters. It uses machine learning models to make predictions based on user inputs.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Running the Application](#running-the-application)
- [Model Deployment](#model-deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

The Diabetes Prediction App leverages a machine learning model to predict the likelihood of diabetes in users based on their health metrics. The model was trained using synthetic and real-world data, including clinical health datasets and Kaggle datasets.

## Features

- User-friendly web interface built with Flask.
- Predictions based on various health metrics like blood glucose levels, BMI, cholesterol levels, etc.
- Deployed on Render for easy accessibility.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/diabetes-prediction-app.git
    cd diabetes-prediction-app
    ```

2. **Create a virtual environment**:
    ```sh
    conda create --name myenv python=3.8
    conda activate myenv
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Download the model**:
   Ensure you have the trained model file `model_diabetes.pkl` in the `model` directory. If not, train the model using your data and save it using `pickle`.

2. **Run the Flask app**:
    ```sh
    python main.py
    ```

3. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000` to use the application.

## Running the Application

To run the application locally:

1. Ensure you have all dependencies installed (`requirements.txt`).
2. Start the Flask app:
    ```sh
    python main.py
    ```

## Model Deployment

The app is deployed on Render. Follow these steps to deploy your app on Render:

1. **Create a `Procfile`** with the following content:
    ```sh
    web: python main.py
    ```

2. **Initialize a git repository and commit your code**:
    ```sh
    git init
    git add .
    git commit -m "Initial commit"
    ```

3. **Push your code to a repository on a platform like GitHub**.

4. **Deploy on Render**:
   - Log in to Render and create a new Web Service.
   - Connect your GitHub repository.
   - Choose the branch to deploy.
   - Set the Build Command to:
     ```sh
     pip install -r requirements.txt
     ```
   - Set the Start Command to:
     ```sh
     python main.py
     ```
   - Click on "Create Web Service" to deploy your app.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any features or bug fixes.

## Acknowledgments

- Thanks to ChatGPT and Gemini for their assistance in generating synthetic data and providing insights.
- Data sources include real-world clinical datasets and Kaggle datasets.

