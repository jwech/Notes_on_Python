import json
import pygal
from country_codes import get_country_code
import pygal.maps.world
from pygal.style import RotateStyle, LightColorizedStyle

filename = 'd:/p/projects_trials/grab_data/data/population_data.json'
with open(filename) as f:
    pop_data =json.load(f)

country_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        # print(country_name, ':', population)
        code = get_country_code(country_name)
        if code:
            country_population[code] = population
        else:
            print('ERROR:', country_name)

cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in country_population.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop
print(len(cc_pops1), len(cc_pops2), len(cc_pops3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population - 2010'
wm.add("0~10m", cc_pops1)
wm.add("10m-1bn", cc_pops2)
wm.add(">1bn", cc_pops3)
wm.render_to_file('world_population.svg')