import pandas as pd
from sklearn.cluster import KMeans


def segment_customers(transactions_df, n_clusters=3):
    """
    Segment customers based on spending behavior
    """

    customer_data = transactions_df.groupby('Customer_ID').agg({
        'Price': 'sum',
        'Product': 'count'
    }).reset_index()

    customer_data.columns = ['Customer_ID', 'Total_Spending', 'Purchase_Count']

    features = customer_data[['Total_Spending', 'Purchase_Count']]

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)

    customer_data['Segment'] = kmeans.fit_predict(features)

    return customer_data