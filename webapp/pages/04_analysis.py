import streamlit as st
import pandas as pd
file_path=r"data/expense.csv"
currency_conversion = {
    "Dollars": 1,  # 1 Dollar = 1 Dollar
    "Yen": 5,
    "Euros": 1.1,  # 1 Euro = 1.1 Dollars (you can change this rate as per current conversion rates)
}
df=pd.read_csv(file_path)
df["Date"]=pd.to_datetime(df["Date"])
df["Amount in USD"] = df.apply(lambda row: row[
"Amount"] * currency_conversion.get(row["Currency"], 1),
                                                axis=1)
monthlybudget=df["Amount in USD"].sum()
if len(df)!=0:
    maxamount=df[df["Amount in USD"]==df["Amount in USD"].max()]
    st.subheader("You are spending the most in here:┗( T﹏T )┛")
    st.dataframe(maxamount)#displays dataframe
    minamount=df[df["Amount in USD"]==df["Amount in USD"].min()]
    st.subheader("You are spending the least in here: (￣y▽￣)╭ ")
    st.dataframe(minamount)#displays dataframe
