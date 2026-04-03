import my_rust_module

# Call the Rust function
result = my_rust_module.sum_as_string(512, 1000) 
print(f"Result: {result}, Type: {type(result)}")

greeting = my_rust_module.greet("World")
print(greeting)

my_rust_module.say("🐍")

b = b"wwww"
my_rust_module.handle_bytes(b)

ba = bytearray(16)
my_rust_module.handle_bytearray(ba)
