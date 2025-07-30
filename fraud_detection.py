import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(filename='fraud_alerts.log', level=logging.INFO, format='%(asctime)s - %(message)s') # Logger ayarları
df = pd.read_csv('transactions.csv', parse_dates=['transaction_date'])

# Aykırı tutar kontrolü
high_amount = df[df['amount'] > 10000]
if not high_amount.empty:
    logging.warning("⚠ High value transactions detected:")
    print("\n🔴 High value transactions:\n", high_amount)

# Gece saatinde yapılan işlemler (00:00–04:00)
df['hour'] = df['transaction_date'].dt.hour
night_tx = df[(df['hour'] >= 0) & (df['hour'] <= 4)]
if not night_tx.empty:
    logging.warning("🌙 Transactions during suspicious night hours detected.")
    print("\n🌙 Night-time transactions (00:00-04:00):\n", night_tx)

# Aynı gün farklı şehirlerden işlem yapan kullanıcılar
df['date'] = df['transaction_date'].dt.date
suspicious_users = df.groupby(['user_id', 'date'])['location'].nunique().reset_index()
suspicious_users = suspicious_users[suspicious_users['location'] > 1]

if not suspicious_users.empty:
    flagged_users = suspicious_users['user_id'].unique()
    multi_loc_tx = df[df['user_id'].isin(flagged_users)]
    logging.warning("📍 Users with multiple transaction locations on same day detected.")
    print("\n📍 Multiple-location transactions by same user in one day:\n", multi_loc_tx)

if high_amount.empty and night_tx.empty and suspicious_users.empty:
    print("✅ No suspicious activity detected. Data looks clean.")