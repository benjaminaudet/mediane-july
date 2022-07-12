from itertools import cycle, islice

week_days = ['Lundi', 'Mardi', 'Mercredi',
             'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

# here we use cycle to transform a standard list into a circular list
# and we use islice to move the iterator to the wanted value
pool_week_days = cycle(week_days)
start_position = islice(pool_week_days, 5, None)

i = 0
while i < len(week_days):
    print('{} : {} |'.format(i + 1, next(start_position)), end=" ")
    i += 1
