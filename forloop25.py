city_population={"bengaluru":123556,"mysore":74847,"hassan":75432}
largest={city: population for city,population in city_population.items() if population>100000}
print(f" The largest city with its population is {largest}")