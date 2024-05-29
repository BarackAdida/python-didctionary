with open("test_file.txt", mode="r", encoding="utf-8") as file:
    # file.write("Content loaded \n")
    content = file.read()
    print(content)

print(file.closed)