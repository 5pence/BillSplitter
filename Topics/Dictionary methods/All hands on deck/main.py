
card = []
for i in range (0, 6):
    card.append(input())
for inx, val in enumerate(card):
    if val == 'Jack':
        card[inx] = 11
    elif val == 'Queen':
        card[inx] = 12
    elif val == 'King':
        card[inx] = 13
    elif val == 'Ace':
        card[inx] = 14
    else:
        card[inx] = int(val)
print(sum(card)/6)
