def openSheeshfile(filename):
    """
    Args: filename [string] name of the sheesh file
    returns file object
    """
    foo = open(filename,"r+")
    # for line in foo.readlines():
    #     if line=="":
    #         foo.seek(1)
    foo.read().strip("\n")
    foo.write("\n")
    return foo

# f = openSheeshfile("sheeshfile.txt")
# print(f.read())
    
# filename = "sheeshfile.txt"
# fullfile = openSheeshfile(filename)
# linenum=1
# for lines in fullfile.readlines():
#     line = lines.split()
#     for word in line:
#         identifier = delemitword(word,len(word)) #uses delimeter to break the word to the one we actually need.

#         #Use try catch block here for the other word associated with the delemiter

#         if identifier:
#             print("Token on line ",linenum," :",identifier)
#     linenum+=1
