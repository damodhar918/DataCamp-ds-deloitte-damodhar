---

**Foreword**

Code snippets and excerpts from the tutorial. Python 3. From DataCamp.

---

# Load and explore the Wine dataset

We use the [wine quality dataset](http://archive.ics.uci.edu/ml/datasets/Wine+Quality) related to red and white vinho verde wine samples, from the north of Portugal.


```python
# import the modules
%pylab inline
import pandas as pd
import matplotlib.pyplot as plt

# set the style
plt.style.use('ggplot')
```

    Populating the interactive namespace from numpy and matplotlib



```python
# import the data
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ' , sep = ';')
df.head(3)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fixed acidity</th>
      <th>volatile acidity</th>
      <th>citric acid</th>
      <th>residual sugar</th>
      <th>chlorides</th>
      <th>free sulfur dioxide</th>
      <th>total sulfur dioxide</th>
      <th>density</th>
      <th>pH</th>
      <th>sulphates</th>
      <th>alcohol</th>
      <th>quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.4</td>
      <td>0.70</td>
      <td>0.00</td>
      <td>1.9</td>
      <td>0.076</td>
      <td>11.0</td>
      <td>34.0</td>
      <td>0.9978</td>
      <td>3.51</td>
      <td>0.56</td>
      <td>9.4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.8</td>
      <td>0.88</td>
      <td>0.00</td>
      <td>2.6</td>
      <td>0.098</td>
      <td>25.0</td>
      <td>67.0</td>
      <td>0.9968</td>
      <td>3.20</td>
      <td>0.68</td>
      <td>9.8</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.8</td>
      <td>0.76</td>
      <td>0.04</td>
      <td>2.3</td>
      <td>0.092</td>
      <td>15.0</td>
      <td>54.0</td>
      <td>0.9970</td>
      <td>3.26</td>
      <td>0.65</td>
      <td>9.8</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# drop target variable
# only keep the values; the DataFrame becomes a simple array (matrix)
# index (axis=0 / ‘index’) or columns (axis=1 / ‘columns’).
X = df.drop('quality' , axis=1).values

# print the array
print(X)
```

    [[  7.4     0.7     0.    ...,   3.51    0.56    9.4  ]
     [  7.8     0.88    0.    ...,   3.2     0.68    9.8  ]
     [  7.8     0.76    0.04  ...,   3.26    0.65    9.8  ]
     ..., 
     [  6.3     0.51    0.13  ...,   3.42    0.75   11.   ]
     [  5.9     0.645   0.12  ...,   3.57    0.71   10.2  ]
     [  6.      0.31    0.47  ...,   3.39    0.66   11.   ]]


The last column is gone from the array. Make it a list instead (or a single-row array).


```python
y1 = df['quality'].values

# print the single-row array
print(y1)
```

    [5 5 5 ..., 6 5 6]



```python
# row, col of the DataFrame
df.shape
```




    (1599, 12)




```python
# plot all the columns or variables
pd.DataFrame.hist(df, figsize = [15,15]);

plt.show()
```


![](img/Scaling_Centering_Noise/output_8_0.png)


Notice the range of each variable; some are wider.

Any algorithm, such as k-NN, which cares about the distance between data points. This motivates scaling our data.

Let us turn it into a two-category variable consisting of 'good' (rating > 5) & 'bad' (rating <= 5) qualities.


```python
print(y1)
```

    [5 5 5 ..., 6 5 6]



```python
# is the rating <= 5 ?
y = y1 <= 5
print(y)
```

    [ True  True  True ..., False  True False]


`True` is worth 1 and `False` is worth 0.


```python
# plot two histograms
# the original target variable
# and the aggregated target variable
plt.figure(figsize=(20,5));

# left plot
plt.subplot(1, 2, 1 );
plt.hist(y1);
plt.xlabel('original target value')
plt.ylabel('count')

# right plot
plt.subplot(1, 2, 2);
plt.hist(y)
plt.xlabel('aggregated target value')
plt.show()
```


![](img/Scaling_Centering_Noise/output_13_0.png)


Again, on the right histogram, `True` = 1 and `False` = 0.

# k-Nearest Neighbours

## Measure performance

**Accuracy** is the default scoring method for both

- k-Nearest Neighbours and
- logistic regression.

$$\text{Accuracy}=\frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}}$$

Accuracy is commonly defined for binary classification problems in terms of true positives & false negatives. It can also be defined in terms of a [confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix). 

[Other measures](https://machinelearningmastery.com/classification-accuracy-is-not-enough-more-performance-measures-you-can-use/) of model performance are derived from the confusion matrix: **precision** (true positives divided by the number of true & false positives) and **recall** (number of true positives divided by the number of true positives plus the number of false negatives). 

The **[F1-score](https://en.wikipedia.org/wiki/F1_score)** is the harmonic mean of the precision and the recall.

## Train-test split and performance in practice

The rule of thumb is to use approximately 

- 80% of the data for training (train set) and
- 20% for testing (test set).


```python
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.2, 
                                                    random_state=42)
```


```python
# the k-NN model
from sklearn import neighbors, linear_model

knn = neighbors.KNeighborsClassifier(n_neighbors = 5)
knn_model_1 = knn.fit(X_train, y_train)
```


```python
print('k-NN score for test set: %f' % knn_model_1.score(X_test, y_test))
print('k-NN score for training set: %f' % knn_model_1.score(X_train, y_train))
```

    k-NN score for test set: 0.612500
    k-NN score for training set: 0.774042


The accuracy, more specifically the test accuracy, is not great.

Let us print out all the *other* performance measures for the test set.


```python
from sklearn.metrics import classification_report

y_true, y_pred = y_test, knn_model_1.predict(X_test)
print(classification_report(y_true, y_pred))
```

                 precision    recall  f1-score   support
    
          False       0.66      0.64      0.65       179
           True       0.56      0.57      0.57       141
    
    avg / total       0.61      0.61      0.61       320
    


*Other* performance measures for the train set.


```python
y_true, y_pred = y_train, knn_model_1.predict(X_train)
print(classification_report(y_true, y_pred))
```

                 precision    recall  f1-score   support
    
          False       0.80      0.76      0.78       676
           True       0.75      0.79      0.77       603
    
    avg / total       0.78      0.77      0.77      1279
    


These underperformances might come from the spread in the variables. The range of each variable is different; some are wider.

# Preprocessing: scaling and centering the data

Preprocessing happens before running any model, such as a regression (predicting a continuous variable) or a classification (predicting a discrete variable) using one or another model (k-NN, logistic, decision tree, random forests etc.).

For numerical variables, it is common to either normalize or standardize the data.

**Normalization**: **scaling** a dataset so that its minimum is 0 and its maximum 1.

$$x_{normalized} = \frac{x-x_{min}}{x_{max}-x_{min}}$$

**Stardardization**: **centering** the data around 0 and to scale with respect to the standard deviation.

$$x_{standardized} = \frac{x-\mu}{\sigma}$$ 

where $\mu$ and $\sigma$ are the mean and standard deviation of the dataset.

There are other transformatoions, such as the log transformation or the Box-Cox transformation, to make the data look more Gaussian or a normally distributed.

# k-NN: scaling in practice

## Scale the data


```python
print(X)
```

    [[  7.4     0.7     0.    ...,   3.51    0.56    9.4  ]
     [  7.8     0.88    0.    ...,   3.2     0.68    9.8  ]
     [  7.8     0.76    0.04  ...,   3.26    0.65    9.8  ]
     ..., 
     [  6.3     0.51    0.13  ...,   3.42    0.75   11.   ]
     [  5.9     0.645   0.12  ...,   3.57    0.71   10.2  ]
     [  6.      0.31    0.47  ...,   3.39    0.66   11.   ]]



```python
from sklearn.preprocessing import scale

# minimum is 0 and its maximum 1
Xs = scale(X)
print(Xs)
```

    [[-0.52835961  0.96187667 -1.39147228 ...,  1.28864292 -0.57920652
      -0.96024611]
     [-0.29854743  1.96744245 -1.39147228 ..., -0.7199333   0.1289504
      -0.58477711]
     [-0.29854743  1.29706527 -1.18607043 ..., -0.33117661 -0.04808883
      -0.58477711]
     ..., 
     [-1.1603431  -0.09955388 -0.72391627 ...,  0.70550789  0.54204194
       0.54162988]
     [-1.39015528  0.65462046 -0.77526673 ...,  1.6773996   0.30598963
      -0.20930812]
     [-1.33270223 -1.21684919  1.02199944 ...,  0.51112954  0.01092425
       0.54162988]]


## Run the k-NN


```python
from sklearn.cross_validation import train_test_split

# split
# 80% of the data for training (train set)
# 20% for testing (test set)
Xs_train, Xs_test, y_train, y_test = train_test_split(Xs,
                                                      y,
                                                      test_size=0.2,
                                                      random_state=42)
```


```python
# Run
knn_model_2 = knn.fit(Xs_train, y_train)
```

## Measure the performance


```python
print('k-NN score for test set: %f' % knn_model_2.score(Xs_test, y_test))
print('k-NN score for training set: %f' % knn_model_2.score(Xs_train, y_train))
```

    k-NN score for test set: 0.712500
    k-NN score for training set: 0.814699



```python
y_true, y_pred = y_test, knn_model_2.predict(Xs_test)

# Test set
print(classification_report(y_true, y_pred))
```

                 precision    recall  f1-score   support
    
          False       0.72      0.79      0.75       179
           True       0.70      0.62      0.65       141
    
    avg / total       0.71      0.71      0.71       320
    



```python
y_true, y_pred = y_train, knn_model_2.predict(Xs_train)

# Train set
print(classification_report(y_true, y_pred))
```

                 precision    recall  f1-score   support
    
          False       0.80      0.86      0.83       676
           True       0.83      0.77      0.80       603
    
    avg / total       0.82      0.81      0.81      1279
    


Normalization-scaling improves the performance compare to the previous `classification_report`.

# k-NN Recap

## Without scaling


```python
# Set sc = False 
# Do not scale the features 
sc = False
# Set the number of k in k-NN
nk = 5

# Load data 
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ' , sep = ';') 
# Drop target variable 
X = df.drop('quality' , 1).values

# Scale, if desired 
if sc == True: 
  X = scale(X) 
  
# Target value 
y1 = df['quality'].values # original target variable 
# New target variable: is the rating <= 5?
y = y1 <= 5 

# Split (80/20) the data into a test set and a train set
# X_train, X_test, y_train, y_test 
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42) 

# Train the k-NN model
knn = neighbors.KNeighborsClassifier(n_neighbors = nk)
knn_model = knn.fit(X_train, y_train)

# Print performance on the test set 
print('k-NN accuracy for test set: %f' % knn_model.score(X_test, y_test))
y_true, y_pred = y_test, knn_model.predict(X_test) 
print(classification_report(y_true, y_pred))
```

    k-NN accuracy for test set: 0.612500
                 precision    recall  f1-score   support
    
          False       0.66      0.64      0.65       179
           True       0.56      0.57      0.57       141
    
    avg / total       0.61      0.61      0.61       320
    


## With scaling


```python
# Set sc = True 
# to scale the features 
sc = True
# Set the number of k in k-NN
nk = 5

# Load data 
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ' , sep = ';') 
# Drop target variable 
X = df.drop('quality' , 1).values

# Scale, if desired 
if sc == True: 
  X = scale(X) 
  
# Target value 
y1 = df['quality'].values # original target variable 
# New target variable: is the rating <= 5?
y = y1 <= 5 

# Split (80/20) the data into a test set and a train set
# X_train, X_test, y_train, y_test 
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42) 

# Train the k-NN model
knn = neighbors.KNeighborsClassifier(n_neighbors = nk)
knn_model = knn.fit(X_train, y_train)

# Print performance on the test set 
print('k-NN accuracy for test set: %f' % knn_model.score(X_test, y_test))
y_true, y_pred = y_test, knn_model.predict(X_test) 
print(classification_report(y_true, y_pred))
```

    k-NN accuracy for test set: 0.712500
                 precision    recall  f1-score   support
    
          False       0.72      0.79      0.75       179
           True       0.70      0.62      0.65       141
    
    avg / total       0.71      0.71      0.71       320
    


# Linear regression

Before addressing an alternative to k-NN, the logistic regression or Logit, let us briefly review the linear regresion with a different dataset.


```python
# Import necessary packages
%pylab inline
import pandas as pd
import matplotlib.pyplot as plt

# set the style
plt.style.use('ggplot')

# Import nmore packages
from sklearn import datasets
from sklearn import linear_model
import numpy as np
```

    Populating the interactive namespace from numpy and matplotlib



```python
# Load the data
# The data is part of the scikit-learn module
boston = datasets.load_boston()
yb = boston.target.reshape(-1, 1)
Xb = boston['data'][:,5].reshape(-1, 1)

print(yb[:10])
```

    [[ 24. ]
     [ 21.6]
     [ 34.7]
     [ 33.4]
     [ 36.2]
     [ 28.7]
     [ 22.9]
     [ 27.1]
     [ 16.5]
     [ 18.9]]



```python
print(Xb[:10])
```

    [[ 6.575]
     [ 6.421]
     [ 7.185]
     [ 6.998]
     [ 7.147]
     [ 6.43 ]
     [ 6.012]
     [ 6.172]
     [ 5.631]
     [ 6.004]]



```python
# Plot data
plt.scatter(Xb,yb)
plt.ylabel('value of house /1000 ($)')
plt.xlabel('number of rooms')
```




    <matplotlib.text.Text at 0x7f3681ae90b8>




![](img/Scaling_Centering_Noise/output_40_1.png)



```python
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit( Xb, yb)
```




    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)




```python
# Plot outputs
plt.scatter(Xb, yb,  color='black')
plt.plot(Xb, regr.predict(Xb), color='blue',
         linewidth=3)
plt.show()
```


![](img/Scaling_Centering_Noise/output_42_0.png)


# Logistic regression (Logit)

## With random numbers


```python
# Synthesize data
X1 = np.random.normal(size=150)
y1 = (X1 > 0).astype(np.float)
X1[X1 > 0] *= 4
X1 += .3 * np.random.normal(size=150)
X1 = X1.reshape(-1, 1)
```


```python
# Run the classifier
clf = linear_model.LogisticRegression()
clf.fit(X1, y1)
```




    LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
              intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
              penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
              verbose=0, warm_start=False)




```python
X1[:10]
```




    array([[-0.74466839],
           [ 0.47335714],
           [-1.94951938],
           [ 0.12078443],
           [-1.62121705],
           [-2.23684396],
           [ 7.66984914],
           [-0.31941781],
           [-1.07205326],
           [ 0.85413978]])




```python
# Order X1
X1_ordered = sorted(X1, reverse=False)

X1_ordered[:10]
```




    [array([-3.29826361]),
     array([-2.76292445]),
     array([-2.23684396]),
     array([-1.96629089]),
     array([-1.94951938]),
     array([-1.87501025]),
     array([-1.83321548]),
     array([-1.73611093]),
     array([-1.62121705]),
     array([-1.61885181])]




```python
# Plot the result
plt.scatter(X1.ravel(), y1, color='black', zorder=20 , alpha = 0.5)
plt.plot(X1_ordered, clf.predict_proba(X1_ordered)[:,1], color='blue' , linewidth = 3)
plt.ylabel('target variable')
plt.xlabel('predictor variable')
plt.show()
```


![](img/Scaling_Centering_Noise/output_48_0.png)


## With the Wine dataset


```python
# Load data
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ' , sep = ';')

df.head(3)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fixed acidity</th>
      <th>volatile acidity</th>
      <th>citric acid</th>
      <th>residual sugar</th>
      <th>chlorides</th>
      <th>free sulfur dioxide</th>
      <th>total sulfur dioxide</th>
      <th>density</th>
      <th>pH</th>
      <th>sulphates</th>
      <th>alcohol</th>
      <th>quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.4</td>
      <td>0.70</td>
      <td>0.00</td>
      <td>1.9</td>
      <td>0.076</td>
      <td>11.0</td>
      <td>34.0</td>
      <td>0.9978</td>
      <td>3.51</td>
      <td>0.56</td>
      <td>9.4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.8</td>
      <td>0.88</td>
      <td>0.00</td>
      <td>2.6</td>
      <td>0.098</td>
      <td>25.0</td>
      <td>67.0</td>
      <td>0.9968</td>
      <td>3.20</td>
      <td>0.68</td>
      <td>9.8</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.8</td>
      <td>0.76</td>
      <td>0.04</td>
      <td>2.3</td>
      <td>0.092</td>
      <td>15.0</td>
      <td>54.0</td>
      <td>0.9970</td>
      <td>3.26</td>
      <td>0.65</td>
      <td>9.8</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Drop target variable
X = df.drop('quality' , 1).values

# Print the array
print(X)
```

    [[  7.4     0.7     0.    ...,   3.51    0.56    9.4  ]
     [  7.8     0.88    0.    ...,   3.2     0.68    9.8  ]
     [  7.8     0.76    0.04  ...,   3.26    0.65    9.8  ]
     ..., 
     [  6.3     0.51    0.13  ...,   3.42    0.75   11.   ]
     [  5.9     0.645   0.12  ...,   3.57    0.71   10.2  ]
     [  6.      0.31    0.47  ...,   3.39    0.66   11.   ]]


The last column is gone.


```python
y1 = df['quality'].values

# Print the single-row array
print(y1)
```

    [5 5 5 ..., 6 5 6]



```python
df.shape
```




    (1599, 12)




```python
# plot the other columns or variables
pd.DataFrame.hist(df, figsize = [15,15]);

plt.show() # facultative in Jypyter
```


![](img/Scaling_Centering_Noise/output_55_0.png)


Let us turn it into a two-category variable consisting of 'good' (rating > 5) & 'bad' (rating <= 5) qualities.


```python
# is the rating <= 5 ?
y = y1 <= 5
print(y)
```

    [ True  True  True ..., False  True False]



```python
from sklearn.cross_validation import train_test_split

# split
# 80% of the data for training (train set)
# 20% for testing (test set)
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)
```


```python
from sklearn import linear_model

# Initial logistic regression model
lr = linear_model.LogisticRegression()
```


```python
# Fit the model
lr = lr.fit(X_train, y_train)
y_true, y_pred = y_train, lr.predict(X_train)

# Evaluate the train set
print('Logistic Regression score for train set: %f' % lr.score(X_train, y_train))
```

    Logistic Regression score for train set: 0.752932



```python
print(classification_report(y_true, y_pred))
```

                 precision    recall  f1-score   support
    
          False       0.77      0.75      0.76       676
           True       0.73      0.75      0.74       603
    
    avg / total       0.75      0.75      0.75      1279
    



```python
from sklearn.metrics import classification_report

# Use the test set
y_true, y_pred = y_test, lr.predict(X_test)

# Evaluate the test set
print('Logistic Regression score for test set: %f' % lr.score(X_test, y_test))
```

    Logistic Regression score for test set: 0.740625



```python
print(classification_report(y_true, y_pred))
```

                 precision    recall  f1-score   support
    
          False       0.78      0.74      0.76       179
           True       0.69      0.74      0.71       141
    
    avg / total       0.74      0.74      0.74       320
    


**Note**: the logistic regression performs better than k-NN without scaling.

## Scale the data


```python
print(X)
```

    [[  7.4     0.7     0.    ...,   3.51    0.56    9.4  ]
     [  7.8     0.88    0.    ...,   3.2     0.68    9.8  ]
     [  7.8     0.76    0.04  ...,   3.26    0.65    9.8  ]
     ..., 
     [  6.3     0.51    0.13  ...,   3.42    0.75   11.   ]
     [  5.9     0.645   0.12  ...,   3.57    0.71   10.2  ]
     [  6.      0.31    0.47  ...,   3.39    0.66   11.   ]]



```python
from sklearn.preprocessing import scale

Xs = scale(X)
print(Xs)
```

    [[-0.52835961  0.96187667 -1.39147228 ...,  1.28864292 -0.57920652
      -0.96024611]
     [-0.29854743  1.96744245 -1.39147228 ..., -0.7199333   0.1289504
      -0.58477711]
     [-0.29854743  1.29706527 -1.18607043 ..., -0.33117661 -0.04808883
      -0.58477711]
     ..., 
     [-1.1603431  -0.09955388 -0.72391627 ...,  0.70550789  0.54204194
       0.54162988]
     [-1.39015528  0.65462046 -0.77526673 ...,  1.6773996   0.30598963
      -0.20930812]
     [-1.33270223 -1.21684919  1.02199944 ...,  0.51112954  0.01092425
       0.54162988]]


## Run the Logit and measure the performance


```python
from sklearn.cross_validation import train_test_split

# Split 80/20
Xs_train, Xs_test, y_train, y_test = train_test_split(Xs,
                                                      y,
                                                      test_size=0.2,
                                                      random_state=42)
```


```python
# Run the logistic regression model
lr_2 = lr.fit(Xs_train, y_train)
```


```python
# Fit the model
y_true, y_pred = y_train, lr_2.predict(Xs_train)

# Evaluate the train set
print('Logistic Regression score for train set: %f' % lr_2.score(Xs_train, y_train))
```

    Logistic Regression score for train set: 0.752150



```python
print(classification_report(y_true, y_pred))
```

                 precision    recall  f1-score   support
    
          False       0.77      0.76      0.76       676
           True       0.73      0.75      0.74       603
    
    avg / total       0.75      0.75      0.75      1279
    



```python
# Use the test set
y_true, y_pred = y_test, lr_2.predict(Xs_test)

# Evaluate the test set
print('Logistic Regression score for test set: %f' % lr_2.score(Xs_test, y_test))
```

    Logistic Regression score for test set: 0.740625



```python
print(classification_report(y_true, y_pred))
```

                 precision    recall  f1-score   support
    
          False       0.79      0.74      0.76       179
           True       0.69      0.74      0.72       141
    
    avg / total       0.74      0.74      0.74       320
    


This is very interesting! The performance of logistic regression did not improve with data scaling.

Predictor variables with large ranges that do not effect the target variable, a regression algorithm will make the corresponding coefficients small so that they do not effect predictions so much.

# Logit Recap

## Without scaling


```python
# Set sc = False
# do not scale the features 
sc = False 

# Load the data 
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ' , sep = ';') 
X = df.drop('quality' , 1).values # drop target variable 

# Scale, if desired 
if sc == True: 
  X = scale(X) 
  
# Target value 
y1 = df['quality'].values # original target variable 
y = y1 <= 5  # new target variable: is the rating <= 5? 

# Split (80/20) the data into a test set and a train
# X_train, X_test, y_train, y_test
train_test_split(X, y, test_size=0.2, random_state=42) 

# Train logistic regression model 
lr = linear_model.LogisticRegression() 
lr = lr.fit(X_train, y_train) 

# Print performance on the test set
print('Logistic Regression score for training set: %f' % lr.score(X_train, y_train)) 
y_true, y_pred = y_test, lr.predict(X_test) 
print(classification_report(y_true, y_pred))
```

    Logistic Regression score for training set: 0.752932
                 precision    recall  f1-score   support
    
          False       0.78      0.74      0.76       179
           True       0.69      0.74      0.71       141
    
    avg / total       0.74      0.74      0.74       320
    


# Noise and scaling

The noisier the symthesized data, the more important scaling will be.

Measurements can be in meters and and miles, with small or large ranges. If we scale the data, they end up being the same.

scikit-learn’s `make_blobs` function to generate 2000 data points that are in 4 clusters (each data point has 2 predictor variables and 1 target variable).


```python
%pylab inline
```

    Populating the interactive namespace from numpy and matplotlib



```python
# Generate some clustered data (blobs!)
import numpy as np
from sklearn.datasets.samples_generator import make_blobs

n_samples=2000
X, y = make_blobs(n_samples, centers=4, n_features=2, random_state=0)

print(X)
```

    [[-0.46530384  1.73299482]
     [-0.33963733  3.84220272]
     [ 2.25309569  0.99541446]
     ..., 
     [ 1.03616476  4.09126428]
     [-0.5901088   3.68821314]
     [ 2.30405277  4.20250584]]



```python
print(y)
```

    [2 0 1 ..., 0 2 0]


## Plotting the synthesized data

Each axis is a predictor variable and the colour is a key to the target variable

All possible target variables are equally represented. In this case (or even if they are approximately equally represented), we say that the class y is balanced.


```python
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.figure(figsize=(20,5));
plt.subplot(1, 2, 1 );
plt.scatter(X[:,0] , X[:,1],  c = y, alpha = 0.7);
plt.subplot(1, 2, 2);
plt.hist(y)

plt.show()
```


![](img/Scaling_Centering_Noise/output_81_0.png)


Plot histograms of the features.


```python
import pandas as pd

# Convert to a DataFrame
df = pd.DataFrame(X)

# Plot it
pd.DataFrame.hist(df, figsize=(20,5))
```




    array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f366d3dbba8>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f366d30ca58>]], dtype=object)




![](img/Scaling_Centering_Noise/output_83_1.png)


Split into test & train sets, and plot both sets (train set > test set; 80/20).


```python
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)
```


```python
plt.figure(figsize=(20,5));
plt.subplot(1, 2, 1 );
plt.title('training set')
plt.scatter(X_train[:,0] , X_train[:,1],  c = y_train, alpha = 0.7);
plt.subplot(1, 2, 2);
plt.scatter(X_test[:,0] , X_test[:,1],  c = y_test, alpha = 0.7);
plt.title('test set')

plt.show()
```


![](img/Scaling_Centering_Noise/output_86_0.png)


## k-Nearest Neighbours

Let’s instantiate a k-Nearest Neighbours classifier and train it on our train set.


```python
from sklearn import neighbors, linear_model

knn = neighbors.KNeighborsClassifier()
knn_model = knn.fit(X_train, y_train)
```

Fit the `knn_model` to the test set and compute the accuracy.


```python
knn_model.score(X_test, y_test)
```




    0.93500000000000005




```python
print('k-NN score for test set: %f' % knn_model.score(X_test, y_test))
```

    k-NN score for test set: 0.935000


Check out a variety of other metrics.


```python
from sklearn.metrics import classification_report

y_true, y_pred = y_test, knn_model.predict(X_test)
print(classification_report(y_true, y_pred))
```

                 precision    recall  f1-score   support
    
              0       0.87      0.90      0.88       106
              1       0.98      0.93      0.95       102
              2       0.90      0.92      0.91       100
              3       1.00      1.00      1.00        92
    
    avg / total       0.94      0.94      0.94       400
    


Re-fit `knn_model` to the train set and compute the accuracy.


```python
print('k-NN score for train set: %f' % knn_model.score(X_train, y_train))
```

    k-NN score for train set: 0.941875



```python
from sklearn.metrics import classification_report

y_true, y_pred = y_train, knn_model.predict(X_train)
print(classification_report(y_true, y_pred))
```

                 precision    recall  f1-score   support
    
              0       0.88      0.90      0.89       394
              1       0.97      0.96      0.96       398
              2       0.94      0.93      0.93       400
              3       0.99      0.98      0.98       408
    
    avg / total       0.94      0.94      0.94      1600
    


### Scale the data, run the k-NN, and measure the performance


```python
print(X)
```

    [[-0.46530384  1.73299482]
     [-0.33963733  3.84220272]
     [ 2.25309569  0.99541446]
     ..., 
     [ 1.03616476  4.09126428]
     [-0.5901088   3.68821314]
     [ 2.30405277  4.20250584]]



```python
from sklearn.preprocessing import scale

Xs = scale(X)
print(Xs)
```

    [[-0.26508542 -0.82638395]
     [-0.19594894 -0.0519305 ]
     [ 1.23046484 -1.09720678]
     ..., 
     [ 0.5609601   0.03951927]
     [-0.33374791 -0.10847199]
     [ 1.25849931  0.08036466]]



```python
from sklearn.cross_validation import train_test_split

Xs_train, Xs_test, y_train, y_test = train_test_split(Xs,
                                                      y,
                                                      test_size=0.2,
                                                      random_state=42)
```


```python
plt.figure(figsize=(20,5));

plt.subplot(1, 2, 1 );
plt.scatter(Xs_train[:,0] , Xs_train[:,1],  c = y_train, alpha = 0.7);
plt.title('scaled training set')

plt.subplot(1, 2, 2);
plt.scatter(Xs_test[:,0] , Xs_test[:,1],  c = y_test, alpha = 0.7);
plt.title('scaled test set')

plt.show()
```


![](img/Scaling_Centering_Noise/output_101_0.png)



```python
knn_model_s = knn.fit(Xs_train, y_train)

print('k-NN score for test set: %f' % knn_model_s.score(Xs_test, y_test))
```

    k-NN score for test set: 0.935000


It doesn’t perform any better with scaling.

This is most likely because both features were already around the same range.

### Add noise to the signal

Adding a third variable of Gaussian noise with mean 0 and variable standard deviation $\sigma$. We call $\sigma$ the strength of the noise and we see that the stronger the noise, the worse the performance of k-Nearest Neighbours.


```python
# Strength of noise term
ns = 10**(3)

# Add noise column to predictor variables
newcol = np.transpose([ns*np.random.randn(n_samples)])
Xn = np.concatenate((X, newcol), axis = 1)

print(Xn)
```

    [[ -4.65303843e-01   1.73299482e+00  -9.41949646e+01]
     [ -3.39637332e-01   3.84220272e+00  -1.00446506e+03]
     [  2.25309569e+00   9.95414462e-01   2.95697211e+02]
     ..., 
     [  1.03616476e+00   4.09126428e+00  -1.16020635e+02]
     [ -5.90108797e-01   3.68821314e+00   5.60244701e+02]
     [  2.30405277e+00   4.20250584e+00  -8.97600798e+02]]


Plot the 3D data.


```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111, projection='3d' , alpha = 0.5)
ax.scatter(Xn[:,0], Xn[:,1], Xn[:,2], c = y)
```




    <mpl_toolkits.mplot3d.art3d.Path3DCollection at 0x7f366d409cf8>




![](img/Scaling_Centering_Noise/output_106_1.png)


### Run the k-NN and measure the performance


```python
# Split into train-test sets
Xn_train, Xn_test, y_train, y_test = train_test_split(Xn,
                                                      y, 
                                                      test_size=0.2, 
                                                      random_state=42)
```


```python
# Run the model
knn = neighbors.KNeighborsClassifier()
knn_model = knn.fit(Xn_train, y_train)
```


```python
# Evaluate
print('k-NN score for test set: %f' % knn_model.score(Xn_test, y_test))
```

    k-NN score for test set: 0.337500


Horrible!

### Scale the data, add noise, run the k-NN, and measure the performance


```python
# Scale
Xns = scale(Xn)

print(Xns)
```

    [[-0.26508542 -0.82638395 -0.07164275]
     [-0.19594894 -0.0519305  -0.98584539]
     [ 1.23046484 -1.09720678  0.31993383]
     ..., 
     [ 0.5609601   0.03951927 -0.09356271]
     [-0.33374791 -0.10847199  0.58562421]
     [ 1.25849931  0.08036466 -0.87851945]]



```python
# Apply noise
s = int(.2*n_samples)
Xns_train = Xns[s:]
y_train = y[s:]
Xns_test = Xns[:s]
y_test = y[:s]

# Run the model
knn = neighbors.KNeighborsClassifier()
knn_models = knn.fit(Xns_train, y_train)

# Evaluate
print('k-NN score for test set: %f' % knn_models.score(Xns_test, y_test))
```

    k-NN score for test set: 0.917500


After scaling the data, the model performs nearly as well as were there no noise introduced.

## Noise strength vs. accuracy (and the need for scaling)

How the noise strength can effect model accuracy?

Create a function to split the data and run the model. 

Use the function in a loop.


```python
def accu( X, y):
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=42)
    
    knn = neighbors.KNeighborsClassifier()
    knn_model = knn.fit(X_train, y_train)
    
    return(knn_model.score(X_test, y_test))
```


```python
# Set the variables
noise = [10**i for i in np.arange(0,6)]
A1 = np.zeros(len(noise))
A2 = np.zeros(len(noise))
count = 0
```


```python
print(noise)
```

    [1, 10, 100, 1000, 10000, 100000]



```python
print(A1)
print(A2)
```

    [ 0.  0.  0.  0.  0.  0.]
    [ 0.  0.  0.  0.  0.  0.]



```python
# Run the loop
for ns in noise:
    newcol = np.transpose([ns*np.random.randn(n_samples)])
    Xn = np.concatenate((X, newcol), axis = 1)
    Xns = scale(Xn)
    A1[count] = accu( Xn, y)
    A2[count] = accu( Xns, y)
    count += 1
```


```python
# Plot the results
plt.scatter( noise, A1 )
plt.plot( noise, A1, label = 'unscaled', linewidth = 2)
plt.scatter( noise, A2 , c = 'r')
plt.plot( noise, A2 , label = 'scaled', linewidth = 2)
plt.xscale('log')
plt.xlabel('Noise strength')
plt.ylabel('Accuracy')
plt.legend(loc=3);
```


![](img/Scaling_Centering_Noise/output_120_0.png)



```python
print(A1)
print(A2)
```

    [ 0.9225  0.9175  0.8025  0.3275  0.22    0.2525]
    [ 0.91    0.9175  0.9325  0.9075  0.9325  0.92  ]


The more noise there is in the nuisance variable, the more important it is to scale the data for the k-NN model.

> More noise, more scaling.

## Logit (Repeat the k-NN procedure)


```python
# Change the exponent of 10 to alter the amount of noise
ns = 10**(3) # Strength of noise term

# Set sc = True if we want to scale the features
sc = True
```


```python
# Import packages
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import neighbors, linear_model
from sklearn.preprocessing import scale
from sklearn.datasets.samples_generator import make_blobs
```


```python
# Generate some data
n_samples=2000
X, y = make_blobs(n_samples, 
                  centers=4, 
                  n_features=2,
                  random_state=0)
```


```python
# Add noise column to predictor variables
newcol = np.transpose([ns*np.random.randn(n_samples)])
Xn = np.concatenate((X, newcol), axis = 1)
```


```python
# Scale if desired
if sc == True:
    Xn = scale(Xn)
```


```python
# Train model and test after splitting
Xn_train, Xn_test, y_train, y_test = train_test_split(Xn, y, test_size=0.2, random_state=42)
lr = linear_model.LogisticRegression()
lr_model = lr.fit(Xn_train, y_train)
print('logistic regression score for test set: %f' % lr_model.score(Xn_test, y_test))
```

    logistic regression score for test set: 0.942500

