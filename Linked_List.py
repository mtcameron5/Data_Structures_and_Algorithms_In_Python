class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None 


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head 

	def append(self, new_element):
		current = self.head 
		if self.head:
			while current.next:
				current = current.next 
			current.next = new_element 
		else:
			self.head = new_element


	def get_position(self, position):
		current = self.head 
		counter = 1
		if position < 1:
			return None
		while current and counter <= position:
			if counter == position:
				return current 
			current = current.next 
			counter += 1
		return None 


	def delete(self, value):
		current = self.head 
		previous = None 
		while current.value != value and current.next:
			previous = current 
			current = current.next 
		if current.value == value:
			if previous:
				previous.next = current.next 
			else:
				self.head = current.next 


	def insert(self, new_element, position):
		counter = 1
		current = self.head 
		if position > 1:
			while current and counter < position:
				if counter == position - 1:
					new_element.next = current.next 
					print new_element.next.value
					current.next = new_element 
				current = current.next 
				counter += 1
		elif position == 1:
			new_element.next = self.head 
			self.head = new_element 

	def insert(self, new_element, position):
		counter = 1 
		current = self.head 
		if position > 1:
			while current and counter < position:
				if counter == position - 1:
					new_element.next = current.next 
					current.next = new_element 
				current = current.next 
				counter += 1 
		elif position == 1:
			new_element.next = self.head 
			self.head = new_element 


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(14)
e6 = Element(20)
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.insert(e6, 4)

print ll.get_position(5).value
