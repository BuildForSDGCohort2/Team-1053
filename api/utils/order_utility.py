def get_order_summary(data):
    orders = len(data)
    if orders == 0:
        return data

    total_cost = 0
    cancelled = 0
    delivered = 0

    for order in orders:
        total_cost += order.cost
        if order.status == 'Cancelled':
            cancelled += 1
        if order.status == 'Delivered':
            delivered += 1
    average_cost = total_cost/orders

    return {
        'total_cost': total_cost,
        'average_cost': average_cost,
        'cancelled': cancelled,
        'delivered': delivered
    }
