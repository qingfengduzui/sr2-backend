# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.preprocessing import MultiLabelBinarizer
# from sklearn.cluster import KMeans
# from sklearn.ensemble import RandomForestClassifier
# import jieba
# import joblib
# import sys

# # 加载数据
# data = pd.read_csv('datat.csv')


# # 使用实际的列名
# text_column = 'text'
# labels_column = 'labels'


# # 分词处理
# data[text_column] = data[text_column].apply(lambda x: ' '.join(jieba.cut(x)))

# # 将类别标签转化为二进制形式
# mlb = MultiLabelBinarizer()
# labels = mlb.fit_transform(data[labels_column].apply(lambda x: x.split(',')))

# # 将文本转化为向量
# vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
# features = vectorizer.fit_transform(data[text_column])

# # 使用KMeans进行聚类
# kmeans = KMeans(n_clusters=len(mlb.classes_))
# clusters = kmeans.fit_predict(features)

# # 将聚类结果加入到特征中
# features_with_clusters = pd.DataFrame(features.toarray())
# features_with_clusters['cluster'] = clusters
# features_with_clusters.columns = features_with_clusters.columns.astype(str)  # 将所有列名转换为字符串类型


# # 训练随机森林模型
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(features_with_clusters, labels)

# # 使用模型进行预测
# new_text = ['我偏爱甜蜜。', '酸酸的味道让我开胃。','我喜欢咸','甜味总是让我感到幸福。','我不喜欢苦']
# new_text = [' '.join(jieba.cut(text)) for text in new_text]
# new_features = vectorizer.transform(new_text)
# new_clusters = kmeans.predict(new_features)

# # 将聚类结果加入到新特征中
# new_features_with_clusters = pd.DataFrame(new_features.toarray())
# new_features_with_clusters['cluster'] = new_clusters
# new_features_with_clusters.columns = new_features_with_clusters.columns.astype(str)  # 将所有列名转换为字符串类型


# predicted_labels = model.predict(new_features_with_clusters)

# # 将结果从二进制形式转化为原始标签形式
# predicted_labels = mlb.inverse_transform(predicted_labels)

# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         print(f"received argument: {sys.argv[1]}")
#     else:
#         print("No argument received.")


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
import jieba
import joblib
import sys
import os
print("当前工作目录:", os.getcwd())
os.environ["PYTHONIOENCODING"] = "utf-8"
print(sys.getdefaultencoding())
# 加载数据
data = pd.read_csv(r'C:\Users\王旭博\Desktop\test_one\python\data5.csv')

# 使用实际的列名
text_column = 'text'
labels_column = 'labels'

# 分词处理
data[text_column] = data[text_column].apply(lambda x: ' '.join(jieba.cut(x)))

# 将类别标签转化为二进制形式
mlb = MultiLabelBinarizer()
labels = mlb.fit_transform(data[labels_column].apply(lambda x: x.split(',')))

# 将文本转化为向量
vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
features = vectorizer.fit_transform(data[text_column])

# 使用KMeans进行聚类
kmeans = KMeans(n_clusters=len(mlb.classes_))
clusters = kmeans.fit_predict(features)

# 将聚类结果加入到特征中
features_with_clusters = pd.DataFrame(features.toarray())
features_with_clusters['cluster'] = clusters
features_with_clusters.columns = features_with_clusters.columns.astype(str)  # 将所有列名转换为字符串类型

# 训练随机森林模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(features_with_clusters, labels)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        new_text = sys.argv[1]
        new_text = ' '.join(jieba.cut(new_text))
        new_features = vectorizer.transform([new_text])
        new_clusters = kmeans.predict(new_features)

        new_features_with_clusters = pd.DataFrame(new_features.toarray())
        new_features_with_clusters['cluster'] = new_clusters
        new_features_with_clusters.columns = new_features_with_clusters.columns.astype(str)

        predicted_labels = model.predict(new_features_with_clusters)
        predicted_labels = mlb.inverse_transform(predicted_labels)

        # 打印预测的标签
for label_group in predicted_labels:
    if label_group:  # 检查label_group非空
        print(', '.join(label_group))
    else:
        print("No labels predicted.")