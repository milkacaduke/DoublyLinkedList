
class LLNode(object):
	def __init__(self, data='none'):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList(object):
	def __init__(self):
		self.head = None

	def insert(self, data):
		if data is None:
			print("Data is null")
			return
		self.insert_front(data)

	def insert_front(self, data):
		if data is None:
			print("Data is null")
			return

		if self.head is None:
			new_node = LLNode(data)
			self.head = new_node
		else:
			new_node = LLNode(data)
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def insert_after_node(self, node, data):
		if node is None:
			return

		if self.head is None:
			return

		cur_node = self.head
		while cur_node:
			if cur_node == node:
				new_node = LLNode(data)
				new_node.next = cur_node.next
				new_node.prev = cur_node
				cur_node.next = new_node
				return
			cur_node = cur_node.next

	def insert_after_data(self, target_data, data):
		if target_data is None:
			return

		if self.head is None:
			return

		cur_node = self.head
		while cur_node:
			if cur_node.data == target_data:
				new_node = LLNode(data)
				new_node.next = cur_node.next
				new_node.prev = cur_node
				cur_node.next = new_node
				if new_node.next is not None:
					new_node.next.prev = new_node
				return
			cur_node = cur_node.next


	def delete_front(self):
		if self.head is None:
			return

		if self.head.next is None:
			self.head = None
			return

		temp_node = self.head
		self.head = self.head.next
		self.head.prev = None
		return temp_node


	def delete_back(self):
		if self.head is None:
			return

		if self.head.next is None:
			self.head = None
			return

		cur_node = self.head
		while cur_node.next:
			cur_node = cur_node.next
		temp_node = cur_node
		cur_node.prev.next = None
		temp_node.prev = None # optional
		return temp_node



	def print_all(self):
		if self.head is None:
			return

		print("")
		print("[head]")
		print("   v")
		print("   ", end="")
		cur_node = self.head
		while cur_node:
			if cur_node.next is None:
				print(cur_node.data + "(" + cur_node.prev.data + ")")	
			else:
				if cur_node == self.head:
					print(cur_node.data + " -> ", end='')
				else:
					print(cur_node.data +"("+ cur_node.prev.data +")"+ " -> ", end='')
			cur_node = cur_node.next



# main stuff
# dll = DoublyLinkedList()
# dll.insert("A")
# dll.insert("B")
# dll.insert("C")

# dll.insert_after_data("B", "B1")
# dll.insert_after_data("A", "A1")
# dll.insert_after_data("C", "C1")
# dll.insert_after_data("A1", "A2")
# dll.print_all()

# n1 = dll.delete_front()
# dll.print_all()
# n2 = dll.delete_back()
# dll.print_all()
# print(n1.data)
# print(n2.data)
# print(n2.data)