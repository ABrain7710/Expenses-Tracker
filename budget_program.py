import pandas as pd
import math


#creates a dict that has every month of the year as the key and the df created from the excel sheet as the value
def get_budget_dfs():
    months = ['August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'July']
    budget_excel = pd.ExcelFile(r'/Users/andrew_brain/Documents/Budget/budget_tracking.xlsx')

    budget_dfs = {}
    for month in months:
        df = pd.read_excel(budget_excel, month)
        budget_dfs[month] = df

    return budget_dfs


# groups the budget_df by Specific Category and sums the costs
# which returns a df with the cost per Specific Category
# currently groups the Bathroom and Laundry categories into toiletries
def get_main_cat_df(df, merge_toiletries=False):

    #groups bathroom and laundry categories into Toiletries
    if merge_toiletries:

        # get total cost of laundry and bathroom
        toiletries_cost = df.loc[(df['Main Category'] == "Bathroom") | (df['Main Category'] == "Laundry")].sum()['Cost']

        #remove bathroom and launry rows
        df.drop(df[df['Main Category'] == "Bathroom"].index, inplace = True)
        df.drop(df[df['Main Category'] == "Laundry"].index, inplace = True)

        #Add new row with toiletries to replace the removed bathroom and launry rows
        toilteries = {'Item': 'Toiletries', 'Cost': toiletries_cost, 'Main Category': "Toiletries"}
        df = df.append(toilteries, ignore_index=True)

    # group by Main Category and sum the costs
    main_category_df = df.groupby(["Main Category"]).sum().reset_index()

    return main_category_df

# groups the budget_df by Specific Category and sums the costs
# which returns a df with the cost per Specific Category
def get_specific_cat_df(df):

    return df.groupby(["Specific Category"]).sum().reset_index()

# prints out df with the specified row_name and the cost
def print_df(df, row_name):

    for index, row in df.iterrows():
        print(f"{row[row_name]} : {round(row['Cost'],2)}")



budget_dfs = get_budget_dfs()
main_category_df = get_main_cat_df(df=budget_dfs["August"], merge_toiletries=True)
specific_category_df = get_specific_cat_df(df=budget_dfs["August"])

print_df(main_category_df, 'Main Category')
print("\n\n")
print_df(specific_category_df, 'Specific Category')
