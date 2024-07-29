-- models/products_report.sql

{{ config(
    materialized='incremental',
    unique_key='product_id'
) }}

WITH base AS (
    SELECT
        p.product_id,
        p.product_name,
        oi.quantity,
        oi.price
    FROM
        {{ ref('products_dim') }} p
    JOIN
        {{ ref('order_items_dim') }} oi ON p.product_name = oi.product_name
)

SELECT
    product_id,
    product_name,
    SUM(quantity) AS total_quantity_sold,
    SUM(quantity * price) AS total_revenue
FROM
    base
GROUP BY
    product_id, product_name 

{% if is_incremental() %}
  WHERE product_id > (SELECT MAX(product_id) FROM {{ this }})
{% endif %}