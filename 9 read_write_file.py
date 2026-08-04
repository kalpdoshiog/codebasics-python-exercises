# file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello.txt","w")
# # file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello.txt","a")
# # file.write("I Love Python")
# file.write("I Love JavaScript") # It will overwrite previous content.
# file.write("\nI Love C++") # Now It will append it.
# file.close()

# file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello.txt","r")
# file_out = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello_word_count.txt","w")
# print(file.read())
# file.close()

# for line in file:
    # token = line.split(" ")
    # print(str(token))
    # file_out.write("Wordcount : "+ str(len(token)) + ",  " + line )
    # print(line)

# file.close()

# with open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_read_write_file\\hello.txt","r") as file:
    # print(file.read())

# print(file.closed)


## Exercise: Python Read Write File
# 1. [poem.txt](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/poem.txt) contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.
#
#
# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/exercise_2_stocks.py)
#
# 2. [stocks.csv](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/stocks.csv) contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file
# with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# ```
# pe ratio = price / earnings per share
# price to book ratio = price / book value
# ```
#
#
# Your input format (stocks.csv) is,
#
# |Company Name|Price|Earnings Per Share|Book Value|
# |-------|----------|-------|----------|
# |Reliance|1467|66|653|
# |Tata Steel|391|89|572|
#
# Output.csv should look like this,
#
# |Company Name|PE Ratio|PB Ratio|
# |-------|----------|-------|
# |Reliance|22.23|2.25|
# |Tata Steel|4.39|0.68|
#
# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/exercise_2_stocks.py)

# poem_file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_Read_Write_File\\poem.txt", "r")
#
# # print(poem_file.read())
# max_count = 0
# max_word = ""
# count = {}
# for line in poem_file:
#     words = line.split()
#     for word in words:
#         if word not in count:
#             count[word] = 1
#         else:
#             count[word] += 1
#         if count[word] > max_count:
#             max_count = count[word]
#             max_word = word
# # print(count)
# print(f"Max Word is: {max_word} and count is: {max_count}")
# poem_file.close()

stock_file = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_Read_Write_File\\stocks.csv", "r")
stock_file_out = open("C:\\Users\\kalpd\\PycharmProjects\\codebasics-python-exercises\\9_Read_Write_File\\stocks_out.csv", "w")
stock_file.readline()

stock_file_out.write("Company Name,PE Ratio,PB Ratio \n")
for line in stock_file:
    words = line.split(",")

    company_name = words[0]
    price = words[1]
    earning_per_share = words[2]
    book_value = words[3]

    price = float(price)
    earning_per_share = float(earning_per_share)
    book_value = float(book_value)

    pe_ratio = price/earning_per_share
    price_to_book = price/ book_value

    pe_ratio = round(pe_ratio, 2)
    pb_ratio = round(price_to_book, 2)
    stock_file_out.write(f"{company_name},{pe_ratio},{pb_ratio}\n")

stock_file.close()
stock_file_out.close()
