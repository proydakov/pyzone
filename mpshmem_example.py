import time
from multiprocessing import shared_memory

memory = shared_memory.SharedMemory(name="ishared_memory", create=True, size=16)
word = "hello, world!\n"
memory.buf[:len(word)] = word.encode("utf-8")

time.sleep(32)

memory.close()
memory.unlink()

