# Cleaning Data

### Dealing with NaN values:
1. Erase the rows with NaN values. Not a good choice because we lose information, especially for small datasets.
2. Replace them. Some ways to do this:
    a. Replace them with specific values, usually 0.<br>Use .describe() to the dataframe to check if zero is a good choice. If the min value equals 0, then it could be a good choice, if not try another one.
    b. Replace them with metrics such as mean or median.
    c. Replace them using MICE or KNN.<br>
    **MICE (Multiple Imputation by Chained Equations):** fits a linear regression with the present values, for every column with missing values.<br>
    **KNN:** very similar to KNeighborsClassifier from sklearn. It finds the closest k samples from dataset to the sample with NaN value, and impute it with it the mean value of these samples.