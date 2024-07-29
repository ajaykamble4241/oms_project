
  create or replace   view OMS_DATABASE.OMS_SCHEMA.order_items_dim
  
   as (
    -- models/order_items.sql
SELECT
    item_id,
    order_id,
    product_name,
    quantity,
    price
FROM
    OMS_DATABASE.OMS_SCHEMA.orderitem
  );

