# Fraud-Risk-Detection-with-SQL-and-Python
Bu proje, işlem verileri üzerinde sahtecilik ve riskli davranışları tespit etmek için geliştirilmiş hafif ama etkili bir analiz sistemidir. Python ve SQL kullanılarak gerçekleştirilen bu analiz, iç denetim, risk kontrolü ve veri güvenliği konularında temel bir bakış sunar.

## 🎯 Projenin Amacı

Gerçek dünyaya uygun sahtecilik senaryolarını veri üzerinden tespit ederek:
- Şüpheli yüksek tutarlı işlemleri,
- Gece saatlerinde gerçekleşen aktiviteleri,
- Aynı kullanıcının farklı şehirlerden işlem yapmasını

analiz etmek ve uyarılar/loglar üretmek.

## 🛠 Kullanılan Teknolojiler

- 🐍 Python (Pandas, datetime, logging)
- 🗃 SQL (SQLite örneği ile)
- 📊 Anomali tespiti kuralları
- 📁 CSV üzerinden veri analizi
- 🪵 Log dosyası çıktısı (fraud_alerts.log)

## 🔎 Yapılan Analizler

1. *High-value transaction detection*  
   → amount > 10,000

2. *Suspicious activity during late hours*  
   → İşlemler 00:00–04:00 arasında

3. *Same user, different locations on same day*  
   → Aynı gün içinde farklı şehirlerden işlem yapan kullanıcılar

## 📂 Klasör Yapıs
fraud-risk-detection-sql-python/
├── data/
│   └── transactions.csv
├── scripts/
│   └── fraud_detection.py
├── fraud_alerts.log
