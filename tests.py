
# from functions.get_file_content import get_files_content
# from functions.write_file import write_file
# from functions.run_python_file import run_python_file

# def tests():
    # #  Run get_files_info("calculator", ".")
   
    # result =  get_files_content("calculator", "main.py")
    # print(f"calculator/main.py: {result}")
    
    # result = get_files_content("calculator", "pkg/calculator.py")
    # print(f"calculator, pkg/calculator.py:  {result}")
    
    # result = get_files_content("calculator", "/bin/cat") 
    # print(f"this should return an error string.....Result{result}")

    # # write file tests
    
    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print(result)
    
    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print(result)
    
    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print(result)
    
    # result = run_python_file("calculator", "main.py")
    # print(result)
    
    # result = run_python_file("calculator", "tests.py")
    # print(result)
    
    # result = run_python_file("calculator", "../main.py") 
    # print(result)#this should return an error 
    
    # result = run_python_file("calculator", "nonexistent.py") 
    # print(result)#this should return an error
    
    # result = run_python_file("calculator", "new.go") 
    # print(result)#this should return an error
    
# if __name__ == "__main__":
#     tests()