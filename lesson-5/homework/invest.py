def invest(amount, rate, years):
    for i in range(1,years+1):
         x=amount*pow((1+rate),i)
         print(f"year {i}: {x:.2f}")
invest(100, 0.05, 4)