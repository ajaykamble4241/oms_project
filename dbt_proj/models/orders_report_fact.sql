-- models/orders_report.sql

{{ config(
    materialized='incremental',
    unique_key='order_id'
) }}

WITH base AS (
    SELECT
        o.order_id,
        o.customer_id,
        o.order_date,
        o.status,
        oi.quantity,
        oi.price
    FROM
        {{ ref('orders_dim') }} o
    JOIN
        {{ ref('order_items_dim') }} oi ON o.order_id = oi.order_id
)

SELECT
    order_id,
    customer_id,
    order_date,
    status,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_amount
FROM
    base
GROUP BY
    order_id, customer_id, order_date, status

{% if is_incremental() %}
  WHERE order_date > (SELECT MAX(order_date) FROM {{ this }})
{% endif %}
