# Personalized Embryo Implantation Predictor

This project predicts the probability of embryo implantation during IVF treatment using machine learning techniques. The model is trained on a synthetic IVF dataset to preserve patient privacy while capturing clinically meaningful patterns.

## Problem Statement
Embryo implantation failure is a major challenge in IVF treatments. This project aims to assist clinical decision-making by predicting implantation success based on patient-specific parameters.

## Dataset
- Cervical cancer Kaggle datasets 

Features:
- Female Age
- BMI
- AMH Level
- Endometrium Thickness
- Embryo Quality
- Previous IVF Failures

Target Variable:
- Implantation Outcome (0 = Failure, 1 = Success)

## Methodology
1. Synthetic data generation and preprocessing
2. Feature engineering
3. Training classification models
4. Model evaluation using medical-relevant metrics
5. Deployment via a web application

## Machine Learning Models
- Logistic Regression (baseline)
- Random Forest / XGBoost

## Evaluation Metrics
- ROC-AUC Score
- Recall
- Confusion Matrix

## Results
The model demonstrates reliable predictive performance on synthetic data and identifies key factors influencing embryo implantation outcomes.

## Web Application
A web-based interface is developed using Flask / Streamlit that allows users to input patient parameters and receive implantation probability predictions.

## Project Structure
- app.py
- ivf_model_training.ipynb
- synthetic_ivf_dataset.csv
- README.md

## Disclaimer
This project is intended for educational and research purposes only and should not be used for real clinical decision-making.
