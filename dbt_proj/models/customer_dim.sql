-- models/customer.sql
SELECT
    customer_id,
    name,
    email
FROM
    {{ source('oms', 'cust') }}

