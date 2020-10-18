class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)

class LinkedList:
	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None

	def add_to_tail(self, value):
		new_node = Node(value)
		self.size += 1
		if self.head is None and self.tail is None:
			self.head = new_node
			self.tail = new_node
		else:
			current_tail = self.tail
			current_tail.next = new_node
			self.tail = new_node

	def remove_head(self):
		if self.head is None and self.tail is None:
			return
		elif self.head == self.tail:
			current_head = self.head
			self.head = None
			self.tail = None
			return current_head.value
		else:
			current_head = self.head
			self.head = current_head.next
			return current_head.value

	def contains(self, value):
		current_node = self.head
		while current_node:
			if current_node.value == value:
				return True
			current_node = current_node.next

		return False

	def get_max(self):
		if self.head is None and self.tail is None:
			return

		current_node = self.head
		max_value = current_node.value

		while current_node:
			if max_value < current_node.value:
				max_value = current_node.value
			current_node = current_node.next

		return max_value


	def __str__(self):
		output = ''
		current_node = self.head
		while current_node:
			output += str(current_node)
			output += ' => '
			current_node = current_node.next
		return output


# li = LinkedList()
#
# li.add_to_tail(10)
# li.add_to_tail(20)
# removed = li.remove_head()
# print(f'removed: {removed}')
# print(li.contains(10))
# print(li)
#
# li.remove_head()
# print(li.contains(20))
#
# li.add_to_tail(10)
# li.remove_head()
# print(li.contains(10))
