import requests

from operator import itemgetter


# make an api call and store the response 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
try:
    r = requests.get(url)
except EnvironmentError:
    print("Could not be found")
else:
    print("Status code: ", r.status_code)

# process infomation about each submisson
submissions_id = r.json()
submissions_dicts = []
for sub in submissions_id[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item' + 
        str(sub) + '.json')
    submision_r = requests.get(url)
    print(submision_r.status_code)`                         `
    response_dict = submision_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' +
        str(sub),
        'comments': response_dict.get('descendants', 0)

        }
    submissions_dicts.append(submission_dict)

submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submissions_dicts:
    print("\nTitle: ", submission_dict['title'])
    print("Discussion link: ", submission_dict['link'])
    print("Comments: ", submission_dict['comments'])

