import pandas as pd
from pypinyin import lazy_pinyin
from config import Config


def process_data(file_path):
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    df[Config.UID] = df[Config.UID].ffill().astype(int)
    df[Config.usr_key] = df[Config.usr_key].ffill()
    df[Config.PID] = df.groupby(Config.UID)[Config.PID].transform(lambda x: x.ffill())
    df['original_devname'] = df[Config.devname]  # 新增原始名称列
    df[Config.devname] = df[Config.devname].apply(lambda x: ''.join(lazy_pinyin(x)))
    required_cols = [Config.UID, Config.usr_key, Config.PID, Config.devname, 'original_devname']  # 新增校验列
    if df[required_cols].isnull().any().any():
        raise ValueError("数据填充有空白")
    return df[[Config.UID, Config.usr_key, Config.PID, Config.devname, 'original_devname']].copy()  # 新增返回列


if __name__ == '__main__':
    file_path = 'demo.xlsx'
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    print(df)
