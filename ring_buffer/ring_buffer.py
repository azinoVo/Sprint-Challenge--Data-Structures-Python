class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if len(self.storage) < self.capacity:
      self.storage[len(self.storage)] = item
    elif len(self.storage) == self.capacity:
      if self.current < self.capacity:
        self.storage[self.current] = item
        self.current += 1
        return self.storage
      elif self.current == self.capacity:
        self.current = 0
        self.storage[self.current] = item
        self.current += 1
        return self.storage

  def get(self):
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





