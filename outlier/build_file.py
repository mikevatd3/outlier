import pandas as pd
from sqlalchemy import text

from connection import tns_engine


stmt = text(
    """
    select clean_taxpayer(taxpayer_1), 
           clean_address(taxpayer_street), 
           taxpayer_zip, 
           assessed_value,
           total_square_footage,
           tax_status,
           num_bldgs = 0 as empty_lot,
           homestead_pre = 100 as owner_occupied,
           substring(property_class::text from 1 for 1) as super_class
    from assessors_2024
    where tax_status not like 'EXEMPT%'
    and assessed_value > 0
    and total_square_footage > 0;
    """
)


with tns_engine.connect() as db:
    df = pd.read_sql(stmt, db)

df.to_parquet("temp_parcels.gzip")


