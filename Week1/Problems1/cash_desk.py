class CashDesk:

	def __init__(self):
		self.money = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}

	def take_money(self, money):
		for m in money:
			self.money[m] += money[m] 

	def print_cash(self):
		print(self.money)

	def total(self):
		sum = 0
		for m in self.money:
			sum += int(m) * self.money[m]
		return sum

	#def can_withdraw_money(self, amound_of_money):
	#	if amound_of_money % 10


def main():
	my_cash_desk = CashDesk()
	my_cash_desk.take_money({1:4, 50:1, 20:1})
	my_cash_desk.print_cash()
	print("pishka")
	print(my_cash_desk.total())
	print(can_withdraw_money(74))

if __name__ == '__main__':
	main()