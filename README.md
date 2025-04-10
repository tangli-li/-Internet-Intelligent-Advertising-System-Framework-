# 备注
本项目内容包含UI界面设计、广告筛选策略设计以及数据库设计（暂时使用excel进行数据存储）。

# 需要安装的python库
1. openpyxl
2. torch & transformers (如果不安装这些python库，请将脚本choose_ad.py中第三行的use_NLP设置为0，此时使用使用随机筛选代替语义相似度筛选)

# 代码运行
运行UI_1.py即可

# 界面使用介绍
## 登录界面
![image](https://github.com/user-attachments/assets/bad67bb9-8034-4499-b0a0-151846ad73e6)

在访问者类型中选择身份，在下方写身份id。如果已录入该身份id，则进入对应身份的操作界面。如果未录入该身份id，则进入对应身份的注册界面。

## 广告主注册界面
![image](https://github.com/user-attachments/assets/1fac3521-8735-4fde-9c7a-cda61561b133)

填入广告初始总预算，点击确定后跳转到广告主操作界面，为必填。增加按钮功能未设置，返回按钮跳转到登录界面。

## 用户注册界面
![image](https://github.com/user-attachments/assets/da68dcf1-6d16-4b8f-a014-fd7598f22f6a)

选择基础信息类型，填入相关信息后需点击确认录入按钮，为选填。如果有多条基础信息则重复上述操作。点击确定后跳转到用户操作界面，增加按钮功能未设置，返回按钮跳转到登录界面。

## 广告主操作界面
![image](https://github.com/user-attachments/assets/07c0f836-5a05-41e3-9059-8be16ed1a505)

1. 广告主基础信息显示界面，点击确定后跳转下一界面，点击返回按钮跳转到登录界面。

![image](https://github.com/user-attachments/assets/b7586f77-9e76-41f0-9dde-dc553322061d)

2. 界面右上角显示广告编号，编号后四位随机生成，第五位开始为广告主ID。界面左侧选择基础信息类型，填入相关信息后需点击确认录入按钮，为选填。界面右侧填入广告内容和竞价，为必填。增加按钮功能暂未设置，返回按钮跳转到上一界面，确定跳转到下一界面。

![image](https://github.com/user-attachments/assets/460840ec-f07b-45af-b6d1-d0ae260770ed)

3.在确认是否继续录入的界面中，点击确定返回上一界面（广告编号变化，广告主ID不变），点击退出跳转到登录界面。

## 用户操作界面
![image](https://github.com/user-attachments/assets/f0c3f175-a51b-4777-9ccd-311fcc3502c9)

1. 在搜索框中输入搜索词，为必填。点击确定后进入下一界面，点击返回跳转到登录界面。

![image](https://github.com/user-attachments/assets/91dc480f-6149-45d8-b915-82866206589c)（示例）

2. 

