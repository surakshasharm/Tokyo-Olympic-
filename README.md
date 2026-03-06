# Tokyo Olympics Data Engineering Pipeline (Azure)

## Project Overview
This project demonstrates an end-to-end Data Engineering pipeline using the Tokyo Olympics dataset. 
The pipeline ingests raw data, stores it in a data lake, performs transformations, and prepares it 
for analytics and visualization.

## Architecture
GitHub CSV -> Azure Data Factory -> Azure Data Lake Storage -> Azure Databricks -> Azure Synapse / SQL -> Power BI

## Dataset
The dataset includes:
- Athletes
- Coaches
- Teams
- Entries by Gender
- Medals

## Technologies Used
- Python
- SQL
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks (PySpark)
- Azure Synapse Analytics
- Power BI
- Git

## Pipeline Steps
1. Extract raw CSV data from GitHub.
2. Load data into Azure Data Lake (Raw Layer).
3. Transform and clean data using PySpark in Azure Databricks.
4. Store processed data in the Curated Layer.
5. Query processed data using SQL.
6. Create dashboards using Power BI.

## Key Features
- End-to-end ETL pipeline
- Data quality checks
- Cloud-based data processing
- Analytics-ready datasets

## Future Improvements
- Real-time ingestion using Kafka
- Data quality monitoring
- Automated pipeline scheduling
