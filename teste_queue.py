from queue import Queue

# teste fila comeca vazia
fila = Queue()
assert fila.is_empty() == True

# teste enqueue funciona
fila.enqueue(10)
fila.enqueue(20)
assert fila.size() == 2

# teste ordem certa (FIFO)
fila2 = Queue(3)
fila2.enqueue("a")
fila2.enqueue("b")
fila2.dequeue()
assert fila2.size() == 1

# teste peek nao remove
fila3 = Queue()
fila3.enqueue(99)
fila3.peek()
assert fila3.size() == 1

# teste clear esvazia
fila4 = Queue()
fila4.enqueue(1)
fila4.enqueue(2)
fila4.clear()
assert fila4.is_empty() == True

