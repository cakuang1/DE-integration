# DE-integration

<h1>Introduction </h1>

Pipeline that extracts data from <a href = 'https://eodhistoricaldata.com/financial-apis/insider-transactions-api/'>EOHDH insider transaction API endpoint</a>, 

<h1>Purpose</h1>
  I want to compare who the best traders are, and answer the ultimate question 'Can you beat the market if you follow the stock purchases made by company insiders?'


<h1>Architecture</h1>


DAG Tasks:

1. Scrape data from [Crinacle's](https://crinacle.com/) website to generate bronze data.
2. Load bronze data to [AWS S3](https://aws.amazon.com/s3/).
3. Initial data parsing and validation through [Pydantic](https://github.com/pydantic/pydantic) to generate silver data.
4. Load silver data to [AWS S3](https://aws.amazon.com/s3/).
5. Load silver data to [AWS Redshift](https://aws.amazon.com/redshift/).
6. Load silver data to [AWS RDS](https://aws.amazon.com/rds/) for future projects.
7. and 8. Transform and test data through [dbt](https://docs.getdbt.com/) in the warehouse.
<h1>Architecture</h1>
<h1>Architecture</h1>
