import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family']='STfangsong'
data=pd.read_csv("digital_marketing_campaign_dataset.csv")

df = pd.DataFrame(data)
# 显示数据的前几行
print(data.head())
# 描述性统计
print(data.describe())
# 数据信息
print(data.info())
# 处理缺失值（选择删除或填补）
data = data.dropna()  # 删除含有缺失值的行

# 绘制年龄的直方图和密度图
plt.figure(figsize=(12, 6))
sns.histplot(data['Age'], bins=30, kde=True)  # kde=True表示同时绘制密度曲线
plt.title('客户年龄分布')
plt.xlabel('年龄')
plt.ylabel('频数')
plt.grid()
plt.show()

# 计算性别占比
gender_counts = data['Gender'].value_counts()

# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('客户性别比例')
plt.axis('equal')  # 确保饼图是圆形
plt.show()

# 绘制条形图
plt.figure(figsize=(8, 6))
sns.barplot(x=gender_counts.index, y=gender_counts.values)
plt.title('客户性别比例')
plt.xlabel('性别')
plt.ylabel('数量')
plt.grid(axis='y')
plt.show()


# 5. 可视化分析
# 5.1 年龄与转化率的关系
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age', y='ConversionRate', data=data)
plt.title('年龄与转化率的关系')
plt.xlabel('年龄')
plt.ylabel('转化率')
plt.show()

# 5.2 性别与转化率的关系
plt.figure(figsize=(10, 6))
sns.barplot(x='Gender', y='ConversionRate', data=data, estimator='mean', errorbar=None)
plt.title('性别与平均转化率的关系')
plt.xlabel('性别')
plt.ylabel('平均转化率')
plt.show()


# 5.4 点击率与转化率的关系
plt.figure(figsize=(10, 6))
sns.scatterplot(x='ClickThroughRate', y='ConversionRate', data=data, alpha=0.7)
plt.title('点击率与转化率的关系')
plt.xlabel('点击率')
plt.ylabel('转化率')
plt.show()
#
# 5.5 网站访问次数与转化率的关系
plt.figure(figsize=(10, 6))
sns.scatterplot(x='WebsiteVisits', y='ConversionRate', data=data, alpha=0.7)
plt.title('网站访问次数与转化率的关系')
plt.xlabel('访问网站的总次数')
plt.ylabel('转化率')
plt.show()

# 5.6 营销活动花销与转化率的关系
plt.figure(figsize=(10, 6))
sns.scatterplot(x='AdSpend', y='ConversionRate', data=data, alpha=0.7)
plt.title('营销活动花销与转化率的关系')
plt.xlabel('营销活动花销')
plt.ylabel('转化率')
plt.show()

# 5.7 营销活动渠道与转化率的关系
plt.figure(figsize=(10, 6))
sns.barplot(x='CampaignChannel', y='ConversionRate', data=data, estimator='mean', errorbar=None)
plt.title('营销活动渠道与平均转化率的关系')
plt.xticks(rotation=45)
plt.xlabel('营销活动渠道')
plt.ylabel('平均转化率')
plt.show()

# 5.8 营销活动类型与转化率的关系
plt.figure(figsize=(10, 6))
sns.barplot(x='CampaignType', y='ConversionRate', data=data, estimator='mean', ci=None)
plt.title('营销活动类型与平均转化率的关系')
plt.xticks(rotation=45)
plt.xlabel('营销活动类型')
plt.ylabel('平均转化率')
plt.show()

# 5.9 社交分享次数与转化率的关系
plt.figure(figsize=(10, 6))
sns.scatterplot(x='SocialShares', y='ConversionRate', data=data, alpha=0.7)
plt.title('社交分享次数与转化率的关系')
plt.xlabel('社交分享次数')
plt.ylabel('转化率')
plt.show()

# 5.10 营销邮件打开次数与转化率的关系
plt.figure(figsize=(10, 6))
sns.scatterplot(x='EmailOpens', y='ConversionRate', data=data, alpha=0.7)
plt.title('营销邮件打开次数与转化率的关系')
plt.xlabel('营销邮件打开次数')
plt.ylabel('转化率')
plt.show()
#
# 5.11 营销邮件点击率与转化率的关系
plt.figure(figsize=(10, 6))
sns.scatterplot(x='EmailClicks', y='ConversionRate', data=data, alpha=0.7)
plt.title('邮件链接点击次数与转化率的关系')
plt.xlabel('邮件链接点击次数')
plt.ylabel('转化率')
plt.show()

# 5.12 购买次数与转化率的关系
plt.figure(figsize=(10, 6))
sns.boxplot(x='PreviousPurchases', y='ConversionRate', data=data)
plt.title('购买次数与转化率的关系')
plt.xlabel('购买次数')
plt.ylabel('转化率')
plt.show()

# 5.13 忠诚度积分与转化率的关系
plt.figure(figsize=(10, 6))
sns.boxplot(x='LoyaltyPoints', y='ConversionRate', data=data)
plt.title('忠诚度积分与转化率的关系')
plt.xlabel('忠诚度积分')
plt.ylabel('转化率')
plt.show()

# 5.14 年龄与收入的关系
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Income', data=data, alpha=0.7)
plt.title('年龄与客户年收入的关系')
plt.xlabel('年龄')
plt.ylabel('客户年收入')
plt.show()

# 5.15 性别与客户年收入的关系
plt.figure(figsize=(10, 6))
sns.barplot(x='Gender', y='Income', data=data, estimator='mean', ci=None)
plt.title('性别与平均收入的关系')
plt.xlabel('性别')
plt.ylabel('平均年收入')
plt.show()

# 5.16 广告平台与转化率的关系
plt.figure(figsize=(10, 6))
sns.barplot(x='AdvertisingPlatform', y='ConversionRate', data=data, estimator='mean', ci=None)
plt.title('广告平台与平均转化率的关系')
plt.xticks(rotation=45)
plt.xlabel('广告平台')
plt.ylabel('平均转化率')
plt.show()

# 5.17 广告工具与转化率的关系
plt.figure(figsize=(10, 6))
sns.barplot(x='AdvertisingTool', y='ConversionRate', data=data, estimator='mean', ci=None)
plt.title('广告工具与平均转化率的关系')
plt.xticks(rotation=45)
plt.xlabel('广告工具')
plt.ylabel('平均转化率')
plt.show()









