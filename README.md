# Data Analysis Project
## Dream Housing Finance Company Customer's Data
Data Cleaning\
Data Exploration\
Model Development\
Model Interpretation/Evaluation

* Data Cleaning\
This involved handling missing data. I used KNNImputer to impute the missing values, It works by finding other variables that have high correlation with the missing value variable and use those variables to predict the missing values and them fill them in.

* Data Exploration\
It helped understand the different variables by anayzing them through visuaizations and statistics, the data set contains 12 columns![Screenshot (36)](https://user-images.githubusercontent.com/42872872/141115314-34628d6c-a49f-4c2a-8973-2dd1f28fe992.png)
 The exploration was in two stages; Univariate and Bivariate
    * -In **Univariate** The variables were explored independently, there are two types of variables and we analyze them differently, they are Categorical and Continuous Variables\
         a. **Continuous Variables -** I explored the distibutions of Continuous variables which included the Applicant's's Income, Coapplicant's Income, Loan Amount and Loan Amount Term to find the average, middle value, highest occurence, and skewness, etc.\
         b. **Categorical Variables -** I found the number of occurence of each category of a variable in the entire dataset e.g I explored the Gender Variable by finding the number of males and females in the dataset.
    * -In **Bivariate** I explored the relationship between the different variabes to remove Highy Correlated Independent Variables, and find variables that have much and less correlation with the dependent variable. There are also different ways of exploring Categorical and Continuous variables in bivariate exploration.\

* Model Development\
After the data preparation and exploratory data analysis, I built the model on different algorithms and selected XGBClassifier, I also performed Feature engineering, and hyperparameter optimization with optuna to Improve the accuracy of the model.

* Model Interpretation\
The model is to predict whether a loan applicant will be eligible for a loan, the classifier learns the relationship between the features and the target variable which is the eligibility status, so as to predict eligibility status for new set of loan applicants.
   
