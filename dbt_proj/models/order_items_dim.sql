-- models/order_items.sql
SELECT
    item_id,
    order_id,
    product_name,
    quantity,
    price
FROM
    {{ source('oms', 'ordritms') }}  