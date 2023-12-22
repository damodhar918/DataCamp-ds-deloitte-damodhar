# Healthcare Revenue Project Readme

## Introduction

The healthcare revenue project aims to analyze the drivers of revenue for FMPF Medical Group across various clinics and hospitals in different locations. The project involves data analysis and predictive modeling to provide insights and recommendations to the Financial Planning Team.

## Business Goals

The project's main business goal is to help the medical group better understand their revenue drivers to make informed decisions and improve growth. The team also aims to predict revenue within 10% of actual values, though it is unclear if this is a realistic goal given the time frame. To achieve the project goals, the analysis involves data validation and cleaning, exploratory analysis, model development, model evaluation, and defining metrics for the business to monitor.

## Project Overview

The project's data is collected from various clinics and hospitals over the past year, with each clinic providing data from a random day in the year. The data consists of patient numbers and ratios, satisfaction scores, ownership type, location type, admitted patients, nurse-patient ratios, emergency department visits, and revenue. The data set has been validated, cleaned, and explored to provide insights and recommendations.

## Data Validation

Data validation is crucial to ensure the accuracy and reliability of the analysis. The health revenue dataset consisted of 1990 rows and 8 columns, which was collected over the past year from various clinics/hospitals across the country on a random date for each clinic. After validation, there were 1814 rows remaining. The data dictionary shows the column name, data type, allowed values, number of rows, number of missing values, and possible values/range.

## Exploratory Data Analysis

Exploratory data analysis is carried out for numeric and categorical attributes to understand the data's characteristics and relationships.

## Model Development/Business Focus

The aim of the project is to predict revenue within a 10% margin of error by using other variables in the dataset. The problem type in the dataset is regression.

## Prepare Data for Modelling

To enable modeling, the project chose clinic_id, ownership, hospital_location, admitted_patients, nurse_patient_ratio, ed_visits, and satisfaction_score as features and revenue as the target variable.

## Model Evaluation

Linear regression and random forest regression models were used for evaluation, with R-squared and RMSE as evaluation metrics.

## Models Result

Both models performed similarly, but the low R-squared values indicate that they cannot accurately predict revenue within the desired range.

## Final Summary and Recommendations

The project's findings indicate that location and ownership type of clinics have a significant influence on revenue generation. Further improvements to the existing models are suggested to meet the business objective of accurately predicting revenue within a 10% margin of error. Additional data acquisition, feature engineering, and exploring additional features are recommended. The project also suggests implementing strategies to improve patient satisfaction scores, as they are vital in clinic revenue.

