import requests
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'


def get_status_code(url_link):
    """see if a URL for an API works will return a code number"""
    final_test = requests.get(url_link)
    return final_test.status_code

def get_the_url(url_link):
    """returns the url when requested"""
    r = requests.get(url_link)
    return r

r = get_the_url(url)
print("Status code: ", get_status_code(url))

# store the API repsonse in a varibale 
response_dict = r.json()
print("Total repo : ", response_dict['total_count'])

# process the results 
# print(response_dict.keys())

repo_dicts = response_dict['items']
print("Repos returned : ", len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

names, plot_dicts = [], []
print("\nSelected infomation about first repository")
for repo_dict in repo_dicts:
    # for dict in list of dict repo_dicts
    # appending these keys to a list will make them easier to work
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

    
    # print("Name: ", repo_dict['name'])
    # print("Owner: ", repo_dict['owner']['login'])
    # print("Stars: ", repo_dict['stargazers_count'])
    # print("Repository: ", repo_dict['html_url'])
    # print("Created: ", repo_dict['created_at'])
    # print("Updated: ", repo_dict['updated_at'])
    # print("Description: ", repo_dict['description'])




my_style = LS('#333366', base_style=LCS)

# make a visualzation 
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False 
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000



chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most Starred Python Projects on Github"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')




