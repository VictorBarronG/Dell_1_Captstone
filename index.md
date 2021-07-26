# Regression Analysis on Predicting Car Price
## Introduction
To complete our training at Talent Path, We must present a capstone project to demonstrate our skills and knowledge that we have been learning for the past few weeks. I have done an indepth analysis on a dataset and created a model that can predict car price at 92% accuracy. My goal for this project is to incorporate the prexisting knowledge that I have of cars and working at a dealership along with my knowledge and skills that I have learning throughout my training.

![][../Images/intro_three.PNG]

## Objective
My Objective is to create a set of models with the dataset I cleaned to achieve an accuracy score above 70% with a low RMSE Score. I will then select a model and incorporate it into a small full stack aplication.

## Business Value
With this model a dealership or any user may use this to predict current market value of vehicles that may come in as trade ins or can be potentially be bought from an auto auction. By being able to predict the market value of the car the user can make an informed decision to purchase a vehicle at a good value or for a dealership to make a purchase of a vehicle knowing exactly the potential marginal profit it can make.

## Data
I obtained my dataset from kaggle called "US Used cars dataset". This dataset was created from a web scrapper in the month of September in 2020. This dataset contains 3 Million rows of data with 66 features that pertained to the car and the dealership information.
## Data Processing
### Remove Features
I decided to start my Data Processing by removing any features that we can simply remove that wont affect our target values and that arent relevant to our situation. As a result of individually looking at the descriptions I brought the amount of features from 66 to 22 including the target feature.
!!!! Image pros_1!!!!

### Cleaning Null Values
Now that the amount of features were reduced I want to remove the amount of nulls that are in the dataset. I used a heat map and value counts to show the amount in the dataset.
!!! Pros 2 and 3 !!!!
I decided to drop all the rows from the data that were missing values in features where I could not pull information from others features. This included featues such as Frame Damage, trim name, transmission, etc. There were some left over null values but overall the dataset was a lot cleaner and I still had over a millon rows remaining in my dataset.
The values that are left i want to leave for now as i might be able to remove some if some may be in our outliers.
!!! pros 4 !!!!!
### Remove Outliers
Next I want to see how my data is distributed by price, so i selected a few features to plot against my target value price.
!!!! pros 5-8 !!!
Based on the previous graphs it is very apparent that price has a lot of outliers in a lot of features. For this model to be as accurate as possible and not allow it to be skewed by these outliers in the high price range. I decided to drop all the rows that had a price value above $90,000. This resulted in removing roughly 5,000 rows. I reploted the previous graphs to compare.
!!!! pros 9 - 12 !!!!

### Remove Under Represented Values
### Replacing values
### Impute

## Training Models

## Comparing Models
## Next Steps
