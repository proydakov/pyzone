from my_cxx_module import module as my_cxx_module

# Call the CXX function
result = my_cxx_module.sum_as_string(512, 1000) 
print(f"Result: {result}, Type: {type(result)}")

greeting = my_cxx_module.greet("World")
print(greeting)

my_cxx_module.say("🐍 🐍🐍 🐍🐍🐍 🐍🐍🐍🐍 🐍🐍🐍🐍🐍")

b = b"wwww"
my_cxx_module.handle_bytes(b)

ba = bytearray(16)
my_cxx_module.handle_bytearray(ba)
