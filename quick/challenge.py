def Solution(paths: list[list[str]]) -> str:
	ins = set()
	outs = set()
	for orig, dest in paths:
		ins.add(orig)
		outs.add(dest)

	return [o for o in outs if o not in ins][0]


paths = [
	["London", "New York"],
	["New York", "Lima"],
	["Lima", "Sao Paulo"]
]
dest = Solution(paths)
print(dest)


def matrix_validity(matrix: list[list[int]]) -> bool:
	n = len(matrix)
	# check rows
	for row in matrix:
		if sorted(row) != [*range(1, n+1, 1)]:
			return False

	# check columns
	for j in range(n):
		col = set()
		for row in matrix:
			col.add(row[j])

		if sorted(col) != [*range(1, n+1, 1)]:
			return False
	
	return True


matrix = [[1,2,3], [3,1,2],[2,3,1]]
v = matrix_validity(matrix)
print(v)
