#!/usr/bin/python3

import numpy as np
import pandas as pd

df = pd.read_csv('Тестовое задание - tz_data.csv')
cols = ['area','cluster','cluster_name','keyword','x','y','count'] # Оставляем эти столбцы
df = df[cols]
df['y'] = pd.to_numeric(df['y'],errors='coerce') # Конвертируем столбец 'y' в numeric, удаляя неформатные значения
df['count'] = pd.to_numeric(df['count'],errors='coerce') # То же самое со столбцом 'count'
df = df.dropna(subset=cols) # Удаляем строки с 'missing values'
colors = ['indianred', 'lightblue', 'limegreen', 'violet'] # Цвета кластеров. 
df['color']=df['cluster'].replace([0, 1, 2, 3], colors) # Всего в данных может быть 4 кластера присваиваю каждому из них один и тот же цвет во всех area.
df = df.drop_duplicates(subset=['area','keyword'], keep='first') # Убираем дублированные слова в каждой area.
df = df.sort_values(['area','cluster','cluster_name','count'], ascending=[True, True,True,False]) # Сортируем по столбцам.
df['cluster'] = pd.to_numeric(df['cluster'], downcast='integer') # Конвертируем столбец 'cluster' в integer
df['count'] = pd.to_numeric(df['count'],downcast='integer') # Конвертируем столбец 'count' в integer
df = df.reset_index()
df.to_csv('output.csv',index=False) # Сохраняем в csv