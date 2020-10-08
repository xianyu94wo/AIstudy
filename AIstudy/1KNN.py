#

######################1
# 数据集获取
# 小数据集获取
#
# print(iris_dataset.DESCR)
# 大数据集获取
# new = fetch_20newsgroups()
# print(new)
########################2
# print('keys of iris_dataset : \n{}'.format(iris_dataset.keys()))
#
# print(iris_dataset['DESCR'][:193] + '\n...')
#
# print('Target names:{}'.format(iris_dataset['target_names']))
#
# print('Feature names:\n{}'.format(iris_dataset['feature_names']))
#
# print('Type of data : {}'.format(type(iris_dataset['data'])))
#
# print('shape of data:{}'.format(iris_dataset['data'].shape))
################################3
# from sklearn.neighbors import KNeighborsClassifier
#
# # get data
# x = [[1], [2], [0], [0]]
# y = [1, 1, 0, 0]
#
# # 1 实例化
# estimator = KNeighborsClassifier(n_neighbors=2)
# # 2 fit方法训练
# estimator.fit(x, y)
# # 3 预测
# ret = estimator.predict([[2]])
# print(ret)
##############################4数据集划分
# x_train, x_test, y_train, y_test = train_test_split(iris_dataset.data, iris_dataset.target, test_size=0.3)
# print('训练集的特征值是：\n',x_train)
# print('测试集的特征值是：\n',x_test)
# print('训练集的目标值是：\n',y_train)
# print('测试集的目标值是：\n',y_test)

# print('训练集的目标值形状：\n',y_train.shape)
# print('测试集的目标值形状：\n',y_test.shape)
#############################5串一遍
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1 获取数据集
iris = load_iris()
# 2 数据基本处理
# 2.1 数据分割
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22, test_size=0.2)
print(x_train)
# 3 特征工程
# 3.1 实例化一个转换器
# transfer = StandardScaler()
# # 3.2 调用fit_transform方法
# x_train = transfer.fit_transform(x_train)
# x_test = transfer.fit_transform(x_test)
# # 4 机器学习（模型训练）
# # 4.1实例化一个估计器
# estimator = KNeighborsClassifier(n_neighbors=5)
# # 4.2模型训练
# estimator.fit(x_train, y_train)
# # 5 模型评估
# # 5.1 输出预测值
# y_pre = estimator.predict(x_test)
# print('预测值是：\n', y_pre)
# # 5.2 输出准确率
# ret = estimator.score(x_test, y_test)
# print('准确率是：\n', ret)
