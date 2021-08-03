import pandas as pd

def get_budget_dfs():
    months = ['August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'July']
    budget_excel = pd.ExcelFile(r'/Users/andrew_brain/Documents/Budget/budget_tracking.xlsx')

    budget_dfs = {}
    for month in months:
        df = pd.read_excel(budget_excel, month)
        budget_dfs[month] = df

    return budget_dfs



def get_main_cat_df(df, merge_toiletries=False):

    if merge_toiletries:
        toiletries_cost = df.loc[(df['Main Category'] == "Bathroom") | (df['Main Category'] == "Laundry")].sum()['Cost']
        df.drop(df[df['Main Category'] == "Bathroom"].index, inplace = True)
        df.drop(df[df['Main Category'] == "Laundry"].index, inplace = True)
        toilteries = {'Item': 'Toiletries', 'Cost': toiletries_cost, 'Main Category': "Toiletries"}
        df = df.append(toilteries, ignore_index=True)

    main_category_df = df.groupby(["Main Category"]).sum().reset_index()

    return main_category_df

def get_specific_cat_df(df):

    return df.groupby(["Specific Category"]).sum().reset_index()

budget_dfs = get_budget_dfs()

main_category_df = get_main_cat_df(df=budget_dfs["August"], merge_toiletries=True)
specific_category_df = get_specific_cat_df(df=budget_dfs["August"])

print(main_category_df)
print("\n\n")
print(specific_category_df)
