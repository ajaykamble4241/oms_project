
  create or replace   view OMS_DATABASE.OMS_SCHEMA.customer_dim
  
   as (
    -- models/customer.sql
SELECT
    customer_id,
    name,
    email
FROM
    OMS_DATABASE.OMS_SCHEMA.customer
  );

