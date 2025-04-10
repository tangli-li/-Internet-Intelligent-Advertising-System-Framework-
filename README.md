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

填入广告初始总预算，点击确定后跳转到广告主操作界面。增加按钮功能未设置，返回按钮跳转到登录界面。

## 用户注册界面
![image](https://github.com/user-attachments/assets/b932142f-474a-4a0c-9d3e-11144c2a3bcb)

