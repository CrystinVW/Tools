## DPP module: Data Preprocessing Module
#########################################
# coding: utf-8

# In[1]:


#Required import statements
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Associated function to preprocess a dataFile
def dataPreprocess(dataFile, 
                   featureColumns=[], #default = all but last 
                   targetColumns=[], #deault = last
                   doLabelEncodeTargetColumns=False,
                   missingValueCheckColumns=[], #default: none
                   missingValueStrategy='mean', #default: mean
                   encodingColumns=[], #none
                   encodingColumns_with_oneHot=[], #for_oneHot
                   testSize = 0.2,
                   randomState=12345,
                   scalingColumns=[], #default: all but last
                   typeOfScaling='standardization', #minmax
                   dont_splitdata = False
                   
                  ):
    dataset = pd.read_csv(dataFile)
    
    #featureColumns
    if not featureColumns: #default, then all but last one belong to feature set
        X = dataset.iloc[:,:-1].values  #:-1 -> all columns except the last column
    else:
        X = dataset.iloc[:,featureColumns].values
        
    #targetColumns
    if not targetColumns: #default, then last one is the target feature
        y = dataset.iloc[:,-1].values  # -1 = is the index of the last column
    else:
        y = dataset.iloc[:,targetColumns].values
        
    #check for missing values
    if missingValueCheckColumns:
        from sklearn.preprocessing import Imputer
        if not missingValueStrategy:
            missingValueStrategy='mean'
            imputer = Imputer(missing_values='NaN', strategy=missingValueStrategy, axis=0)  #axis=0, column
        
        else:
            imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)  #axis=0, column
        
        for mvc in missingValueCheckColumns:
            X[:,[mvc]] = imputer.fit_transform(X[:,[mvc]]) #In python upperbound is excluded)
        
    #Encoding
    if encodingColumns:
        from sklearn.preprocessing import LabelEncoder, OneHotEncoder
        for ec in encodingColumns:
            labelEncoderX = LabelEncoder()
            X[:, ec] = labelEncoderX.fit_transform(X[:, ec])
        for ec in encodingColumns_with_oneHot:
            oneHotEncoderX = OneHotEncoder(categorical_features=[ec]) #feature index = 0
            X = oneHotEncoderX.fit_transform(X).toarray()


    if doLabelEncodeTargetColumns:
            labelEncoder_y = LabelEncoder()
            y = labelEncoder_y.fit_transform(y.ravel())
            
    
    #Split dataset into training and test
    from sklearn.model_selection import train_test_split
    XTrain, XTest, yTrain, yTest = train_test_split(X,y,test_size=testSize,random_state=randomState)
    
    #Feature scaling
    if scalingColumns:
        if typeOfScaling=='standardization':
                from sklearn.preprocessing import StandardScaler
                scalerX = StandardScaler()
                XTrain = scalerX.fit_transform(XTrain.astype(float))  #we will fit & transform the training dataset
                XTest = scalerX.transform(XTest.astype(float))   #we only transform our test set based on fit params in training set
        elif typeOfScaling=='minmax':
            for ec in scalingColumns:
                from sklearn.preprocessing import MinMaxScaler
                scalerX = MinMaxScaler()
                XTrain[scalingColumns]= scalerX.fit_transform(XTrain.astype(float)[scalingColumns])  #we will fit & transform the training dataset
                XTest[scalingColumns] = scalerX.transform(XTest.astype(float)[scalingColumns])   #we only transform our test set based on fit params in training set
   
        else:
            print("Error! not understood the type of scaling. Default action: DO NOTHING.")
        if dont_splitdata == True:
                from sklearn.preprocessing import StandardScaler
                scalerX = StandardScaler()
                X = scalerX.fit_transform(X.astype(float))
                return X,y
      
    return XTrain, XTest, yTrain, yTest

