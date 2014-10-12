fruit = ["Apple", "Apricot", "Avocado", "Breadfruit", "Bilberry", "Banana", "Blackberry", "Blackcurrant", "Blueberry", "Boysenberry", "Blood Orange", "Clementine", "Currant", "Cloudberry", "Cucumber", "Cherimoya", "Cherry", "Clementine", "Coconut", "Cranberry", "Canteloupe", "Durian", "Damson", "Date", "Dragonfruit", "Eggplant", "Elderberry", "Feijoa", "Fig", "Goji berry", "Gooseberry", "Grapefruit", "Grape", "Guava", "Huckleberry", "Honeydew", "Jackfruit", "Jambul", "Jujube", "Kiwi", "Kumquat", "Lemon", "Lime", "Loquat", "Lychee", "Loganberry", "Mandarin", "Mango", "Mangosteen", "Melon", "Marion berry", "Miracle fruit", "Mulberry", "Nectarine", "Nut", "Olive", "Orange", "Papaya", "Peach", "Pear", "Persimmon", "Pineapple", "Plum", "Pomegranate", "Passionfruit", "Pepper", "Physalis", "Pomelo", "Purple Mangosteen", "Quince", "Raspberry", "Rambutan", "Redcurrant", "Salal berry", "Salmon berry", "Star fruit", "Satsuma", "Sharon Fruit", "Strawberry", "Tamarillo", "Tomato", "Tangerine", "Ugli Fruit", "Watermelon"]

def splitInto(n, s):
	while len(s) % n != 0:
		s += "a"
	tr = []
	while s:
		tr.append(s[0:n])
		s = s[n:]
	return tr

def letterTOnumber(c):
	return "abcdefghijklmnopqrstuvwxyz".index(c.lower())

def encode(s):
	groups = splitInto(3, s)
	results = []
	for group in groups:
		nums = map(letterTOnumber, group)
		a, b, c = nums[2] % 3, (nums[2] / 3) % 3, nums[2] / 9
		f1 = fruit[nums[0] + 26 * a]
		f2 = fruit[nums[1] + 26 * b]
		tone = "(high)" if c == 1 else "(low)"
		complement = "(high)" if nums[0] % 2 == 0 else "(low)"
		results.append(" ".join([f1, tone, f2, complement]))
	print " . ".join(results)

while 1:
	encode(raw_input("Input an english word: "))
