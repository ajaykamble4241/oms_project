
  create or replace   view OMS_DATABASE.OMS_SCHEMA.products_dim
  
   as (
    -- models/products.sql
SELECT
    product_id,
    product_name,
    price
FROM
    OMS_DATABASE.OMS_SCHEMA.product
  );

