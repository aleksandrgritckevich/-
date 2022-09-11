#!/usr/bin/python3




import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Создаем датафрейм из cvs файла созданного в предыдущей части задания. 

df = pd.read_csv('output.csv')
colors = ['indianred', 'lightblue', 'limegreen', 'violet']

# Создаем функции для генерации графиков.
def plotscatter(df):
    fig,ax = plt.subplots()
    ax = sns.scatterplot(data=df,x='x', y='y',palette = colors, hue='cluster_name',s=100) # Создаем базовый график.
    ax.set_title(f"Area: {df['area'].iloc[0]}",fontdict={'fontsize':15},pad=30)# Добавляем заголовок графика.
    ax.axis('off') # Убираем оси с графика.
    # Добавляем обводку точек в легенде. Обводка выполнена более темным оттенком того же цвета, что и цвет кластера.
    handles, labels = ax.get_legend_handles_labels()
    darkercolors = ['darkred', 'darkblue', 'darkgreen', 'darkviolet']
    for i in range(len(handles)):
        handles[i].set_edgecolor(darkercolors[i])
    lgd = ax.legend(
        handles, 
        labels,
        loc="upper left", 
        ncol=2,
    )
    # Добавляем легенду за границами самого графика. Также добавляем название легенды.
    plt.legend(bbox_to_anchor=(1.05, 0.7), loc=2, borderaxespad=0.,title='Кластеры')
    # Добавляем Footer-подпись.
    ax.annotate('Источник: НИУ ВШЭ',(0.7,-0.1),xycoords='axes fraction')
    # Добавляем подписи для каждлй точки в виде соответствующего ей keyword. Также, если длина словосочетания
    # превышает 17 символов, переносим его. Если слова 2, то переносим одно слово на следующую строку. Если слов 3 или 4,
    # переносим 2 слова на следующую строку.
    # Кроме того, корректируем величину надписей в зависимости от того насколько близко находятся другие точки для
    # минимизации наложений.
    for line in range(0,df.shape[0]):
        distances = (df['x']-df['x'].iloc[line])**2+(df['y']-df['y'].iloc[line])**2
        distances = distances.drop(line)
        if sum(distances>5)==len(distances):
            size=6.2
        elif sum(distances>2)<len(distances):
            size=3
        else:
            size=4
        if len(df['keyword'].iloc[line])>=17:
            listofwords = df['keyword'].iloc[line].split(' ')
            if len(listofwords)==2:
                word = listofwords[0]+'\n '+listofwords[1]
            elif len(listofwords)==3:
                word = listofwords[0]+'\n '+listofwords[1]+' '+listofwords[2]
            elif len(listofwords)==4:
                word = listofwords[0]+' '+listofwords[1]+'\n '+listofwords[2]+' '+listofwords[3]
            else:
                word = listofwords[0]                            
            ax.text(df['x'].iloc[line]+0.01, df['y'].iloc[line], 
            word, horizontalalignment='center', 
            size=size, color='black', weight='semibold')
        else:
            ax.text(df['x'].iloc[line]+0.01, df['y'].iloc[line], 
            df['keyword'].iloc[line], horizontalalignment='center', 
            size=size, color='black', weight='semibold')
    # Название файла, в котором будет сохранен график.
    file_name = f"{df['area'].iloc[0]}.png"
    # Если название area содержит \, заменяем его на or.
    if "\\" in file_name:
        file_name = file_name.replace('\\'," or ")
    # Сохраняем график в png.
    plt.savefig(file_name, facecolor='w',bbox_inches='tight',dpi=400)



# Генерируем графики для каждой area и сохраняем их.
for area in df['area'].unique():
    newdf = df[df['area']==area]
    newdf = newdf.reset_index()
    plotscatter(newdf)