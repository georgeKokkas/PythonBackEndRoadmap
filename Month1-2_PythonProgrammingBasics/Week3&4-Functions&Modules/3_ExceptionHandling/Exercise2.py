# Create a function that reads a file and handles the exception if the file does not exist.

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found!"
    
file_path = "C:/Users/geoko/Desktop/PythonBackEndRoadmap/Week3&4-Functions&Modules/3_ExceptionHandling/example.txt"
print(read_file(file_path)) # Output: File content or "File not found!"