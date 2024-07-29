-- models/products.sql
SELECT
    product_id,
    product_name,
    price
FROM
    {{ source('oms', 'prod') }}
