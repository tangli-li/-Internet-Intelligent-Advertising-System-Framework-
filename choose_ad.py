
import numpy as np
use_NLP=1
class User_coming():
    def __init__(self,User_id,User_search,AD_display,USER,ADHOST):
        self.ID=User_id
        USR_target=USER.loc[USER["用户id"]==self.ID,:]
        self.usr_dict=USR_target.iloc[:,2:].to_dict(orient="list")
        self.AD_display=AD_display
        self.ADHOST=ADHOST
        self.User_search=User_search
    def sort(self,List,num):
        paired = [(value, idx) for idx, value in enumerate(List)]
        # 按数值降序排序，数值相同则按索引升序
        sorted_pairs = sorted(paired, reverse=True)
        return [pair[1] for pair in sorted_pairs[:num]]
    def rough_select(self,num=30):#用户属性与广告需求属性一致
        AD_ID = self.AD_display.loc[:, "广告id"].to_numpy()
        AD_host=self.AD_display.loc[:,"广告主id"].to_numpy()
        AD_atri=self.AD_display.iloc[:,4:]
        match_list=[]
        for i in range(0,len(AD_host)):
            ADi=AD_host[i]
            host_info=self.ADHOST.loc[self.ADHOST["广告主id"]==ADi,"广告预算剩余"].to_list()
            if host_info[0]<=0:#如果费用用完则不考虑
                continue
            else:
                match_num = 0
                AD_dict = AD_atri.loc[i,:].to_dict()#广告主需求属性
                for ii in AD_dict.keys():
                    ad_value=AD_dict[ii]
                    usr_value=self.usr_dict[ii][0]
                    if ad_value==usr_value:#完全匹配
                        match_num+=1
                match_list.append(match_num)
        ad_index=self.sort(match_list,num)
        ad_out=AD_ID[ad_index]
        return ad_out

    def exact_select(self,AD_ID,num=5):#num为初筛后广告最大数量
        AD_content=[]
        for i in AD_ID:
            AD1=self.AD_display.loc[self.AD_display["广告id"]==i,"广告内容"].to_list()
            AD_content.append(AD1[0])
        if len(AD_ID)<num:
            return AD_ID
        else:
            if use_NLP == 1:
                import torch
                from transformers import BertModel, BertTokenizer
                user_search=self.User_search
                Sim=[]
                device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
                tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
                model = BertModel.from_pretrained('bert-base-uncased').to(device)
                model.eval()
                print("第二次筛选时搜索词与广告语相似度：")
                for i in AD_content:
                    sim=bert(user_search,i,tokenizer,model,device)
                    Sim.append(sim)
                    print(f"{i}：{sim}")
                top_indices = self.sort(Sim,num)
                AD_ID_out=AD_ID[top_indices]
                return AD_ID_out
            if use_NLP == 0:
                AD_ID_out=np.random.choice(AD_ID,size=num,replace=False)
                return AD_ID_out

    def sort_selected(self,AD_ID,num=3):
        AD_id=self.AD_display.loc[self.AD_display["广告id"].isin(AD_ID),:]

        ADhost_id=AD_id.loc[:,"广告主id"].to_numpy()
        price=AD_id.loc[:,"广告竞价"].to_numpy()
        value=[]
        for i in range(0,len(ADhost_id)):
            ADhost_id0=ADhost_id[i]
            click_rate=self.ADHOST.loc[self.ADHOST["广告主id"]==ADhost_id0,"历史广告被点击率"].to_list()
            price0=price[i]
            value.append(click_rate[0]*price0)
        top_sort_id=self.sort(value,num)
        AD_ID_out = AD_ID[top_sort_id]
        AD_content_out=[]
        for i in AD_ID_out:
            adi=self.AD_display.loc[self.AD_display["广告id"]==i,"广告内容"].to_numpy()
            AD_content_out.append(adi)
        return AD_ID_out,AD_content_out

    def run_all(self):
        AD_1=self.rough_select()
        AD_2=self.exact_select(AD_1)
        AD_3,AD_content=self.sort_selected(AD_2)
        return AD_3,AD_content

def bert(sentence1,sentence2,tokenizer,model,device):
    import torch
    def get_bert_embedding(sentence):
        inputs = tokenizer(sentence, return_tensors='pt', padding=True, truncation=True).to(device)
        outputs = model(**inputs)
        return outputs.last_hidden_state[:, 0, :].detach()  # 取[CLS]向量

    embedding1 = get_bert_embedding(sentence1)
    embedding2 = get_bert_embedding(sentence2)

    # 计算余弦相似度
    cos_sim = torch.nn.CosineSimilarity(dim=0)
    similarity = cos_sim(embedding1[0], embedding2[0]).item()
    return similarity

