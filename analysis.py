import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("customer_data.csv")
print(df.head())

# Data celaning
df.drop_duplicates(inplace=True)
print(df.isnull().sum())
df['Income'].fillna(df['Income'].mean(), inplace=True)

# creating Age Groups
bins = [18, 25, 35, 45, 60]
labels = ['18-25', '26-35', '36-45', '46-60']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

print(df[['Age', 'Age_Group']])

# Age Group Analysis
age_group_sales = df.groupby('Age_Group')['Purchase_Amount'].sum()
print(age_group_sales)

age_group_sales.plot(kind='bar')
plt.title("Purchase by Age Group")
plt.show()

#Gender Analysis
gender_sales = df.groupby('Gender')['Purchase_Amount'].sum()
print(gender_sales)

gender_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender-wise Purchase")
plt.show()

#Region Analysis
region_count = df.groupby('Location')['Customer_ID'].count()
print(region_count)

region_count.plot(kind='bar')
plt.title("Region-wise Customer Count")
plt.show()

# Save cleaned data
df.to_csv("cleaned_customer_data.csv", index=False)