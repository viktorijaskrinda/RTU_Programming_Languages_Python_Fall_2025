"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

temperatures = [10, 12, 14, 8, 6, 4, 2]
city_population = {"Riga": 591882, "Amsterdam": 933680, "Cork": 224004}

average_temperature = sum(temperatures) / len(temperatures)
largest_city = max(city_population, key=lambda city: city_population[city])
largest_population = city_population[largest_city]
total_population = sum(city_population.values())
smallest_city = min(city_population, key=lambda city: city_population[city])
smallest_population = city_population[smallest_city]

print("Average temperature:", average_temperature, "Celsius")
print("Largest city:", largest_city, "-", largest_population)
print("Total population:", total_population)
