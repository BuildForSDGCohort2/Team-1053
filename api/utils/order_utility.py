import json


def get_order_summary(data):
    all_orders = len(data)
    data = json.loads(json.dumps(data))
    total_cost = 0
    cancelled = []
    delivered = []
    new = []
    on_hold = []
    approved = []

    for order in data:
        total_cost += order.get('grand_total')
        if order.get('status') == 'Cancelled':
            cancelled.append(order)
        if order.get('status') == 'Delivered':
            delivered.append(order)
        if order.get('status') == 'New':
            new.append(order)
        if order.get('status') == 'On Hold':
            on_hold.append(order)
        if order.get('status') == 'Approved':
            approved.append(order)
    average_cost = total_cost/all_orders

    return {
        'total_cost': total_cost,
        'average_cost': average_cost,
        'new': new,
        'on_hold': on_hold,
        'approved': approved,
        'cancelled': cancelled,
        'delivered': delivered,
        'orders': all_orders
    }
