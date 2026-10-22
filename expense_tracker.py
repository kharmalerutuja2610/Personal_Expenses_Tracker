import pandas as pd

data = {
"Date": ["2026-10-01", "2026-10-02", "2026-10-03", "2026-10-04", "2026-10-05"],
"Category": ["Food", "Travel", "Shopping", "Food", "Bills"],
"Amount": [150, 80, 500, 200, 300]
}

df = pd.DataFrame(data)

print("Expense Data:")
print(df)

print("\nTotal Expense:", df["Amount"].sum())

print("\nCategory-wise Expense:")
print(df.groupby("Category")["Amount"].sum())
category_expense = df.groupby("Category")["Amount"].sum()

print("\nHighest Expense Category:")
print(category_expense.idxmax(), "-", category_expense.max())