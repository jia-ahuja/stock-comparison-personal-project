import streamlit as st
import pandas as pd

st.header('Stock Comparison Tool')

stock_name = st.text_input('Stock name')

options = st.multiselect(
    "Columns to compare",
    ['valuation', 'grade', 'quad', 'valuscor', 'cmp', 'pe', 'fv', 'eq', 'dy', 'np2eq', 'cmp2npeq', 'ttmsal', 'salfy', 'salq0', 'salq1', 'ttmnp', 'npfy', 'npq0', 'npq1', 'ttmeps', 'epsfy', 'epsq0', 'epsq1', 'roe3y', 'roa3y', 'roce3y', 'debt', 'intcov', 'db2eq', 'ncffy', 'fcffy', 'ev2fcf', 'ph']
)


if st.button('Get data'):
    if stock_name and options:
        try:
            df_2022 = pd.read_excel('file1.xlsx')  
            df_2023 = pd.read_excel('file2.xlsx') 
            df_2024 = pd.read_excel('file3.xlsx') 


            stock_2022 = df_2022[df_2022['name'].str.contains(stock_name, case=False, na=False)]
            stock_2023 = df_2023[df_2023['name'].str.contains(stock_name, case=False, na=False)]
            stock_2024 = df_2024[df_2024['name'].str.contains(stock_name, case=False, na=False)]
            
            comparison_data = []
            
            for column in options:
                row = {
                    'Metric': column,
                    '2022': stock_2022[column].iloc[0] if len(stock_2022) > 0 and column in stock_2022.columns else 'N/A',
                    '2023': stock_2023[column].iloc[0] if len(stock_2023) > 0 and column in stock_2023.columns else 'N/A',
                    '2024': stock_2024[column].iloc[0] if len(stock_2024) > 0 and column in stock_2024.columns else 'N/A'
                }
                comparison_data.append(row)
            
            comparison_df = pd.DataFrame(comparison_data)

            actual_stock_name = stock_name  
            if len(stock_2024) > 0:
                actual_stock_name = stock_2024['name'].iloc[0]
            elif len(stock_2023) > 0:
                actual_stock_name = stock_2023['name'].iloc[0]
            elif len(stock_2022) > 0:
                actual_stock_name = stock_2022['name'].iloc[0]

            st.write('Collecting comparison data for:', actual_stock_name)
            
            st.table(comparison_df)


        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        if not stock_name:
            st.warning("Please enter a stock name.")
        if not options:
            st.warning("Please select at least one column to compare.")

