import pandas as pd
from mlxtend.frequent_patterns import apriori


def generate_frequent_itemsets(transactions_df, min_support=0.02):
    """
    Generate frequent itemsets using Apriori algorithm
    """

    # Convert transactions to basket format
    basket = (
        transactions_df
        .groupby(['Customer_ID', 'Product'])['Product']
        .count()
        .unstack()
        .fillna(0)
    )

    # Convert counts to binary
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)

    # Run Apriori
    frequent_itemsets = apriori(
        basket,
        min_support=min_support,
        use_colnames=True
    )

    return frequent_itemsets