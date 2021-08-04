# Regression Analysis on Predicting Car Price
## Introduction
To complete our training at Talent Path, We must present a capstone project to demonstrate the skills and knowledge that we have been learning for the past few weeks. I have done an in-depth analysis of a dataset and created a model that can predict car prices at 92% accuracy. My goal for this project is to incorporate the preexisting knowledge that I have of cars and working at a dealership along with the knowledge and skills that I have learned throughout my training.&nbsp;

![img](/Images/intro_three.PNG)

## Objective
My Objective is to create a set of models with the dataset I cleaned to achieve an accuracy score above 70% with a low RMSE Score. I will then select a model and incorporate it into a small full-stack application.

## Business Value
With this model, a dealership or any user may use this to predict the current market value of vehicles that may come in as trade-ins or can be potentially be bought from an auto auction. By being able to predict the market value of the car the user can make an informed decision to purchase a vehicle at a good value or for a dealership to purchase a vehicle knowing exactly the potential marginal profit it can make.

## Data
I obtained my dataset from Kaggle called "US Used cars dataset". This dataset was created from a web scrapper in September 2020. This dataset contains 3 million rows of data with 66 features that pertained to the car and the dealership information.
## Data Processing
### Remove Features
I decided to start my Data Processing by removing any features that we can simply remove that won't affect our target values and that aren't relevant to our situation. As a result of individually looking at the descriptions, I brought the number of features from 66 to 22 including the target feature. &nbsp;
![img](/Images/Pros_1.PNG)&nbsp;

### Cleaning Null Values
Now that the number of features was reduced I want to remove the number of nulls that are in the dataset. I used a heat map and value counts to show the amount in the dataset.&nbsp;
![img](/Images/pros_2.PNG)&nbsp;&nbsp;

![img](/Images/pros_3.png)&nbsp;

I decided to drop all the rows from the data that were missing values in features where I could not pull information from other features. This included features such as Frame Damage, trim name, transmission, etc. There were some leftover null values but overall the dataset was a lot cleaner and I still had over a million rows remaining in my dataset.
The values that are left I want to leave for now as I might be able to remove some if some may be in our outliers.&nbsp;

![img](/Images/pros_4.PNG)&nbsp;

### Remove Outliers
Next, I want to see how my data is distributed by price, so I selected a few features to plot against my target value price.&nbsp;

![img](/Images/pros_5.PNG)&nbsp;

![img](/Images/pros_6.PNG)&nbsp;

![img](/Images/pros_7.PNG)&nbsp;&nbsp;

![img](/Images/pros_8.PNG)&nbsp;

Based on the previous graphs it is very apparent that price has a lot of outliers in a lot of features. For this model to be as accurate as possible and not allow it to be skewed by these outliers in the high price range. I decided to drop all the rows that had a price value above $90,000. This resulted in removing roughly 5,000 rows. I replotted the previous graphs to compare.&nbsp;

![img](/Images/pros_9.PNG)&nbsp;

![img](/Images/pros_10.PNG)&nbsp;

![img](/Images/pros_11.PNG)&nbsp;&nbsp;

![img](/Images/pros_12.PNG)&nbsp;

The graphs are much cleaner and even on our scatterplot, we can see there is a positive correlation. Although we do still have outliers in our data it's not out of range with the overall dataset. I also do not want to go to a lower range in price because we do have biodiesel vehicles in our dataset which are typically in this upper price range.
### Remove Under-Represented Values
After viewing the count of the unique values of the values in each feature I discovered that some had very small counts in regards to the overall size of the data. For example, the feature City had a very long list of unique values but almost half of the list had less than 100 records. With that being said some cities were being underrepresented so I decided to filter out values that were underrepresented in features for City and Make. I removed all values that had a count of 100 or less in City and removed all the values that had a count less than 30 in Make.

### Replacing values
Now at this point in my project, I would like to take care of the null values that I have. For features such as Maximum Seating and horsepower, I indexed all the rows that were missing values, I then looked up the most common unique value for that specific feature based on the Model name associated with each row and replaced the null value. I also did a similar strategy for mileage in the exception that instead of using the model name as a reference, I am using the average miles driven based on the year the vehicle was made. I did this because the miles are driven on a vehicle typically have a positive correlation with each other. I was able to recover 6,639 values for Maximum Seating, 4,688 rows for Horsepower, and 8,166 rows for Mileage.

![img](/Images/pros_14.PNG) ![img](/Images/pros_13.PNG)

I still had 512 rows remaining for seating and 79 for horsepower. At this point, I will assume that because I was not able to recover these rows there isn't enough information for these specific vehicles so I decided to remove these rows as the size is negligible compared to the overall amount of rows I have.

While I went through the process to remove null values I also used the same strategy to replace values for maximum seating where one unique value was "---". I was able to completely recover 376 rows in this feature. At this point, I also discovered that Exterior Color had a unique value called "UNKOWN" in which case I decided to drop these values as it is a feature that we cannot extract from another.

### Impute
Now at this point, there are no null values or unknown values in my dataset. Before I split my data for training I must impute these features into numerical values that I can fit onto my model. My ideal attempt to replace binary values using label Encoder and replace multi categorical features using getDummies was not something my current machine was capable of handling. Because get dummies separates each unique value in the feature into its own feature it resulting in having way more features than my machine was capable of processing at a time. I decided to also use Label Encoder for Trim Name and City. By doing this step I was able to significantly reduce the number of columns I had and can fit onto a model.

![img](/Images/pros_25.PNG) ![img](/Images/pros_15.PNG)

This previous image is only a small portion of the overall data frame. At this point, I have 1,158,767 Rows of data with 1,137 features.

## Training Models
For my Train Test Split, I decided to do an 80% Train and a 20% Test split and I set a random state to 42. My first model is MultiLinear Regression Model that resulted in an accuracy score of roughly 86% for both train and test data. While this is above my goal accuracy I also did two more models before picking one just yet.

![img](/Images/pros_16.PNG)&nbsp;

Gradient Boosting Regressor has given me good results before and so I also decided to create this model. I set the parameters of n_estimators to 400 with a random state of 42.

![img](/Images/pros_17.PNG)&nbsp;

For my Final Model, I decided to do a Random Forest Regressor with n_estimators of 300 and a random state of 42. This ultimately provided me with the highest accuracy but by comparing the train and test accuracy it's pretty apparent that the model is overfitted.

![img](/Images/pros_18.PNG)&nbsp;
![img](/Images/pros_19.PNG)&nbsp;

## Comparing Models
For me to decide my candidate model I had two major factors for my decision. One is that I want a high accuracy but I do not want to sacrifice Overfitting as I want my model to be as accurate and consistent with its answers. And my second deciding factor is the RMSE score. RMSE or Root Mean Square Error is the measure of residual values in terms of my target measure which in my case is money. I am using this measure because RMSE is rigorous on residuals and is usually used when residual values are lower.

![img](/Images/pros_20.PNG)&nbsp;

![img](/Images/pros_21.PNG)&nbsp;

![img](/Images/pros_22.PNG)&nbsp;

![img](/Images/pros_23.PNG)&nbsp;

![img](/Images/pros_24.PNG)&nbsp;
## Conclusion
In conclusion, I have selected the Gradient Boosting Regressor as my candidate model as it provided me both high and consistent Accuracy throughout both train and test data as well as provide a low RMSE score compared to MLR. My Random Forest Regressor received a slightly higher accuracy but it was overfitted so results from this model may be inconsistent.
## Deployment
I integrated my candidate model to a flask application and successfully upload it to docker hub linked [here](https://hub.docker.com/r/vbarron/capstone) and I also deployed it to aws that will be linked [here](http://18.234.156.71:5000/).
## Next Steps
My next steps for this project will be to build my own web scrapper. I believe if I can obtain data from more sites and update my models regularly I will be able to consistently provide a good working model for any user to use. I would also like to impute my dataset like I originally planned if resources are available.
