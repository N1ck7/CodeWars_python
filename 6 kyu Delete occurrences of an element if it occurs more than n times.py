def delete_nth(order,max_e):
    
    for num in order:
        order.reverse()
        while order.count(num) > max_e:            
            order.remove(num)
        order.reverse()
    return order
