# file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello.txt","w")
# # file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello.txt","a")
# # file.write("I Love Python")
# file.write("I Love JavaScript") # It will overwrite previous content.
# file.write("\nI Love C++") # Now It will append it.
# file.close()

file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello.txt","r")
print(file.read())
file.close()
