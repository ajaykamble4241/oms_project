WITH orders_cte AS (
    SELECT
        order_id,
        customer_id,
        order_date,
        status
    FROM
        {{ source('oms', 'ordr') }} 
),

order_items_agg AS (
    SELECT
        order_id,
        SUM(quantity) AS total_quantity
    FROM
        {{ source('oms', 'ordritms') }} 
    GROUP BY
        order_id
)

SELECT
    o.order_id,
    o.customer_id,
    o.order_date,
    o.status,
    oi.total_quantity
FROM
    orders_cte AS o
LEFT JOIN
    order_items_agg AS oi
ON
    o.order_id = oi.order_id



