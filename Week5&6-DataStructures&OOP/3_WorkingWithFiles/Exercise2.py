# Write a program to create a new file and write some text to it, then read the content back.

def write_and_read_file(filename, text):
    try:
        with open(filename, 'w') as file:
            file.write(text)

        with open(filename, 'r') as file:
            content = file.read()

        return content
    
    except Exception as e:
        return str(e)

filename = "new_file.txt"

file_path = "C:/Users/geoko/Desktop/PythonBackEndRoadmap/Week5&6-DataStructures&OOP/3_WorkingWithFiles/new_file.txt"

text = "Hello, this is a test text!"

content = write_and_read_file(file_path, text)

print(content)