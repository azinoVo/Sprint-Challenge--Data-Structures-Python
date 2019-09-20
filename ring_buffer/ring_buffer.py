class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # If storage length is less than total capacity, just insert a new item at that index
    # length of 0 would insert a fresh value at self.storage[0] and so forth
    if len(self.storage) < self.capacity:
      self.storage[len(self.storage)] = item
    # When storage and and capacity are equal, we need to start removing old elements
    elif len(self.storage) == self.capacity:
      # The current is used to keep track of where the oldest element is in terms of index
      # If current is less than capacity, replace current with the fresh values and increment to the next oldest
      if self.current < self.capacity:
        self.storage[self.current] = item
        self.current += 1
        return self.storage
      # If current is equal to capacity, it means the last item has already been updated since lists start at index zero
      # We start over at index zero, replace the item and increment accordingly
      elif self.current == self.capacity:
        self.current = 0
        self.storage[self.current] = item
        self.current += 1
        return self.storage

  def get(self):
    # Loops through the elements of the list and return anything that's not None
    new_array = []
    for x in range(0, len(self.storage)):
      if self.storage[x] != None:
        new_array.append(self.storage[x])
    return new_array

buffer = RingBuffer(7)
buffer.append("a")
buffer.append("b")
buffer.append("c")
# d and e are both inserted at index 0
buffer.append("d")
buffer.append("e")
buffer.append("f")
# buffer.append("g")
# buffer.append("h")
# buffer.append("i")
print("GETTING", buffer.get())
print(buffer.storage)





