# 1 - Apple Stock
# INPUT: List of integers.
# 	Indecies: time in min past 9:30a
# 	Values: price of stock at that time
# OUTPUT: Integer
# 	Value: Max profit.
# RUNTIME: 0(n)

def get_max_profit(stock_prices_yesterday):
	"""
		>>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
		>>> get_max_profit(stock_prices_yesterday)
		6
		>>> stock_prices_yesterday = []
		>>> get_max_profit(stock_prices_yesterday)
		0
		>>> stock_prices_yesterday = [10]
		>>> get_max_profit(stock_prices_yesterday)
		0
		>>> stock_prices_yesterday = [10, 9]
		>>> get_max_profit(stock_prices_yesterday)
		-1
	"""
	if len(stock_prices_yesterday) < 2:
		return 0

	min_price = stock_prices_yesterday[0]
	max_profit = float('-inf')

	for price in stock_prices_yesterday[1:]:  # price:  	 7,  5, 8, 11, 9 
		profit = price - min_price			  # profit: 	-3, -2, 3,  6, 4
		max_profit = max(profit, max_profit)  # max_profit: -3, -2, 3,  6, 6
		min_price = min(min_price, price)	  # min_price:	 7,  5, 5,  5, 5

	return max_profit



if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"