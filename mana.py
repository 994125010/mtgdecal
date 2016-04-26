import re, sys

hybrid2symb = re.compile('\\(([WUBRGSCP]+|\d+)/')
mana_hybrid = re.compile('\\([WUBRGSCP\d]/[WUBRGSC]+\\)')
mana_single = re.compile('^([XYZ]*)(\d*)(W*)(U*)(B*)(R*)(G*)(S*)(C*)')

def CMC(s):
	""" Mana costs must be in the following format
		XX11WUBRGSCC(P/W)(WUBRG/UBRG)(4/W)

	>>> CMC('XX11WUBRGSCC(P/W)(U/G)(2/C)')
	23
	"""
	singles = map(len_or_int, mana_single.match(s).groups()[1:])
	hybrids = map(lambda h: len_or_int(hybrid2symb.match(h).group(1)), mana_hybrid.findall(s))
	return sum(singles) + sum(hybrids)

def len_or_int(s):
	try:
		return int(s)
	except ValueError:
		return len(s)

def deck_CMC(d):
	""" d is a textfile that contains tab delimited lines of the form
		card_name	mana_cost
	"""
	total_cmc = {}
	f = open(d, 'r')
	for line in f.readlines():
		mana_cost = line.split('\t')[1]
		card_cmc = CMC(mana_cost)
		if card_cmc not in total_cmc:
			total_cmc[card_cmc] = 0
		total_cmc[card_cmc] += 1
	return total_cmc