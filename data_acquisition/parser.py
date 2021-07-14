file = open("top50_list.txt", 'r')
csv_file = open("top50_parsed.csv", 'w')

for line in file:
    word = line.split(" ")
    print("\n word:")
    print(word)
    symbol = word[1].split("\t")
    print("\n symbol:")
    print(symbol)
    csv_file.write(symbol[0][3:] + ',' + word[0] + '\n')

csv_file.close()

