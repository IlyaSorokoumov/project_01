
## Пункт А.

import random
k = 3
y = []
total = 0
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
while k != 0:
  x = random.choice(my_favorite_songs)[1]
  k -= 1
  y.append(x)
# print(y)

for i in y:
  total += i

totalr = round(total, 2)

print("Три песни звучат", totalr, "минут")
