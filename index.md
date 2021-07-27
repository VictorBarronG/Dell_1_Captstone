# Regression Analysis on Predicting Car Price
## Introduction
To complete our training at Talent Path, We must present a capstone project to demonstrate our skills and knowledge that we have been learning for the past few weeks. I have done an indepth analysis on a dataset and created a model that can predict car price at 92% accuracy. My goal for this project is to incorporate the prexisting knowledge that I have of cars and working at a dealership along with my knowledge and skills that I have learning throughout my training.

![img](/Images/intro_three.PNG)

## Objective
My Objective is to create a set of models with the dataset I cleaned to achieve an accuracy score above 70% with a low RMSE Score. I will then select a model and incorporate it into a small full stack aplication.

## Business Value
With this model a dealership or any user may use this to predict current market value of vehicles that may come in as trade ins or can be potentially be bought from an auto auction. By being able to predict the market value of the car the user can make an informed decision to purchase a vehicle at a good value or for a dealership to make a purchase of a vehicle knowing exactly the potential marginal profit it can make.

## Data
I obtained my dataset from kaggle called "US Used cars dataset". This dataset was created from a web scrapper in the month of September in 2020. This dataset contains 3 Million rows of data with 66 features that pertained to the car and the dealership information.
## Data Processing
### Remove Features
I decided to start my Data Processing by removing any features that we can simply remove that wont affect our target values and that arent relevant to our situation. As a result of individually looking at the descriptions I brought the amount of features from 66 to 22 including the target feature.
![img](/Images/Pros_1.PNG)

### Cleaning Null Values
Now that the amount of features were reduced I want to remove the amount of nulls that are in the dataset. I used a heat map and value counts to show the amount in the dataset.
![img](/Images/pros_2.PNG)
![img](/Images/pros_3.png)

I decided to drop all the rows from the data that were missing values in features where I could not pull information from others features. This included featues such as Frame Damage, trim name, transmission, etc. There were some left over null values but overall the dataset was a lot cleaner and I still had over a millon rows remaining in my dataset.
The values that are left i want to leave for now as i might be able to remove some if some may be in our outliers.
![img](/Images/pros_4.PNG)

### Remove Outliers
Next I want to see how my data is distributed by price, so i selected a few features to plot against my target value price.
![img](/Images/pros_5.PNG)
![img](/Images/pros_6.PNG)
![img](/Images/pros_7.PNG)
![img](/Images/pros_8.PNG)

Based on the previous graphs it is very apparent that price has a lot of outliers in a lot of features. For this model to be as accurate as possible and not allow it to be skewed by these outliers in the high price range. I decided to drop all the rows that had a price value above $90,000. This resulted in removing roughly 5,000 rows. I reploted the previous graphs to compare.
![img](/Images/pros_9.PNG)
![img](/Images/pros_10.PNG)
![img](/Images/pros_11.PNG)
![img](/Images/pros_12.PNG)

The graphs are much cleaner and even on our scatterplot we can see there is a positive correlation. Although we do still have outliers in our data its not out of range with the overall dataset. I also do not want to go to a lower range in price because we do have biodesiel vehicles in our dataset which are typically in this upper price range.
### Remove Under Represented Values
After viewing the unique values count of the values in each feature I discovered that there are some that had very small counts in regards to the overall size of the data. For example the feature City had a very long list of unique values but almost half of the list had less then 100 records. With that being said some cities were being under represented so I decided to filter out values that were under represented in features for City and Make. I removed all values that had a count of 100 or less in City, and removed all the values that had a count less then 30 in Make.

### Replacing values
Now at this point in my project i would like to take care of the null values that I have. For features such as Maximum Seating and horsepower I indexed all the rows that were missing values, I then looked up the most common unique value for that specific feature based on the Model name associated with each row and replaced the null value. I also did a similar strategy for mileage in the exception that instead of using the model name as a reference, I am using the average miles driven based on the year the vehicle was made. I did this because the miles driven on a vehicle typically has a positive correlation with each other. I was able to recover 6,639 values for Maximum Seating, 4,688 rows for Horsepower, and 8,166 rows for Mileage. 
![img](/Images/pros_14.PNG)
I still had 512 rows remaing for seating and 79 for horsepower. At this point I will assume that because I was not able to recover these rows there isnt enough information for these specific vehicles so I decided to remove these rows as the size is negligible compared to the overall amount of rows I have.
![img](/Images/pros_13.PNG)
While I went through the process to remove null values I also used the same strategy to replace values for maximum seating where one unique value was "---". I was able to completly recover 376 rows in this feature. At this point I also discovered that Exterior Color had a unique value called "UNKOWN" in which case I decided to drop these values as it is a feature that we cannot extract from another.
### Impute
Now at this point there are no null values or unkown values in my dataset. Before I split my data for training I must impute these features into numerical values that I can fit onto my model. My ideal attempt to replace binary values using label transformer and replace multicategorical featues using getDummies was not something my current machine was capable of handling. I decided to also use label encoder for Trim Name and City.
## Training Models

## Comparing Models
## Next Steps
