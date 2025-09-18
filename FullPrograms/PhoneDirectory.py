# Phone Directory for the same number in different countries

area, prefix, line = input().split()

phone_directory = {
    "U.S.":     f"+1 ({area}){prefix}-{line}",
    "Brazil":   f"+55 ({area}){int(prefix) + 100}-{line}",   
    "Croatia":  f"+385 ({area}){prefix}-{str(int(line) + 50).zfill(len(line))}",   
    "Egypt":    f"+20 ({int(area) + 30}){prefix}-{line}",    
    "France":   f"+33 ({prefix}){area}-{line}" 
}

print("Country  Phone Number")
print("-------  ------------")

for country,number in phone_directory.items():
    print(f'{country:<8} {number}')
