import sys

# Access individual arguments
if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    print(f"Argument 1: {arg1}")
else:
    print("No arguments provided.")
