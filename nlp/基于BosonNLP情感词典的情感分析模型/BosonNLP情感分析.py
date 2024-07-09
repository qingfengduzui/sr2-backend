# -*- coding:utf-8 -*-
import pandas as pd
import jieba

#基于波森情感词典计算情感值
def getscore(text):
    df = pd.read_table(r"BosonNLP_dict\BosonNLP_sentiment_score.txt", sep=" ", names=['key', 'score'])
    key = df['key'].values.tolist()
    score = df['score'].values.tolist()
    # jieba分词
    segs = jieba.lcut(text,cut_all = False) #返回list
    # 计算得分
    score_list = [score[key.index(x)] for x in segs if(x in key)]
    return sum(score_list)

#读取文件
def read_txt(filename):
    with open(filename,'r',encoding='utf-8')as f:
        txt = f.read()
    return txt
#写入文件
def write_data(filename,data):
    with open(filename,'a',encoding='utf-8')as f:
        f.write(data)


if __name__=='__main__':
    text = read_txt('test_data\评论汇总.txt')
    lists  = text.split('\n')

    # al_senti = ['无','积极','消极','消极','中性','消极','积极','消极','积极','积极','积极',
    #             '无','积极','积极','中性','积极','消极','积极','消极','积极','消极','积极',
    #             '无','中性','消极','中性','消极','积极','消极','消极','消极','消极','积极'
    #             ]
    al_senti = read_txt(r'test_data\人工情感标注.txt').split('\n')
    i = 0
    for list in lists:
        if list  != '':
            # print(list)
            sentiments = round(getscore(list),2)
            #情感值为正数，表示积极；为负数表示消极
            print(list)
            print("情感值：",sentiments)

            if sentiments > 0:
                print("机器标注情感倾向：积极\n")
                s = "机器判断情感倾向：积极\n"
            else:
                print('机器标注情感倾向：消极\n')
                s = "机器判断情感倾向：消极"+'\n'
            sentiment = '情感值：'+str(sentiments)+'\n'

            #文件写入
            filename = 'result_data\评论汇总-情感分析结果.txt'
            write_data(filename,'情感分析文本：')
            write_data(filename,list+'\n') #写入待处理文本
            write_data(filename,sentiment) #写入情感值

            write_data(filename,s+'\n') #写入人工标注情感
            i = i+1


