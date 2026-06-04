import pandas as pd

from app.models import Transaction


def load_transactions(
        file_path,
        db
):
    df = pd.read_csv(file_path)

    inserted = 0

    for _, row in df.iterrows():

        transaction_id = (
            f"{row['invoice_number']}_{row['sku']}"
        )

        existing = (
            db.query(Transaction)
            .filter(
                Transaction.transaction_id
                == transaction_id
            )
            .first()
        )

        if existing:
            continue

        transaction = Transaction(
            transaction_id=transaction_id,
            invoice_number=row["invoice_number"],
            store_id=row["store_id"],
            store_name=row["store_name"],
            brand_name=row["brand_name"],
            product_name=row["product_name"],
            salesperson_name=row["salesperson_name"],
            quantity=row["qty"],
            total_amount=row["total_amount"],
            timestamp=pd.to_datetime(
                f"{row['order_date']} {row['order_time']}"
            )
        )

        db.add(transaction)

        inserted += 1

    db.commit()

    return inserted
