
from functions.get_file_content import get_files_content
from functions.write_file import write_file
def tests():
    # #  Run get_files_info("calculator", ".")
   
    # result =  get_files_content("calculator", "main.py")
    # print(f"calculator/main.py: {result}")
    
    # result = get_files_content("calculator", "pkg/calculator.py")
    # print(f"calculator, pkg/calculator.py:  {result}")
    
    # result = get_files_content("calculator", "/bin/cat") 
    # print(f"this should return an error string.....Result{result}")

    # # write file tests
    
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)
    
if __name__ == "__main__":
    tests()