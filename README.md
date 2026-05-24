# Customer Lifecycle Segmentation & Leakage Revenue Mapping

## Summary
This project analyzes customer churn patterns and promotional dependencies across a high-volume retail customer base of 9 Million user profiles. By implementing an RFM (Recency, Frequency, Monetary) clustering approach on historical transactional logs, this pipeline successfully isolated a critical margin leakage point where 76% of trial category users churned after a single purchase. 

Predictive financial modeling proved that converting just a fraction of these high-value one-time buyers back into the category uncovers a $5.5 Million revenue opportunity without adding incremental customer acquisition costs.

---

## Tech Stack & Methodologies
* **Language:** Python 3.10+
* **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
* **Methodologies:** RFM Segmentation, Cohort Retention Analysis, Customer Churn Profiling, Revenue Opportunity Sizing

---

## Core Data Insights
1. **The Churn Vector:** 76% of customers who sampled the target retail product class only made a single purchase before dropping out of the category ecosystem entirely.
2. **Promotional Dependency:** 93% of high-frequency shoppers purchase strictly during discount windows, accounting for 74% of total category sales volume. This flags a steep price-elasticity curve and margin erosion risk.
3. **The Value Gap:** 38% of the one-time category churners are actually overall top-tier, high-frequency store loyalists with strong baseline average basket values ($70+). They love the retail store; they are simply skipping this category.

---

## Project Architecture
* `synthetic_data_generator.py`: Generates large-scale transactional records simulating historical retail customer metrics.
* `rfm_segmentation_pipeline.ipynb`: Cleans data, executes user profiling, builds cohort metrics, and measures promotional sensitivity.

---

## Compliance & Confidentiality Disclaimer
To comply with strict standard Non-Disclosure Agreements, all raw source financial scales, operational parameters, and proprietary corporate identities have been completely anonymized, transformed into relative percentages, or synthesized with generative mock variables without breaking the underlying mathematical logic.
