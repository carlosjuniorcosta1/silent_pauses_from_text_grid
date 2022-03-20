# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 18:58:36 2021

@author: Usuario
"""

import pandas as pd
import re
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker




file = input(str('Digite o nome - com extensão TextGrid- do arquivo gerado pelo script de Mietta Lennes \n Lembre-se de que as pausas devem estar marcadas com "xxx": '))

while True:
    
    limite_min = input('Digite um limite mínimo,em segundos, para ser considerado pausa silenciosa no gráfico \n ou aperte enter para ignorar: ')
    if len(limite_min) == 0:
        continue
    if len(limite_min) > 0:
        limite_min = float(limite_min)
        
    limite_max = input('Digite um limite máximo, em segundos, para ser considerado pausa silenciosa no gráfico \n ou aperte enter para ignorar: ')
    
    if len(limite_max) == 0:
        break
    if len(limite_max) > 0:
        limite_max = float(limite_max)
        break 
    
    
with open(file, 'r') as source:
    arquivo = source.read()

arquivo_f = ' '.join(re.findall(r'intervals.+\n.\s+xmin...+\n.\s+xmax.+\n.\s+text...\"xxx\"', arquivo))


arquivo_f = re.sub(r'(?<=text).+', '', arquivo_f)

arquivo_f = arquivo_f.split('text')

df = pd.DataFrame(arquivo_f)

df.columns = ['dados']

df['xmin'] = df['dados'].apply(lambda x: ' '.join(re.findall(r'(?<=xmin).+', x)))
df['xmin'] = df['xmin'].apply(lambda x: re.sub(r'=\s', '', x))
df['xmax'] = df['dados'].apply(lambda x: ' '.join(re.findall(r'(?<=xmax).+', x)))
df['xmax'] = df['xmax'].apply(lambda x: re.sub(r'=\s', '', x))
df = df.query('xmin != ""')
df['xmin'] = df['xmin'].astype('float')
df['xmax'] = df['xmax'].astype('float')
df['silent_pause'] = df['xmax'] - df['xmin']

df['silent_pause'] = df['silent_pause'].round(3)


df['audio'] = file[:-9]


if type(limite_min) == float and type(limite_max) == float:
    df_f = df.query('silent_pause > @limite_min & silent_pause < @limite_max')
    sns.set_style('whitegrid')
    plt.figure(dpi = 300, figsize=(6, 5))
    a = sns.histplot(data= df_f, x = 'silent_pause', kde = True, color = 'purple')
    a.set_title(f'Duração de pausas preenchidas em {df_f["audio"][0]}', fontsize = 16)
    a.set_xlabel("Tempo (s)",fontsize= 14)
    a.set_ylabel("Frequência",fontsize = 15)
    a.tick_params(labelsize=15)
    a.xaxis.set_major_locator(ticker.LinearLocator(20))
    plt.xticks(rotation=90)
    plt.show()

    sns.set_style('whitegrid')
    plt.figure(dpi = 300, figsize=(5, 4))
    a = sns.boxplot(data = df_f, y = 'silent_pause', showmeans = True, showfliers = False, \
                     meanprops={"marker":"s","markerfacecolor":"white", "markeredgecolor":"black"}, color = 'orange')
    sns.swarmplot(data = df_f, y = 'silent_pause', color = 'black', alpha = 0.5)
    a.set_title(f'Duração de pausas silenciosas em {df_f["audio"][0]}', fontsize = 16) 
    # a.set_xlabel(,fontsize= 14)
    a.set_ylabel("Duração - (s)",fontsize = 15)
    a.tick_params(labelsize=15)
    plt.show()
    
if type(limite_min) == float and type(limite_max) == str:
    df_f = df.query('silent_pause > @limite_min')
    sns.set_style('whitegrid')
    plt.figure(dpi = 300, figsize=(6, 5))
    a = sns.histplot(data= df_f, x = 'silent_pause', kde = True, color = 'purple')
    a.set_title(f'Duração de pausas preenchidas em {df_f["audio"][0]}', fontsize = 16)
    a.set_xlabel("Tempo (s)",fontsize= 14)
    a.set_ylabel("Frequência",fontsize = 15)
    a.tick_params(labelsize=15)
    a.xaxis.set_major_locator(ticker.LinearLocator(20))
    plt.xticks(rotation=90)
    plt.show()

    sns.set_style('whitegrid')
    plt.figure(dpi = 300, figsize=(5, 4))
    a = sns.boxplot(data = df_f, y = 'silent_pause', showmeans = True, showfliers = False, \
                     meanprops={"marker":"s","markerfacecolor":"white", "markeredgecolor":"black"}, color = 'orange')
    sns.swarmplot(data = df_f, y = 'silent_pause', color = 'black', alpha = 0.5)
    a.set_title(f'Duração de pausas silenciosas em {df_f["audio"][0]}', fontsize = 16) 
    # a.set_xlabel(,fontsize= 14)
    a.set_ylabel("Duração - (s)",fontsize = 15)
    a.tick_params(labelsize=15)
    plt.show()
    

if type(limite_min) == str and type(limite_max) == float:
    df_f = df.query('silent_pause < @limite_max')
    sns.set_style('whitegrid')
    plt.figure(dpi = 300, figsize=(6, 5))
    a = sns.histplot(data= df_f, x = 'silent_pause', kde = True, color = 'purple')
    a.set_title(f'Duração de pausas preenchidas em {df_f["audio"][0]}', fontsize = 16)
    a.set_xlabel("Tempo (s)",fontsize= 14)
    a.set_ylabel("Frequência",fontsize = 15)
    a.tick_params(labelsize=15)
    a.xaxis.set_major_locator(ticker.LinearLocator(20))
    plt.xticks(rotation=90)
    plt.show()

    sns.set_style('whitegrid')
    plt.figure(dpi = 300, figsize=(5, 4))
    a = sns.boxplot(data = df_f, y = 'silent_pause', showmeans = True, showfliers = False, \
                     meanprops={"marker":"s","markerfacecolor":"white", "markeredgecolor":"black"}, color = 'orange')
    sns.swarmplot(data = df_f, y = 'silent_pause', color = 'black', alpha = 0.5)
    a.set_title(f'Duração de pausas silenciosas em {df_f["audio"][0]}', fontsize = 16) 
    # a.set_xlabel(,fontsize= 14)
    a.set_ylabel("Duração - (s)",fontsize = 15)
    a.tick_params(labelsize=15)
    plt.show()


if type(limite_min) == str and type(limite_max) == str:
    
    sns.set_style('whitegrid')
    plt.figure(dpi = 300, figsize=(6, 5))
    a = sns.histplot(data= df, x = 'silent_pause', kde = True, color = 'purple')
    a.set_title(f'Duração de pausas preenchidas em {df["audio"][0]}', fontsize = 16)
    a.set_xlabel("Tempo (s)",fontsize= 14)
    a.set_ylabel("Frequência",fontsize = 15)
    a.tick_params(labelsize=15)
    a.xaxis.set_major_locator(ticker.LinearLocator(20))
    plt.xticks(rotation=90)
    plt.show()

    sns.set_style('whitegrid')
    plt.figure(dpi = 300, figsize=(5, 4))
    a = sns.boxplot(data = df, y = 'silent_pause', showmeans = True, showfliers = False, \
                     meanprops={"marker":"s","markerfacecolor":"white", "markeredgecolor":"black"}, color = 'orange')
    sns.swarmplot(data = df_f, y = 'silent_pause', color = 'black', alpha = 0.5)
    a.set_title(f'Duração de pausas silenciosas em {df["audio"][0]}', fontsize = 16) 
    # a.set_xlabel(,fontsize= 14)
    a.set_ylabel("Duração - (s)",fontsize = 15)
    a.tick_params(labelsize=15)
    plt.show()


try:
    if len(df_f) < 0:
        df.to_csv(f'{df["audio"][0]}.csv')
    if len(df_f) > 0:
        df.to_csv(f'{df["audio"][0]}.csv')
        df_f.to_csv(f'{df_f["audio"][0]}_lim.csv')
except: 
    pass 

