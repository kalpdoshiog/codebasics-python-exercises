# file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello.txt","w")
# # file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello.txt","a")
# # file.write("I Love Python")
# file.write("I Love JavaScript") # It will overwrite previous content.
# file.write("\nI Love C++") # Now It will append it.
# file.close()

file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello.txt","r")
file_out = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello_word_count.txt","w")
# print(file.read())
# file.close()

for line in file:
    token = line.split(" ")
    # print(str(token))
    file_out.write("Wordcount : "+ str(len(token)) + ",  " + line )
    # print(line)

file.close()