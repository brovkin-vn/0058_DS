# def check_server(mode):
#     if mode == "memory":
#         return "Memory is ok"
#     elif mode == "connection":
#         return "Connection is ok"
#     else:
#         raise ValueError("Incorrect mode")

# print(check_server("asf"))        

def safe_sum(a, b):
    try:
        return a + b
    except TypeError:
        print(f"Can't sum {a} and {b}")
        return 0

print(safe_sum(1, 2))
# 3

print(safe_sum(5, 'a'))
# => Can't sum 5 and a
# 0 
      