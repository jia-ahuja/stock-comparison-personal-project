import streamlit as st
import pandas as pd

st.header('Stock Comparison Tool')

stock_name = st.text_input('Stock name')

options = st.multiselect(
    "Columns to compare",
    ['valuation', 'grade', 'quad', 'valuscor', 'cmp', 'pe', 'fv', 'eq', 'dy', 'np2eq', 'cmp2npeq', 'ttmsal', 'salfy', 'salq0', 'salq1', 'ttmnp', 'npfy', 'npq0', 'npq1', 'ttmeps', 'epsfy', 'epsq0', 'epsq1', 'roe3y', 'roa3y', 'roce3y', 'debt', 'intcov', 'db2eq', 'ncffy', 'fcffy', 'ev2fcf', 'ph'],
    default=['valuation', 'grade', 'quad', 'valuscor', 'cmp', 'pe', 'fv', 'np2eq', 'ph']
)

def find_stock(df, search_term):
    # search through nsecode (exact match)
    if 'nsecode' in df.columns:
        result = df[df['nsecode'].notna() & (df['nsecode'].astype(str).str.upper() == search_term.upper())]
        if len(result) > 0:
            return result
    
    # search through name
    if 'name' in df.columns:
        result = df[df['name'].str.contains(search_term, case=False, na=False)]
        if len(result) > 0:
            return result
    
    return pd.DataFrame()

if st.button('Get data'):
    if stock_name and options:
        try:
            df_jan = pd.read_excel('file1.xlsx')  
            df_apr = pd.read_excel('file2.xlsx') 
            df_jun = pd.read_excel('file3.xlsx') 


            stock_jan = find_stock(df_jan, stock_name.strip())
            stock_apr = find_stock(df_apr, stock_name.strip())
            stock_jun = find_stock(df_jun, stock_name.strip())
            
            comparison_data = []
            
            for column in options:
                    row = {
                        'Metric': column,
                        'Jan 2025': stock_jan[column].iloc[0] if len(stock_jan) > 0 and column in stock_jan.columns else 'N/A',
                        'Apr 2025': stock_apr[column].iloc[0] if len(stock_apr) > 0 and column in stock_apr.columns else 'N/A',
                        'Jun 2025': stock_jun[column].iloc[0] if len(stock_jun) > 0 and column in stock_jun.columns else 'N/A'
                    }
                    comparison_data.append(row)
                
            
            names_row = {
                'Metric': 'Stock Name',
                'Jan 2025': stock_jan['name'].iloc[0] if len(stock_jan) > 0 and 'name' in stock_jan.columns else 'N/A',
                'Apr 2025': stock_apr['name'].iloc[0] if len(stock_apr) > 0 and 'name' in stock_apr.columns else 'N/A',
                'Jun 2025': stock_jun['name'].iloc[0] if len(stock_jun) > 0 and 'name' in stock_jun.columns else 'N/A'
            }
            comparison_data.insert(0, names_row)
            
            comparison_df = pd.DataFrame(comparison_data).astype(str)
            transposed_df = comparison_df.set_index('Metric').T.reset_index()
            st.dataframe(transposed_df, use_container_width=False)


        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        if not stock_name:
            st.warning("Please enter a stock name.")
        if not options:
            st.warning("Please select at least one column to compare.")




