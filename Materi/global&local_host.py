x = 1
def fungsi():
    # x = 2 # --> local host >> mengubah nilai variabel hanya di dalam fungsi
    # global x # --> global >> mengubah nilai variabel secara global
    # x = 10
    print(x)

fungsi()
print(x)

# tidak berlaku di if dan for statement
