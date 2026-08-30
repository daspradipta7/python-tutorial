daily_sales = [10, 15, 2, 4, 3, 11]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(f"Total sale > 5: {total_cups}")