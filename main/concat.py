#读取特定文件夹里的所有csv文件并合并成一个文件
import pandas as pd
import os

#设置读取的文件夹路径
paths= ['C:\\Users\\14253\\Desktop\\数据科学\\datasets\\law',
        'C:\\Users\\14253\\Desktop\\数据科学\\datasets\\law+']

#读取所有文件夹里的csv文件并合并成一个文件
for path in paths:
    path+='\\raw'
    files = os.listdir(path)
    csv_files = [file for file in files if file.endswith('.csv')]

    #读取所有csv文件并合并成一个文件
    df_list = []
    for file in csv_files:
        df = pd.read_csv(os.path.join(path, file))
        df_list.append(df)

    result = pd.concat(df_list)
    result.drop_duplicates(inplace=True)

    #保存合并后的文件
    result.to_csv(path+'\\2004-2023law.csv', index=False)