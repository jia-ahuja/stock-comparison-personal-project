import streamlit as st
import pandas as pd

st.header('Stock Comparison Tool')

stock_name = st.text_input('Stock name')

options = st.multiselect(
    "Columns to compare",
    ['valuation', 'grade', 'quad', 'valuscor', 'cmp', 'pe', 'fv', 'eq', 'dy', 'np2eq', 'cmp2npeq', 'ttmsal', 'salfy', 'salq0', 'salq1', 'ttmnp', 'npfy', 'npq0', 'npq1', 'ttmeps', 'epsfy', 'epsq0', 'epsq1', 'roe3y', 'roa3y', 'roce3y', 'debt', 'intcov', 'db2eq', 'ncffy', 'fcffy', 'ev2fcf', 'ph'],
    default=['valuation', 'grade', 'quad', 'valuscor', 'cmp']
)


if st.button('Get data'):
    if stock_name and options:
        try:
            df_jan = pd.read_excel('file1.xlsx')  
            df_apr = pd.read_excel('file2.xlsx') 
            df_jun = pd.read_excel('file3.xlsx') 


            stock_jan = df_jan[df_jan['name'].str.contains(stock_name, case=False, na=False)]
            stock_apr = df_apr[df_apr['name'].str.contains(stock_name, case=False, na=False)]
            stock_jun = df_jun[df_jun['name'].str.contains(stock_name, case=False, na=False)]
            
            comparison_data = []
            
            for column in options:
                row = {
                    'Metric': column,
                    'Jan 2025': stock_jan[column].iloc[0] if len(stock_jan) > 0 and column in stock_jan.columns else 'N/A',
                    'Apr 2025': stock_apr[column].iloc[0] if len(stock_apr) > 0 and column in stock_apr.columns else 'N/A',
                    'Jun 2025': stock_jun[column].iloc[0] if len(stock_jun) > 0 and column in stock_jun.columns else 'N/A'
                }
                comparison_data.append(row)
            
            comparison_df = pd.DataFrame(comparison_data)

            actual_stock_name = stock_name  
            if len(stock_jun) > 0:
                actual_stock_name = stock_jun['name'].iloc[0]
            elif len(stock_apr) > 0:
                actual_stock_name = stock_apr['name'].iloc[0]
            elif len(stock_jan) > 0:
                actual_stock_name = stock_jan['name'].iloc[0]

            st.write('Collecting comparison data for:', actual_stock_name)
            
            st.table(comparison_df)


        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        if not stock_name:
            st.warning("Please enter a stock name.")
        if not options:
            st.warning("Please select at least one column to compare.")


