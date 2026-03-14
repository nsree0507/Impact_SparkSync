import pandas as pd
from mlxtend.frequent_patterns import association_rules
from backend.models.apriori_model import generate_frequent_itemsets


def generate_rules(transactions_df):
    """
    Generate association rules
    """

    frequent_itemsets = generate_frequent_itemsets(transactions_df)

    rules = association_rules(
        frequent_itemsets,
        metric="confidence",
        min_threshold=0.3
    )

    return rules


def recommend_products(transactions_df, purchased_products):
    """
    Recommend products based on purchased products
    """

    rules = generate_rules(transactions_df)

    recommendations = []

    for _, row in rules.iterrows():

        antecedents = list(row['antecedents'])
        consequents = list(row['consequents'])

        for product in purchased_products:
            if product in antecedents:
                recommendations.extend(consequents)

    # Remove duplicates
    return list(set(recommendations))