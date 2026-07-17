import json
import os


score_file = "score_store.json"
#文件名，方便后续书写

def save_score (score):
    #存储数据

    records = load_all_records()
    #读取的数据
    records.append(score)
    #添加记录


    with open(score_file,"w",encoding="utf-8") as f :
    #写数据
        json.dump(records,f,ensure_ascii=False,indent = 2)
    #把数据改成json




def load_all_records():
    #从文件读取数据
    
    if not os.path.exists(score_file):
        #判断文件是否存在
        return []
        #返回空列表

    try:
        with open(score_file,"r",encoding="utf-8") as f :
        #读取数据
            return json.load(f)
        #输出改好格式的数据
    except:
        return [0,0,0,]
    


def get_top3():
    #分类数据

    records = load_all_records()
    #数据改格式
    sorted_records = sorted(records,reverse=True)
    #给数据排列
    top3 = sorted_records[:3]
    #取前三个数据
    return top3




