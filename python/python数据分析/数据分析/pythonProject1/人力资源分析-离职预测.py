import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family']='STfangsong'
data = pd.read_csv('HR_comma_sep.csv')

# 数据概览
print(data.head())
print(data.info())

# 数据预处理
data['left'] = data['left'].astype('int')


plt.figure(figsize=(8, 5))
satisfaction_counts = data['satisfaction_level'].value_counts()
satisfaction_counts.plot(kind='bar', color='skyblue')
plt.title('员工满意度分析')
plt.xlabel('满意度水平')
plt.xticks(rotation=45)
plt.ylabel('员工数量')
plt.xticks(rotation=0)
plt.show()

satisfaction_ratio = data['satisfaction_level'].value_counts(normalize=True) * 100
print('满意度比例：')
print(satisfaction_ratio)

# 2. 项目数量与满意度的关系
plt.figure(figsize=(8, 5))
sns.boxplot(x='number_project', y='satisfaction_level', data=data)
plt.title('项目数量与员工满意度关系')
plt.xlabel('项目数量')
plt.ylabel('满意度水平')
plt.show()

# 3. 工作时间与满意度的关系
plt.figure(figsize=(8, 5))
sns.scatterplot(x='average_montly_hours', y='satisfaction_level', data=data)
plt.title('平均工作时间与满意度关系')
plt.xlabel('平均每月工作小时')
plt.ylabel('满意度水平')
plt.show()

# 4. 员工流失率分析
turnover_rate = data['left'].mean() * 100
print(f'员工流失率: {turnover_rate:.2f}%')

# 5. 绩效评估与晋升关系
plt.figure(figsize=(8, 5))
sns.countplot(x='promotion_last_5years', hue='left', data=data)
plt.title('绩效评估与晋升关系')
plt.xlabel('是否晋升 (1=是, 0=否)')
plt.ylabel('员工数量')
plt.legend(title='离职', loc='upper right', labels=['没有离职', '离职'])
plt.show()

# 6. 部门间满意度比较
plt.figure(figsize=(10, 6))
sns.boxplot(x='sales', y='satisfaction_level', data=data)
plt.title('不同部门员工满意度比较')
plt.xlabel('部门')
plt.ylabel('满意度水平')
plt.xticks(rotation=45)
plt.show()

# 7. 薪资水平与满意度的关系
plt.figure(figsize=(8, 5))
sns.boxplot(x='salary', y='satisfaction_level', data=data)
plt.title('薪资水平与满意度的关系')
plt.xlabel('薪资水平')
plt.ylabel('满意度水平')
plt.show()

# 8. 工作事故与满意度的关系
plt.figure(figsize=(8, 5))
sns.boxplot(x='Work_accident', y='satisfaction_level', data=data)
plt.title('工作事故对员工满意度的影响')
plt.xlabel('工作事故 (1=是, 0=否)')
plt.ylabel('满意度水平')
plt.show()

# 9. 员工在职时间与满意度的关系
plt.figure(figsize=(8, 5))
sns.boxplot(x='time_spend_company', y='satisfaction_level', data=data)
plt.title('员工在职时间与满意度的关系')
plt.xlabel('在职时间（年）')
plt.ylabel('满意度水平')
plt.show()

# 11. 员工绩效评估分布
plt.figure(figsize=(8, 5))
sns.histplot(data['last_evaluation'], bins=10, kde=True, color='orange')
plt.title('员工绩效评估分布')
plt.xlabel('绩效评估分数')
plt.ylabel('员工数量')
# plt.show()
