import my_rust_module

# Call the Rust function
result = my_rust_module.sum_as_string(512, 1000) 
print(f"Result: {result}, Type: {type(result)}")

greeting = my_rust_module.greet("World")
print(greeting)

