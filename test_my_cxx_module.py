from my_cxx_module import module as my_cxx_module

# Call the CXX function
result = my_cxx_module.sum_as_string(512, 1000) 
print(f"Result: {result}, Type: {type(result)}")

greeting = my_cxx_module.greet("World")
print(greeting)

