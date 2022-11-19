"""
	Weitere Tests fuer die main.py!
"""
d4 = DataSet()
d4.set_iteration(sort=False)
d4 += DataSetItem("A", 1, "a")
d4 += DataSetItem("C", 3, "c")
d4 += DataSetItem("B", 2, "b")
d4 += DataSetItem("D", 4, "d")

d5 = DataSet()
d5.set_iteration(sort=False)
d5 += DataSetItem("C", 5, "c")
d5 += DataSetItem("E", 7, "e")
d5 += DataSetItem("D", 6, "d")
d5 += DataSetItem("F", 8, "f")
d5 += DataSetItem("G", 9, "g")

# Beinhaltet?
if not "G" in d5:
	code_fail()
if "G" in d4:
	code_fail()

# Loeschen
del d5["G"]
if "G" in d5:
	code_fail()
for i, l in zip(d5, ["c", "e", "d", "f"]):
	if i.content != l:
		code_fail()

# Schnitt 
d_intersect = d4 & d5 
if len(d_intersect) != 2:
	code_fail()

d_intersect.set_iteration(sort=True)
for i, l in zip(d_intersect, [3, 4]):
	if i.id != l:
		code_fail()

# Vereinigung
d_union = d4 | d5 
if len(d_union) != 6:
	code_fail()

d_union.set_iteration(sort=True)
for i, l in zip(d_union, [1, 2, 5, 6, 7, 8]):
	if i.id != l:
		code_fail()
