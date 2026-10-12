import pandas as pd

df = pd.read_csv("titanic.csv")
print("\n print the first 10 entires")
print(df.head(10))
print("\n prints the shape")
print(df.shape)
print("\n pints the number of missing enties in each row")
print(df.isnull().sum())

#fill the missing values using mean mode and median

#fill the missing age values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

#fill the missing fare valuse using the median
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
#fill the missing values of the embarked with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode())

df = df.drop(columns=["Cabin"])
print("values after handling the missing values")
print(df.isnull().sum())

#FEATURE SCALING

#1.MIN MAX SCALING:

# from sklearn.preprocessing import MinMaxScaler
# feature = df[["Age","Fare"]].dropna()

# scaler = MinMaxScaler()
# scaled = scaler.fit_transform(feature)

# scaled_df = pd.DataFrame(scaled, columns = ["Age", "Fare"])
# print(scaled_df.head())

from sklearn.preprocessing import StandardScaler
features = df[["Age", "Fare"]].dropna()
scaler = StandardScaler()
scaled = scaler.fit_transform(features)
scaled_df = pd.DataFrame(scaled, columns = ["Age", "Fare"])
print(scaled_df.head(10))

#ONE-HOT ENCODING
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(
    sparse_output=False,
    handle_unknown="ignore"
)
encoded_data = encoder.fit_transform(
    df[["Sex", "Embarked"]]
)
encoded_df = pd.DataFrame(
    encoded_data,
    columns=encoder.get_feature_names_out(
        ["Sex", "Embarked"]
    )
)
print(encoded_df.head(10))

#LABLE ENCODING
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["Sex_encoded"] = le.fit_transform(df["Sex"])
print(df[["Sex", "Sex_encoded"]].head(10))


