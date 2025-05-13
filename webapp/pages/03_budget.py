import streamlit as st
import pandas as pd
file_path=r"data/expense.csv"
# Define currency conversion rates to USD
currency_conversion = {
    "Dollars": 1,  # 1 Dollar = 1 Dollar
    "Yen": 5,
    "Euros": 1.1,  # 1 Euro = 1.1 Dollars (you can change this rate as per current conversion rates)
}
def clear():
    st.session_state.amt1=0 #clears amt
tab1,tab2=st.tabs(["Budget", "Analysis"])
with tab1:   
    month1=st.slider("Please select a month", 1,12)
    year1=st.number_input("Year 🗓️", min_value=2000)
    budget=st.number_input(f'Amount {month1}/{year1}💸', min_value=0, key='amt1')
    df=pd.read_csv(file_path)
    df["Date"]=pd.to_datetime(df["Date"])
    df_filter=df[(df["Date"].dt.month==month1) & (df["Date"].dt.year==year1)]
    df_filter["Amount in USD"] = df_filter.apply(lambda row: row[
    "Amount"] * currency_conversion.get(row["Currency"], 1),
                                                    axis=1)
    monthlybudget=df_filter["Amount in USD"].sum()
    if budget>0:
        if monthlybudget>budget:
            st.write("Sleep with one eye open👁️")
        else:
            st.write(f'You saved {budget-monthlybudget}')
    st.write(f'expenses for {month1}/{year1}:')
    st.dataframe(df_filter)
    st.title("Amount (Converted to USD) :money_with_wings:")
    st.line_chart(df_filter["Amount in USD"])

    if st.button("clear"):
        clear()
with tab2:
    st.title("Analyzing your expenditure 🚨")



