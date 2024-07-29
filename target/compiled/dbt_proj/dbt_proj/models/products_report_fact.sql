-- models/products_report.sql



WITH base AS (
    SELECT
        p.product_id,
        p.product_name,
        oi.quantity,
        oi.price
    FROM
        OMS_DATABASE.OMS_SCHEMA.products_dim p
    JOIN
        OMS_DATABASE.OMS_SCHEMA.order_items_dim oi ON p.product_name = oi.product_name
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


  WHERE product_id > (SELECT MAX(product_id) FROM OMS_DATABASE.OMS_SCHEMA.products_report_fact)
