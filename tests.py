from functions.write_file import write_file
from functions.run_python_file import run_python_file


def test():
    # Test write_file function
    print("=== Testing write_file ===")
    result = write_file("calculator", "calculator/lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file("calculator", "calculator/pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

    # Test run_python_file function
    print("\n=== Testing run_python_file ===")
    
    # Test 1: Run calculator main.py without arguments (should show usage)
    print("Test 1: run_python_file('calculator', 'main.py')")
    result = run_python_file("calculator", "main.py")
    print(result)
    print()

    # Test 2: Run calculator with expression "3 + 5"
    print("Test 2: run_python_file('calculator', 'main.py', ['3 + 5'])")
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)
    print()

    # Test 3: Run tests.py file
    print("Test 3: run_python_file('calculator', 'tests.py')")
    result = run_python_file("calculator", "tests.py")
    print(result)
    print()

    # Test 4: Try to run file outside working directory (should error)
    print("Test 4: run_python_file('calculator', '../main.py')")
    result = run_python_file("calculator", "../main.py")
    print(result)
    print()

    # Test 5: Try to run non-existent file (should error)
    print("Test 5: run_python_file('calculator', 'nonexistent.py')")
    result = run_python_file("calculator", "nonexistent.py")
    print(result)


if __name__ == "__main__":
    test()
