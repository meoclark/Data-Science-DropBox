city_name = "Istanbul,Turkey"
pop_1927 = 691000
pop_2017 =15029231
pop_change = pop_2017 - pop_1927
percentage_gr = ((pop_change)/pop_1927) * 100
annual_gr = percentage_gr / 90

def population_growth(year_one, year_two, population_one, population_two):
  growth_rate =  (((population_two - population_one)/population_one) * 100)/(year_two - year_one)
  return growth_rate

print(annual_gr)
set_one = population_growth(1927,2017,691000,15029231)
print(set_one)

set_two = population_growth(1950,2000,983000,8831800)
print(set_two)

report = f"From the year 1927 to 2017 there was {pop_change} change in the population and an annual growth rate of {set_one}. Also from the year 1950 t0 2000 there was an annual growth rate of {set_two}"
print(report)





  









