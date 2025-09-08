val = int(input())

if val >= 212:
    print('Boiling')
    if val == 212:
        print('Caution: Hot!')
elif val >= 115:
    print('Hot')
elif val >= 80:
    print('Warm')
elif val >= 33:
    print('Cold')
else:
    print('Frozen\nWatch out for ice!')