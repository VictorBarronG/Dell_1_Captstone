# Regression Analysis on Predicting Car Price
## Introduction
To complete our training at Talent Path, We must present a capstone project to demonstrate our skills and knowledge that we have been learning for the past few weeks. I have done an indepth analysis on a dataset and created a model that can predict car price at 92% accuracy. My goal for this project is to incorporate the prexisting knowledge that I have of cars and working at a dealership along with my knowledge and skills that I have learning throughout my training.

![img]["/Images/intro_three.PNG"]

## Objective
My Objective is to create a set of models with the dataset I cleaned to achieve an accuracy score above 70% with a low RMSE Score. I will then select a model and incorporate it into a small full stack aplication.

## Business Value
With this model a dealership or any user may use this to predict current market value of vehicles that may come in as trade ins or can be potentially be bought from an auto auction. By being able to predict the market value of the car the user can make an informed decision to purchase a vehicle at a good value or for a dealership to make a purchase of a vehicle knowing exactly the potential marginal profit it can make.

## Data
I obtained my dataset from kaggle called "US Used cars dataset". This dataset was created from a web scrapper in the month of September in 2020. This dataset contains 3 Million rows of data with 66 features that pertained to the car and the dealership information.
## Data Processing
### Remove Features
I decided to start my Data Processing by removing any features that we can simply remove that wont affect our target values and that arent relevant to our situation. As a result of individually looking at the descriptions I brought the amount of features from 66 to 22 including the target feature.
![img]["/Images/pros_1.PNG"]

### Cleaning Null Values
Now that the amount of features were reduced I want to remove the amount of nulls that are in the dataset. I used a heat map and value counts to show the amount in the dataset.
![img]["/Images/pros_2.PNG"]
![img]["/Images/pros_3.PNG"]

I decided to drop all the rows from the data that were missing values in features where I could not pull information from others features. This included featues such as Frame Damage, trim name, transmission, etc. There were some left over null values but overall the dataset was a lot cleaner and I still had over a millon rows remaining in my dataset.
The values that are left i want to leave for now as i might be able to remove some if some may be in our outliers.
![img]["/Images/pros_4.PNG"]

### Remove Outliers
Next I want to see how my data is distributed by price, so i selected a few features to plot against my target value price.
![img]["/Images/pros_5.PNG"]
![img]["/Images/pros_6.PNG"]
![img]["/Images/pros_7.PNG"]
![img]["/Images/pros_8.PNG"]

Based on the previous graphs it is very apparent that price has a lot of outliers in a lot of features. For this model to be as accurate as possible and not allow it to be skewed by these outliers in the high price range. I decided to drop all the rows that had a price value above $90,000. This resulted in removing roughly 5,000 rows. I reploted the previous graphs to compare.
![img]["/Images/pros_9.PNG"]
![img]["/Images/pros_10.PNG"]
![img]["/Images/pros_11.PNG"]
![img]["/Images/pros_12.PNG"]

The graphs are much cleaner and even on our scatterplot we can see there is a positive correlation. Although we do still have outliers in our data its not out of range with the overall dataset. I also do not want to go to a lower range in price because we do have biodesiel vehicles in our dataset which are typically in this upper price range.
### Remove Under Represented Values
After viewing the unique values count of the values in each feature I discovered that there are some that had very small counts in regards to the overall size of the data. For example the feature City had a very long list of unique values but almost half of the list had less then 100 records. With that being said some cities were being under represented so I decided to filter out values that were under represented in features for City and Make. I removed all values that had a count of 100 or less in City, and removed all the values that had a count less then 30 in Make.

### Replacing values
### Impute

## Training Models

## Comparing Models
## Next Steps
