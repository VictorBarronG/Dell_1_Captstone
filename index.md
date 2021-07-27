# Regression Analysis on Predicting Car Price
## Introduction
To complete our training at Talent Path, We must present a capstone project to demonstrate our skills and knowledge that we have been learning for the past few weeks. I have done an indepth analysis on a dataset and created a model that can predict car price at 92% accuracy. My goal for this project is to incorporate the prexisting knowledge that I have of cars and working at a dealership along with my knowledge and skills that I have learning throughout my training.&nbsp;

![img](/Images/intro_three.PNG)

## Objective
My Objective is to create a set of models with the dataset I cleaned to achieve an accuracy score above 70% with a low RMSE Score. I will then select a model and incorporate it into a small full stack aplication.

## Business Value
With this model a dealership or any user may use this to predict current market value of vehicles that may come in as trade ins or can be potentially be bought from an auto auction. By being able to predict the market value of the car the user can make an informed decision to purchase a vehicle at a good value or for a dealership to make a purchase of a vehicle knowing exactly the potential marginal profit it can make.

## Data
I obtained my dataset from kaggle called "US Used cars dataset". This dataset was created from a web scrapper in the month of September in 2020. This dataset contains 3 Million rows of data with 66 features that pertained to the car and the dealership information.
## Data Processing
### Remove Features
I decided to start my Data Processing by removing any features that we can simply remove that wont affect our target values and that arent relevant to our situation. As a result of individually looking at the descriptions I brought the amount of features from 66 to 22 including the target feature. &nbsp;
![img](/Images/Pros_1.PNG)&nbsp;

### Cleaning Null Values
Now that the amount of features were reduced I want to remove the amount of nulls that are in the dataset. I used a heat map and value counts to show the amount in the dataset.&nbsp;
![img](/Images/pros_2.PNG)&nbsp;&nbsp;

![img](/Images/pros_3.png)&nbsp;

I decided to drop all the rows from the data that were missing values in features where I could not pull information from others features. This included featues such as Frame Damage, trim name, transmission, etc. There were some left over null values but overall the dataset was a lot cleaner and I still had over a millon rows remaining in my dataset.
The values that are left i want to leave for now as i might be able to remove some if some may be in our outliers.&nbsp;

![img](/Images/pros_4.PNG)&nbsp;

### Remove Outliers
Next I want to see how my data is distributed by price, so i selected a few features to plot against my target value price.&nbsp;

![img](/Images/pros_5.PNG)&nbsp;

![img](/Images/pros_6.PNG)&nbsp;

![img](/Images/pros_7.PNG)&nbsp;&nbsp;

![img](/Images/pros_8.PNG)&nbsp;

Based on the previous graphs it is very apparent that price has a lot of outliers in a lot of features. For this model to be as accurate as possible and not allow it to be skewed by these outliers in the high price range. I decided to drop all the rows that had a price value above $90,000. This resulted in removing roughly 5,000 rows. I reploted the previous graphs to compare.&nbsp;

![img](/Images/pros_9.PNG)&nbsp;

![img](/Images/pros_10.PNG)&nbsp;

![img](/Images/pros_11.PNG)&nbsp;&nbsp;

![img](/Images/pros_12.PNG)&nbsp;

The graphs are much cleaner and even on our scatterplot we can see there is a positive correlation. Although we do still have outliers in our data its not out of range with the overall dataset. I also do not want to go to a lower range in price because we do have biodesiel vehicles in our dataset which are typically in this upper price range.
### Remove Under Represented Values
After viewing the unique values count of the values in each feature I discovered that there are some that had very small counts in regards to the overall size of the data. For example the feature City had a very long list of unique values but almost half of the list had less then 100 records. With that being said some cities were being under represented so I decided to filter out values that were under represented in features for City and Make. I removed all values that had a count of 100 or less in City, and removed all the values that had a count less then 30 in Make.

### Replacing values
Now at this point in my project i would like to take care of the null values that I have. For features such as Maximum Seating and horsepower I indexed all the rows that were missing values, I then looked up the most common unique value for that specific feature based on the Model name associated with each row and replaced the null value. I also did a similar strategy for mileage in the exception that instead of using the model name as a reference, I am using the average miles driven based on the year the vehicle was made. I did this because the miles driven on a vehicle typically has a positive correlation with each other. I was able to recover 6,639 values for Maximum Seating, 4,688 rows for Horsepower, and 8,166 rows for Mileage.

![img](/Images/pros_14.PNG)&nbsp;

I still had 512 rows remaing for seating and 79 for horsepower. At this point I will assume that because I was not able to recover these rows there isnt enough information for these specific vehicles so I decided to remove these rows as the size is negligible compared to the overall amount of rows I have.

![img](/Images/pros_13.PNG)&nbsp;

While I went through the process to remove null values I also used the same strategy to replace values for maximum seating where one unique value was "---". I was able to completly recover 376 rows in this feature. At this point I also discovered that Exterior Color had a unique value called "UNKOWN" in which case I decided to drop these values as it is a feature that we cannot extract from another.
### Impute
Now at this point there are no null values or unkown values in my dataset. Before I split my data for training I must impute these features into numerical values that I can fit onto my model. My ideal attempt to replace binary values using label Encoder and replace multicategorical featues using getDummies was not something my current machine was capable of handling.Because get dummies seperates each unique value in the feature into its own feature it resulting in having way more features then my machine was capable of processing at a time. I decided to also use label encoder for Trim Name and City. By doing this step I was able to significantly reduce the amount of columns I had and am able to fit onto a model.

![img](/Images/pros_14.PNG)&nbsp;

This previous image is only a small portion of the overall dataframe. At this point I have 1,158,767 Rows of data with 1,137 features.

![img](/Images/pros_15.PNG)&nbsp;

## Training Models
For my Train Test Split I decided to do a 80% Train and a 20% Test split and I set a random state to 42. My first model is MultiLinear Regression Model that resulted in with an accuracy score or roughly 86% for both train and test data. While this is above my goal accuracy I also did two more models before picking one just yet.

![img](/Images/pros_16.PNG)&nbsp;

Gradient Boosting Regressor has given me good results before and so I also decided to create this model. I set the parameters of n_estimators to 400 with a random state of 42.

![img](/Images/pros_17.PNG)&nbsp;

For my Final Model I decided to do a Random Forest Regressor with n_estimators of 300 and a random state of 42. This ultimatley provided me with the highest accuracy but by comparing the train and test accuracy its pretty apparent that the model is overfitted.

![img](/Images/pros_18.PNG)&nbsp;
![img](/Images/pros_19.PNG)&nbsp;

## Comparing Models
## Next Steps
