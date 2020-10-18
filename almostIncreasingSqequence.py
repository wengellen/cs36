# O(n)
def find_odd_elem_out(sequence):
	odd_elem_index = -1

	for i in range(len(sequence) - 1):
		if sequence[i] >= sequence[i + 1]:
			odd_elem_index = i
			break

	return odd_elem_index


# O(5 * n) ~ O(n)
def almostIncreasingSequence(sequence):
	# what's the best runtime we could possibly get?
	# O(c * n)

	# finding the odd-elem-out
	# go through our input and see if we can find an odd-elem-out
	odd_elem_out = find_odd_elem_out(sequence)  # O(n)

	if odd_elem_out == -1:
		return True

	# remove that odd-elem-out
	removed_seq = sequence[:odd_elem_out] + sequence[odd_elem_out + 1:]  # O(n)

	if find_odd_elem_out(removed_seq) == -1:  # O(n)
		return True

	# print(removed_seq)

	# remove the odd-elem-out + 1
	removed_seq = sequence[:odd_elem_out + 1] + sequence[odd_elem_out + 2:]  # O(n)

	# print(removed_seq)

	if find_odd_elem_out(removed_seq) == -1:  # O(n)
		return True

	return False