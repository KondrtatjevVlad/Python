#!/usr/bin/env python
# coding: utf-8

# ## Задание 1

# Переведите содержимое файла purchase_log.txt в словарь purchases вида:
# {'1840e0b9d4': 'Продукты', ...}

# In[ ]:


import json


# In[114]:


# создание словаря
purchases = {}


# In[116]:


# Читаем purchase_log.txt и формируем словарь purchases пропуская пустые и некорректные строки
with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().lstrip('\ufeff')  
        if not line:
            continue
        try:
            data = json.loads(line)
            purchases[data['user_id']] = data['category']
        except (json.JSONDecodeError, KeyError):
            continue


# In[117]:


# Вывод первых строк
for i, (user_id, category) in enumerate(purchases.items()):
    print(f"{user_id} '{category}'")
    if i == 4: 
        break


# In[118]:


# Проверка: вывод последних строк
for user_id, category in list(purchases.items())[-4:]:
    print(f"{user_id} '{category}'")


# ## Задание 2 

# Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки. Если покупка была, сам файл visit_log.csv изменять не надо.
# Запишите в файл funnel.csv визиты из файла visit_log.csv, в которых были покупки с указанием категории.
# 

# In[98]:


import csv


# In[119]:


# создание нового словаря
purchases_1 = {}


# In[120]:


#Чтение purchase_log.txt в словарь
with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().lstrip('\ufeff')
        if not line:
            continue
        try:
            data = json.loads(line)
            purchases_1[data['user_id']] = data['category']
        except (json.JSONDecodeError, KeyError):
            continue


# In[121]:


# построчная обработка visit_log.csv
with open('visit_log.csv', 'r', encoding='utf-8') as f_in, \
     open('funnel.csv', 'w', encoding='utf-8', newline='') as f_out:
    
    reader = csv.reader(f_in, delimiter=',')
    writer = csv.writer(f_out)
    
    writer.writerow(['user_id', 'source', 'category'])
    
    next(reader) 
    for row in reader:
        if not row:
            continue
        user_id = row[0]
        source = row[1] if len(row) > 1 else ''
        
        if user_id in purchases_1:
            writer.writerow([user_id, source, purchases_1[user_id]])


# In[122]:


# проверка записи данных в funnel и вывод первых 10 строк
with open('funnel.csv', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        print(line.strip())
        if i == 9:  
            break

