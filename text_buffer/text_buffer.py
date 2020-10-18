

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class TextBuffer:
	def __init__(self):
		self.storage = DoublyLinkedList()

	def __str__(self):
		pass

	def join(self, other_buffer):
		pass

	def append(self, string_to_add):
		self.storage.add_to_tail(string_to_add)

	def prepend(self, string_to_add):
		self.storage.add_to_head(string_to_add)

	def delete_from_front(self):
		pass

	def delete_from_back(self):
		pass

	def find_text(self, text_to_find):
		pass

# add to the back of a text buffer
	# add to the front of a text buffer
	# delete to

	# grab input
	# display output
	# insert string
	# add to front buffer

	# add to back of a text buffer

	# join text buffers together


	# << array vs dll >>
	# ** [Array]:
	# add to back O(1)
	# add to front 0(n)
	# delete from back O(1)
	# delete from front 0(n)
	# join text buffers together 0(n)
	# __str__, to print what's inside O(n)

	# ** [DLL]: (Better)
	# add to back O(1)
	# add to front 0(1)
	# delete from back O(1)
	# delete from front 0(1)
	# join text buffers together 0(1)
	# __str__, to print what's inside O(n)