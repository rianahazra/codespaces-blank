import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt #graphing

file_path=r"data/expense.csv"
dataframe=pd.read_csv(file_path)
date_from=st.date_input("From Date: 🗓️")
date_to=st.date_input("To Date: 🗓️")
st.write("Amount 💸🤑")
minimum= st.slider("Minimum Amount: 💰",min_value=0,max_value=20000, value=0, step=10) #label, min, max, increase by
maximum= st.slider("Maximum Amount: 💰", min_value=0, max_value=20000, value=20000,step=10)
category=st.multiselect('category ☑️',("Housing","Utilities", "Transportation", "Food", "Healthcare", "Insurance", "Debt Payments","Entertainment", "Personal Care", "Education", "Savings", "Taxes", "Miscellaneous"), placeholder="Select an option(s) of your choice")

dataframe["Date"]=pd.to_datetime(dataframe["Date"])
date_from= pd.to_datetime(date_from)
date_to=pd.to_datetime(date_to)

if len(category)==0: #havent selected anything
    condition=(dataframe["Date"]>=date_from) & (dataframe["Date"]<=date_to) & (dataframe["Amount"]>=minimum) & (dataframe["Amount"]<=maximum) 
    dataframe=dataframe[condition]
else: 
    condition=(dataframe["Date"]>=date_from) & (dataframe["Date"]<=date_to) & (dataframe["Amount"]>=minimum) & (dataframe["Amount"]<=maximum) & (dataframe ["Category"]).isin(category)
    dataframe=dataframe[condition]
st.title("Expenses 💰")
st.dataframe(dataframe[["Category", "Description", "Currency", "Amount"]].reset_index(drop=True)) #reset to get 0,1,2,3
category_expenses = dataframe.groupby("Category")["Amount"].sum()
fig, ax = plt.subplots()
ax.bar(category_expenses.index, category_expenses.values)
st.title("line graph")
st.line_chart(dataframe["Amount"])
fig3, axs=plt.subplots()
axs.pie(category_expenses.values, labels=category_expenses.index, autopct="%1.1f%%", shadow=True, startangle=53, textprops={"color":"blue"})
ax.set_xlabel("Category")
ax.set_ylabel("Total Expense")
ax.set_title("Expenses by Category")
st.pyplot(fig)
st.pyplot(fig3)
