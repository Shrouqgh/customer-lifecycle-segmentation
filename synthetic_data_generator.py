import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_retail_data(num_customers=5000, num_records=50000):
    print(f"Generating {num_records} synthetic transactional records for {num_customers} loyalty profiles...")
    np.random.seed(42)
    
    # Generate customer base
    customer_ids = [f"PICA_{100000 + i}" for i in range(num_customers)]
    
    # Assign latent segments to ensure realistic data anomalies (76% single-purchase churn)
    customer_types = np.random.choice(['One-Time-Churn', 'Promo-Dependent', 'Core-Loyalist'], 
                                      p=[0.76, 0.19, 0.05], size=num_customers)
    cust_segment_map = dict(zip(customer_ids, customer_types))
    
    start_date = datetime(2025, 3, 1)
    
    data = []
    for _ in range(num_records):
        cust_id = np.random.choice(customer_ids)
        seg = cust_segment_map[cust_id]
        
        # Enforce behavior profiles
        if seg == 'One-Time-Churn' and any(x['customer_id'] == cust_id for x in data):
            continue # Force single purchase limitation for the 76% cohort
            
        days_offset = np.random.randint(0, 365)
        tx_date = start_date + timedelta(days=days_offset)
        
        if seg == 'Promo-Dependent':
            is_promo = np.random.choice([1, 0], p=[0.93, 0.07])
            basket_value = np.round(np.random.normal(140, 25), 2)
        elif seg == 'Core-Loyalist':
            is_promo = np.random.choice([1, 0], p=[0.40, 0.60])
            basket_value = np.round(np.random.normal(310, 40), 2) # Higher value tier
        else: # One-time trial users
            is_promo = np.random.choice([1, 0], p=[0.65, 0.35])
            basket_value = np.round(np.random.normal(226, 30), 2)
            
        data.append({
            "transaction_id": f"TX_{1000000 + len(data)}",
            "customer_id": cust_id,
            "transaction_date": tx_date.strftime("%Y-%m-%d"),
            "basket_value_sar": max(10.0, basket_value),
            "is_promotional": is_promo,
            "category_class": np.random.choice(["Toilet Soap", "Toothpaste", "Deodorants", "Feminine Care"], p=[0.28, 0.16, 0.15, 0.41])
        })
        
    df = pd.DataFrame(data)
    df.to_csv("synthetic_retail_transactions.csv", index=False)
    print("Data extraction pipeline simulation complete. File saved as 'synthetic_retail_transactions.csv'.")

if __name__ == "__main__":
    generate_mock_retail_data()
