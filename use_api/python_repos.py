import requests
import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

r_dicts = r.json()
print('incomplete_results:', r_dicts['incomplete_results'])
print('Total amount:', r_dicts['total_count'])

repo_dicts = r_dicts['items'] # list
print('Returned repositories amount:', len(repo_dicts))

names, plot_dicts = [], []
# # print('\nSelected information about returned repositories.')
for repo_dict in repo_dicts:
    # print('\nName:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repository:', repo_dict['html_url'])
    # print('Created:',  repo_dict['created_at'])
    # print('Updated:', repo_dict['updated_at'])
    # print('Description:', repo_dict['description'])
    names.append(repo_dict['name'])
    if repo_dict['description']:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url'],
        }
        plot_dicts.append(plot_dict)
    else:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': 'nothing',
            'xlink': repo_dict['html_url']
        }
        plot_dicts.append(plot_dict)   

my_style = LS('#336699', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_lengend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.main_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

bar = pygal.Bar(my_config, style=my_style)
bar.title = 'Most-Starred Python Projects on GitHub'
bar.x_labels = names
bar.add('', plot_dicts)
bar.render_to_file('stars_javascript.svg')
