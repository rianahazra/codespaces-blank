import streamlit as st
import pandas as pd
import os

folder="data"
file_path=r"data/expense.csv"
if not os.path.exists(folder): #if no folder create a folder
    os.makedirs(folder)

if not os.path.exists(file_path): #if no file create a file
    expenses=pd.DataFrame(columns=["Date", "Category", "Description", "Currency", "Amount"])
    expenses.to_csv(file_path, index=False) #false or 0, no index, true or 1, index

file1_path=r"data/feedback.csv"
if not os.path.exists(file1_path): #if no file create a file
    df2=pd.DataFrame(columns=["Feedback", "Slider"])
    df2.to_csv(file1_path, index=False) #false or 0, no index, true or 1, index


def insert(date,category,description,currency,amount):
    df=pd.read_csv(file_path)
    len1=len(df)
    if description != "" and amount>0: #dont write key as function
        df.loc[len1]=[date,category,description,currency,amount]# = means inserting 
        df.to_csv(file_path, index =False)
        st.balloons()
    else:
        st.error("Please provide a description and a valid amount >0", icon="🚨")
def insert1(feedback,slider):
    df1=pd.read_csv(file1_path)
    len2=len(df1)
    df1.loc[len2]=[feedback,slider]
    df1.to_csv(file1_path, index=False)
def clear():
    st.session_state.desc="" #clears desc
    st.session_state.amt=0 #clears amt
def clear1():
    st.session_state.fd=""
tab1,tab2=st.tabs(["Add expenses", "Feedback"])
with tab1:
    st.title("Expense Tracker")
    date=st.date_input('Date :date:')
    category=st.selectbox('category ☑️',("Housing","Utilities", "Transportation", "Food", "Healthcare", "Insurance", "Debt Payments","Entertainment", "Personal Care", "Education", "Savings", "Taxes", "Miscellaneous"))
    description=st.text_input("Description 💡", key='desc') #key is like giving an id, can clear the desc using the key
    currency=st.selectbox('currency🤑',("Dollar", "Euro", "Rupee", "Yen", "Won", "Yuan", "Pound"))
    amount=st.number_input("Amount 💸", min_value=0, key='amt')
    column1,column2=st.columns([0.5,0.5]) #add square bracket
    with column1:
        expense=st.button("Add Expense") 
        
    with column2:
        clear=st.button("Clear", on_click=clear)
        
    if expense:
        insert(date,category,description,currency,amount)
with tab2:
    feedback=st.text_input("Please enter any comments you have", key="fd")
    slider=st.slider("Please select a rating",
                      0, 10)
    column1,column2=st.columns([0.5,0.5]) #add square bracket
    with column1:
        submit=st.button("Submit your feedback")
        if submit:
            insert1(feedback,slider)
    with column2:
        clear1=st.button("Clear feedback", on_click=clear1)
