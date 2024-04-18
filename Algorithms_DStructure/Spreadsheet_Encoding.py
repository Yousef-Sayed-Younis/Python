def spreadsheet_encoding(column_str):
    num = 0
    count = len(column_str) - 1
    for s in column_str:
        num += 26 ** count * (ord(s) - 64) # or (ord(s) - ord("A") + 1)
        count -= 1
    return num 

print(spreadsheet_encoding('A')) # 1
print(spreadsheet_encoding('AA')) # 27
print(spreadsheet_encoding('ZZ')) # 702