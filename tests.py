from functions.get_file_content import get_file_content

def run_tests():
    print("Test 'main.py'")
    print(get_file_content("calculator", "main.py"))

    print("Test 'pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("Test '/bin/cat'")
    print(get_file_content("calculator", "/bin/cat'"))

    print("Test 'pkg/doesn_not_exist.py'")
    print(get_file_content("calculator", "pkg/doesn_not_exist.py"))

if __name__ == "__main__":
    run_tests()