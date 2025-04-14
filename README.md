# 🚗 Used Cars Data Warehouse Project

## 📊 Overview

This project involves the design and implementation of a **Data Warehouse** to analyze pricing trends in the used cars market. It incorporates **ETL processes** using **Talend** and **Python**, storing data in **MySQL**, and performing multidimensional analysis through an **OLAP cube** using **Pentaho**.

---

## 🛠️ Tools & Technologies

- **ETL Tools:** Talend, Python (Pandas, SQL libraries)
- **Database:** MySQL
- **Data Format:** CSV (5000 rows × 10 columns)

---

## 🔁 ETL Process

### 🔍 Extraction
- **Talend:** Read data from `Cars_File.csv`
- **Python:** Used Pandas to load and inspect data

### 🧹 Transformation
- Filtered rows with null/illogical values
- Removed unneeded columns (e.g., "additional information")
- Mapped and divided data into **dimensions** and **facts**
- Created primary keys and structured dimension tables

### 💾 Loading
- Loaded data into 5 MySQL tables (dimension + fact)
- Used Python and Talend for loading processes

---

## 🧱 Data Warehouse Schema

### ✅ Fact Table:
- `fact_prix`: Holds car prices

### ✅ Dimensions:
- `brand_model`: Brand and model information
- `date`: Year and age of car
- `mileage`: Vehicle mileage
- `information`: Fuel type, transmission, etc.

---

## 📈 OLAP Cube

Created using **Pentaho** to support:
- Brand-level value analysis
- Price trends by year and mileage
- Insightful custom queries

---

## 💡 Insights

- Which brands/models retain value over time
- Pricing impact of mileage and age
- Trends useful for consumers, dealerships, and market analysts

---

## 📌 Conclusion

This project highlights the efficiency of combining **ETL automation** with **data modeling** and **BI tools** to uncover valuable insights from raw datasets. The architecture enables both deep analysis and practical business applications in the automotive sector.

---

## 👨‍💻 Authors

- Aymen Ben Youssef
- Med Ali Kechrida  
