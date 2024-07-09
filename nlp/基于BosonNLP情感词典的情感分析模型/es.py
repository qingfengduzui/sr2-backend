import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import jieba

# 步骤 1: 读取 Excel 文件
# 假设 Excel 文件名为 'data.xlsx'，第一列包含句子，第二列包含合并的分类标签
df = pd.read_excel('data.xlsx', header=None)
df.columns = ['sentence', 'category']

# 处理合并的单元格，为每一行分配正确的分类标签
df['category'].fillna(method='ffill', inplace=True)

# 步骤 2: 数据预处理和分词
def preprocess_text(text):
    return " ".join(jieba.cut(text))

df['processed_sentence'] = df['sentence'].apply(preprocess_text)

# 步骤 3: 特征提取
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['processed_sentence'])
y = df['category']

# 步骤 4: 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 步骤 5: 模型训练
model = LogisticRegression()
model.fit(X_train, y_train)

# 步骤 6: 模型评估
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 保存模型，以便后续使用
# 你可以使用 joblib 或 pickle 来保存模型
import joblib
joblib.dump(model, 'model.pkl')
joblib.dump(tfidf, 'tfidf.pkl')

# 使用保存的模型进行预测
def predict_new_sentence(new_sentence):
    model = joblib.load('model.pkl')
    tfidf = joblib.load('tfidf.pkl')
    processed_sentence = preprocess_text(new_sentence)
    features = tfidf.transform([processed_sentence])
    return model.predict(features)[0]

# 示例：预测新句子
print(predict_new_sentence("这是一个测试句子"))