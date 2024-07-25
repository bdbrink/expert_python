from graphlib import TopologicalSorter

table_ref = {
    "customers": set(),
    "accounts": {"customers"},
    "products": set(),
    "orders": {"accounts", "customers"},
    "order_products": {"orders", "products"}
}

sorter = TopologicalSorter(table_ref)
print(list(sorter.static_order()))