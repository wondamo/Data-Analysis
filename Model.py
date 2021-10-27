import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score,f1_score,recall_score,confusion_matrix

data=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Data Analysis/data_cleaned.csv")
data.head()

X=data.drop(['Loan_Status','Loan_ID'],axis=1)
y=data['Loan_Status']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,stratify=y,random_state=21)

model=XGBClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test,y_pred)}')
print(f'F1: {f1_score(y_test,y_pred)}')
print(f'Recall: {recall_score(y_test,y_pred)}')
m=confusion_matrix(y_test,y_pred)

sns.heatmap(m,annot=True)
plt.savefig('/content/drive/MyDrive/Colab Notebooks/Data Analysis/Pics/heatmap.png')