# backend/pos/pos_loader.py

import pandas as pd
from backend.database.mongo_connection import get_database

def load_pos_data(csv_path="datasets/transactions.csv"):
    """
    Load POS transaction data from CSV and insert into MongoDB
    """

    db = get_database()
    transactions_collection = db["transactions"]

    df = pd.read_csv(csv_path)

    records = df.to_dict(orient="records")

    if records:
        transactions_collection.insert_many(records)

    return {
        "message": "POS data loaded successfully",
        "records_inserted": len(records)
    }


if __name__ == "__main__":
    result = load_pos_data()
    print(result)