# Crypto Arbitrage Graph Analysis  
**Python · REST APIs · NetworkX · Graph Algorithms · ETL Logic**

This project retrieves real-time cryptocurrency exchange rates from the CoinGecko API and constructs a **weighted directed graph** to analyze all possible trading paths between coins. By evaluating forward and reverse exchange paths, the system identifies potential **arbitrage opportunities** caused by exchange inefficiencies.

This project demonstrates skills in **API integration**, **graph-based modeling**, **data transformation**, and **algorithmic analysis** common components in data engineering and quantitative analytics workflows.

---

## Features

- Pulls live crypto exchange rates using the CoinGecko REST API  
- Converts API response into a **directed, weighted graph**  
- Uses NetworkX to explore **all simple currency paths**  
- Calculates forward and reverse conversion weights  
- Determines arbitrage factor for each path  
- Identifies the **most profitable** and **least efficient** cycles  
- Clean, extensible Python code suitable for production-style pipelines  

---
