import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("GURGAON DATA.csv")
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.isnull().sum())

# DATA CLEANING

df.columns=df.columns.str.strip().str.upper().str.replace(' ','_')
print(df.columns)

# NUMERIC COLUMNS CLEANING

df["PRICE"]=df["PRICE"].astype(str).str.replace(",","").astype(float)
print(df["PRICE"])

df["AREA"]=df["AREA"].astype(int)
print(df["AREA"])

df["RATE_PER_SQFT"] = df['RATE_PER_SQFT'].astype(str).str.replace(",", "").astype(float)
print(df['RATE_PER_SQFT'])

df=df.drop_duplicates()
print(df.shape)

# CLEAN CATEGORICAL COLUMNS
df["STATUS"]=df["STATUS"].str.strip().str.lower()
print(df["STATUS"])

df["PROPERTY_TYPE"]=df["PROPERTY_TYPE"].str.strip().str.lower()
print(df["PROPERTY_TYPE"])

df["RERA_APPROVAL"]=df["RERA_APPROVAL"].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
print(df["RERA_APPROVAL"])

df["COMPANY_NAME"]=df["COMPANY_NAME"].str.strip().str.upper()
print(df["COMPANY_NAME"])

df.info()

# QUESTION NO.1 WHICH IS THE COSTLIEST AND CHEAPEST FLAT?

costliest_flat=df.loc[df["PRICE"].idxmax()]
print(costliest_flat)

cheapest_flat=df.loc[df["PRICE"].idxmin()]
print(cheapest_flat)


# QUESTION NO.2 WHICH LOCALITY HAVE THE HIGHEST AND LOWEST AVERAGE PRICE
highest_avg_price_locality=df.groupby("LOCALITY")["PRICE"].mean().idxmax()
print(highest_avg_price_locality)

lowest_avg_price_locality=df.groupby("LOCALITY")["PRICE"].mean().idxmin()
print(lowest_avg_price_locality)

# QUESTION NO.3 WHICH LOCALITY HAS THE HIGHEST AND LOWEST RATE PER SQUARE FOOT
highest_rate_per_square_foot_locality=df.groupby("LOCALITY")["RATE_PER_SQFT"].mean().sort_values(ascending=False)
print(f"The locality with the highest rate per square foot is {highest_rate_per_square_foot_locality.index[0]}")

lowest_rate_per_square_foot_locality=df.groupby("LOCALITY")["RATE_PER_SQFT"].mean().idxmin()
print(f"The locality with the lowest rate per square foot is {lowest_rate_per_square_foot_locality}")

# QUESTION NO.4 PROPERTY STATUS VS PRICING
status_mean=df.groupby("STATUS")["PRICE"].mean()
print(status_mean)

status_median=df.groupby("STATUS")["PRICE"].median()
print(status_median)

status_max=df.groupby("STATUS")["PRICE"].max()
print(status_max)

status_min=df.groupby("STATUS")["PRICE"].min()
print(status_min)

# QUESTION NO.5 FLAT_TYPE  VS PRICING

flat_price_mean=df.groupby("FLAT_TYPE")["PRICE"].mean()
print(flat_price_mean)

flat_price_median=df.groupby("FLAT_TYPE")["PRICE"].median()
print(flat_price_median)

maximum_flat_price=df.groupby("FLAT_TYPE")["PRICE"].max()
print(maximum_flat_price)

minimum_flat_price=df.groupby("FLAT_TYPE")["PRICE"].min()
print(minimum_flat_price)

# QUESTION NO.6 PROPERTY TYPE VS RATE_PER_SQFT

rate_mean=df.groupby("PROPERTY_TYPE")["RATE_PER_SQFT"].mean().sort_values(ascending=False)
print(rate_mean.head())

rate_median=df.groupby("PROPERTY_TYPE")["RATE_PER_SQFT"].median().sort_values(ascending=True)
print(rate_median.head())

max_rate=df.groupby("PROPERTY_TYPE")["RATE_PER_SQFT"].max().sort_values(ascending=False)
print(max_rate.head())

min_rate=df.groupby("PROPERTY_TYPE")["RATE_PER_SQFT"].min().sort_values(ascending=True)
print(min_rate.head())

# QUESTION NO.7 DOES RERA APPROVAL AFFECT PRICING?
print(df.groupby("RERA_APPROVAL")["PRICE"].median())

# QUESTION NO.8 DOES PROPERTY TYPE AFFECT PRICING?
print(df.groupby("PROPERTY_TYPE")["PRICE"].median().sort_values(ascending=False).head())

# QUESTION N0.9 HOW DOES STATUS AFFECT PRICE?

plt.style.use("ggplot")
sns.barplot(x="STATUS",y="PRICE",hue="RERA_APPROVAL",data=df)
plt.xlabel("STATUS")
plt.ylabel("PRICE")
plt.title("STATUS VS PRICE")
plt.savefig("STATUS VS PRICE.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# QUESTION NO.10 WHICH SOCIETIES HAVE THE LOWEST AND HIGHEST LISTING PRICES?

cheapest_society=df.groupby("SOCIETY")["PRICE"].min().sort_values(ascending=True)
print(cheapest_society)

expensive_society=df.groupby("SOCIETY")["PRICE"].max().sort_values(ascending=False)
print(expensive_society)


cheapest_society_desc=df.groupby("SOCIETY")["PRICE"].min().sort_values(ascending=False)
print(cheapest_society_desc)

expensive_society_asc=df.groupby("SOCIETY")["PRICE"].max().sort_values(ascending=True)
print(expensive_society_asc)

# QUESTION NO.11 WHICH PROPERTY TYPE IS THE CHEAPEST AND  COSTLIEST ?

cheapest_price_property=df.groupby("PROPERTY_TYPE")["PRICE"].min()
print(cheapest_price_property)

costliest_price_property=df.groupby("PROPERTY_TYPE")["PRICE"].max()
print(costliest_price_property)

# QUESTION NO.12 DOES FLAT TYPE MATTERS PRICING

price_flat_type=df.groupby("FLAT_TYPE")["PRICE"].median()
print(price_flat_type)

# QUESTION NO.13 WHICH BHK CONFIGURATION IS MOST EXPENSIVE ON AVERAGE?
print(df.groupby("BHK_COUNT")["PRICE"].mean())

# QUESTION NO.14 WHICH COMPANIES HAVE THE HIGHEST MEDIAN LISTING PRICES?
print(df.groupby("COMPANY_NAME")["PRICE"].median().sort_values(ascending=False).head(10))

# QUESTION NO.15 ARE LARGER HOMES MORE EXPENSIVE PER SQUARE FEET?

plt.style.use("bmh")
plt.figure(figsize=(10, 5))
clean_area_df = df[df["AREA"] < 20000] 
sns.scatterplot(x="AREA", y="RATE_PER_SQFT", hue="RERA_APPROVAL", data=clean_area_df, alpha=0.7, palette="Set1")
plt.xlabel("AREA")
plt.ylabel("RATE PER SQUARE FEET")
plt.title("AREA VS RATE PER SQFT")
plt.savefig("AREA VS RATE PER SQFT.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# QUESTION NO.16 HOW DOES PROPERTY AREA RELATE TO PRICE?

plt.style.use("ggplot")
plt.figure(figsize=(10, 5))
mass_market=df[df["PRICE"]<15000000]
sns.scatterplot(x="AREA", y="PRICE", hue="FLAT_TYPE", data=mass_market,alpha=0.7, palette="coolwarm")
plt.xlabel("AREA")
plt.ylabel("PRICE")
plt.title("PROPERTY AREA VS PRICE")
plt.savefig("AREA VS PRICE.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# QUESTION NO.17 HOW DOES STATUS RELATE TO APPROVAL OF RERA?

plt.style.use("ggplot")
plt.figure(figsize=(10, 5))

sns.countplot(x="STATUS", hue="RERA_APPROVAL", data=df,palette="pastel")
plt.xlabel("Construction STATUS")
plt.ylabel("Total Listings")
plt.title("STATUS VS RERA APPROVAL")
plt.savefig("STATUS VS RERA APPROVAL.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

print("\nGURGAON REAL ESTATE MARKET ANALYSIS COMPLETED SUCCESSFULLY!")
print("THANK YOU!")



