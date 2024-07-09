import requests
from bs4 import BeautifulSoup

import json
from time import sleep
import random
import os


url = 'https://prof.mathege.ru/'
for_all_tasks = '&filter=&limit=1000'


# req = requests.get(url)
# scr = req.text
# print(scr)

# with open('main.html', 'w') as f:
#     f.write(scr)



# with open('index.html') as f:
#     scr = f.read()

# soup = BeautifulSoup(scr, "xml")

# tasks = {}

# all_tasks_href = soup.find('div', class_='catalogbuttons').find_all('a')
# for task in all_tasks_href:
#     task_text = task.text
#     task_href = 'https://prof.mathege.ru/' + task.get("href")
#     tasks[task_text] = task_href

# with open('task_links.json', 'w') as f:
#     json.dump(tasks, f, indent=4, ensure_ascii=False)

# with open('task_links.json') as f:
#     links = json.load(f)

# for key in links:
#     req = requests.get(links[key] + for_all_tasks)
#     scr = req.text

#     with open(f'data/number_{key}.html', 'w') as f:
#         f.write(scr)

#     print(f'Страница задания {key} успешна сохранена')

# full_pic = {}

# for num in range(1, 12 + 1):
#     with open(f'data/number_{num}.html') as f:
#         scr = f.read()
#     soup = BeautifulSoup(scr, "xml")
#     all_pic_tasks = soup.find_all('div', class_='task')
#     help_pic = {}
#     for pic in all_pic_tasks:
#         number_in = BeautifulSoup(str(pic), "xml").find('div', class_='titleTask').text.split(' ', maxsplit=1)[1].split('.', maxsplit=1)[0]
#         link_pic_in = url + BeautifulSoup(str(pic), "xml").find('div', class_='contentTask').find('img').get('src')
#         print(number_in)
#         print(link_pic_in)
#         help_pic[number_in] = link_pic_in
#     full_pic[num] = help_pic

#     with open('data/task_dict.json', 'w') as f:
#         json.dump(full_pic, f, indent=4, ensure_ascii=False)
    
#     print(f'Страница задания {num} успешна сохранена')
#     sleep(random.randint(2, 4))

# with open('data/task_dict.json') as f:
#     task_pic = json.load(f)
# for i in task_pic:
#     os.mkdir(f'data/photo_math_ege/{i}_num')
#     for g in task_pic[i]:
#         response=requests.get(task_pic[i][g])
#         if response.status_code == 200:
#             with open(f'data/photo_math_ege/{i}_num/{g}.jpg', 'wb') as f:
#                 f.write(response.content)
#     print(f'Задания №{i} успешно сохранены')
#     sleep(random.randint(2, 4))

with open('data/task_dict.json') as f:
    task_pic = json.load(f)
    
# for i in task_pic:
#     for g in task_pic[i]:
#         link = task_pic[i][g]
#         task_pic[i][g] = {}
#         task_pic[i][g]['link'] = link
#         task_pic[i][g]['answer'] = None

# with open('data/task_dict.json', 'w') as f:
#     json.dump(task_pic, f, indent=4, ensure_ascii=False)
    
# with open('data/task_dict.json') as f:
#     task_pic = json.load(f)

# while True:
#     num = random.choice(list(task_pic))
#     task = random.choice(list(task_pic[num]))
#     link = task_pic[num][task]['link']
#     if task_pic[num][task]['answer'] is None:
#         print(link)
#         answer = input(f'Введите ответ на задание №{num} {task}: ')

#         task_pic[num][task]['answer'] = answer

#         with open('data/task_dict.json', 'w') as f:
#             json.dump(task_pic, f, indent=4, ensure_ascii=False)
    
count_in_total = 0
count_with_answer = 0

with open('data/task_dict.json') as f:
    task_pic = json.load(f)

for i in task_pic:
    for g in task_pic[i]:
        if not(task_pic[i][g]['answer'] is None):
            count_with_answer += 1
        count_in_total += 1

print(count_with_answer, count_in_total, count_with_answer /  count_in_total)