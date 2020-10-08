from sklearn.linear_model import LinearRegression

# 线性回归
# 获取数据
x = [[80, 86],
     [82, 80],
     [85, 78],
     [90, 90],
     [86, 82],
     [82, 90],
     [78, 80],
     [92, 94]]
y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]
# 模型训练
# 1.实例化一个估算其
estimator = LinearRegression()
# 2.调用fit方法进行模型训练
estimator.fit(x, y)
#查看系数
coef = estimator.coef_
print('系数是:\n',coef)
#预测
print('预测值：\n',estimator.predict([[70,90]]))