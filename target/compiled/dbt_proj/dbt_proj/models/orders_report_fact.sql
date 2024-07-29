-- models/orders_report.sql



WITH base AS (
    SELECT
        o.order_id,
        o.customer_id,
        o.order_date,
        o.status,
        oi.quantity,
        oi.price
    FROM
        OMS_DATABASE.OMS_SCHEMA.orders_dim o
    JOIN
        OMS_DATABASE.OMS_SCHEMA.order_items_dim oi ON o.order_id = oi.order_id
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


  WHERE order_date > (SELECT MAX(order_date) FROM OMS_DATABASE.OMS_SCHEMA.orders_report_fact)
