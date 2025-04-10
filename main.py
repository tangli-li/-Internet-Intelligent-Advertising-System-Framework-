from .xlsx_operation import (add_info,delete_info)
import pandas as pd
import random

paths=r".\data\ad_system.xlsx"
AD_display=pd.read_excel(paths,sheet_name=0)#提前预设2
USER=pd.read_excel(paths,sheet_name=1)
AD_click=pd.read_excel(paths,sheet_name=2)
ADHOST=pd.read_excel(paths,sheet_name=3)#提前预设1

input0=input("身份：[adholder/usr]")

class adholder:
    def __init__(self,id,adid,ADHOST,AD_display):
        ADHOST.index = ADHOST["广告主id"]
        self.name=ADHOST.loc[id,0]
        self.id=id
        self.total_value=ADHOST.loc[id, 2]
        self.rest_value=ADHOST.loc[id, 3]
        #广告投放
        AD_display.index=AD_display["广告id"]
        self.adid=adid#int
        self.ad_feature=AD_display.loc[adid,2]
        self.display_area=AD_display.loc[adid,3]
        self.sex=AD_display.loc[adid,4]
        self.display_type=AD_display.loc[adid,5]
        self.display_price=AD_display.loc[adid,6]


if input0=="adholder":#广告主身份
    input1=input("登录：")
    host_list=ADHOST.columns
    host_name=ADHOST.loc[:,"广告主"]
    host_id=ADHOST.loc[:,"广告主id"]

    if input1 not in host_name and input1 not in host_id:#创建新身份
        input2 = input("用户不存在，请新建：")
        input3 = input("输入广告预算：")
        id = "000000"
        while id in host_id:
            id = str(random.randint(1, 1e6))
        list = [id, input2, float(input3), float(input3)]
        dict0 = dict(zip(host_list, list))
        ADHOST = add_info(ADHOST, 1, dict0)
        ADHOST.to_excel(paths,sheet_name=3)
        rest_value=float(input3)

    if input1 in host_name:
        ADHOST.index=ADHOST["广告主"]
        rest_value=ADHOST.loc[input1,-1]
    if input1 in host_id:
        ADHOST.index = ADHOST["广告主id"]
        rest_value = ADHOST.loc[input1, -1]

def create