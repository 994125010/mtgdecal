import sys

def IRR(sell, buy, costs, duration, period):
	return (sell/(buy+costs))**(duration/period)-1

def p1():
	with open(sys.argv[0], 'r') as f:
		print("### 1) IRR FUNCTION:\n")
		for line in f.readlines()[2:4]:
			print(line, end='')
		print("\nIRR(64, 3, 1, 10, 40): {:.2f}%".format(100*IRR(64, 3, 1, 10, 40)))

p1()

def p2():
	print("\n\n### 2) Intrepid Grad Student")
	initial_c = 148.41 * 12 * 4
	grading = 12 * 12 * 4
	shipping = 2.5 * 48
	sold_p = 170.98 * 12 * 4 * 1.1
	tcg_cut = 0.08 * sold_p

	irr = IRR(sold_p-tcg_cut-shipping, initial_c, grading, 2, 2)
	print("\nIRR (over 2 years): {:.2f}%".format(100*irr))
	wage = irr * initial_c / (48*.5)
	print("Hourly Wage: ${:.2f}".format(wage))

p2()

import numpy as np

def p3():
	print("\n\n### 3) Volatility\n")
	with open('bayou.txt', 'r') as f:
		initial_c = 148.41 * 12 * 4
		irrs = []
		max_irr = -float('inf')
		min_irr = float('inf')
		max_irr_date = None
		min_irr_date = None
		for days, line in enumerate(f.readlines()):
			date, price = line.split()
			price = float(price)
			sold_p = 48 * price
			irr = IRR(sold_p, initial_c, 0, 1, 1)
			if irr > max_irr:
				max_irr_date = date
				max_irr = irr
			if irr < min_irr:
				min_irr_date = date
				min_irr = irr
			irrs.append(irr)
		print("Lowest:  {:.2f}% @ {}".format(min_irr*100, min_irr_date))
		print("Highest: {:.2f}% @ {}".format(max_irr*100, max_irr_date))
		neg_irrs = [irr for irr in irrs if irr < 0]
		print("P(losing money): {:.2f}%".format(len(neg_irrs)/len(irrs)*100))
		vol = np.std(irrs)
		print("Volatility: {:.2f}%".format(vol*100))
p3()

def p4():
	print("\n\n### 4) Five Thousand MTG Investment")
	reasons = """Spend $2,000 on two EDH decks
	Because I want to try the format

Spend $1,000 on OGW booster boxes
	for pretty Expeditions
	and the enjoyment of opening boosters

Spend $500 on getting into Standard
	Small pool formats are where I can analyze effectively
	Seems like a popular format to play
	Doesn't require a huge buy-in

Spend $1,500 on buying "staples"/blue-chip cards that are useful for various decks.
	Probably just one playset of each
	Semi-investment (cards will never go bad)
	more collector's sentiment (I want a pretty goyf, sculptor, etc.)
	Nice to help realise deck concepts
	Nice to remember mechanics I like
	Nice to remember art I like
"""
	print(reasons)

p4()