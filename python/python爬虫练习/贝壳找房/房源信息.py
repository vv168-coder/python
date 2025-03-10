import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


# 设置字体为 SimHei（黑体）
matplotlib.rcParams['font.family'] = 'SimHei'
# 避免负号显示为方块
matplotlib.rcParams['axes.unicode_minus'] = False

#加载
driver = webdriver.Chrome(service=Service(r"D:\workspace\utils\chromedriver\最新\chromedriver-win64\chromedriver.exe"))

#get请求
driver.get("https://sy.ke.com/")

driver.maximize_window()
#进入租房页面
element_btn_category = driver.find_element(By.XPATH, '//ul/li[@class="CLICKDATA"][3]')
element_btn_category.click()

#关闭弹窗
element_btn_close = driver.find_element(By.CLASS_NAME, 'mask-close')
element_btn_close.click()

# #选择房源要求
# # #区域：大东
# # element_btn_addr = driver.find_element(By.XPATH, '//ul/li[@data-type="district"][1]')
# # element_btn_addr.click()
#
#方式：整租
element_btn_way = driver.find_element(By.XPATH, '//div[@id="filter"]/ul[5]/li[3]')
element_btn_way.click()
# #租金：1000~2000
# # 等待元素可见
# element_input_money = WebDriverWait(driver, 20).until(
#     EC.visibility_of_element_located((By.XPATH, '//div[@id="filter"]/ul[6]/li[9]/input[1]'))
# )
# element_input_money.send_keys('1000')
# element_input_moneyEnd = driver.find_element(By.XPATH, '//div[@id="filter"]/ul[6]/li[9]/input[2]')
# element_input_moneyEnd.send_keys('2000')
# element_btn_money = driver.find_element(By.XPATH, '//div[@id="filter"]/ul[6]/li[9]/span')
# element_btn_money.click()
# #户型：一室
# element_btn_bedroom = driver.find_element(By.XPATH, '//div[@id="filter"]/ul[7]/li[2]')
# element_btn_bedroom.click()
# #打开更多
# # element_btn_more = driver.find_element(By.XPATH, '//div[@class="filter__item--more"]')
# # element_btn_more.click()
# #打开更多按钮之前先等待它可点击
# element_btn_more = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//div[@class="filter__item--more"]'))
# )
# element_btn_more.click()
# # 电梯：有电梯
# element_btn_elevator = driver.find_element(By.XPATH, '//div[@id="filter"]/ul[last()]/li[3]')
# element_btn_elevator.click()
# time.sleep(3)

# 数据存储
data = []
#获取页面数据
def handle_detail_xpath(content):
    global  message_01, message_02, message_03, message_04, message_05, message_06, message_07, message_08, message_09, message_10
    soup = BeautifulSoup(content, 'lxml')
    all_house = soup.find_all("div", class_="content__list--item")
    for item in all_house:
        house_messages = item.find_all("p",class_="content__list--item--des")
        # 初始化地址列表
        house_addr = []
        # 遍历每个 house_message，查找地址
        for message in house_messages:
            addr_links = message.find_all("a", target="_blank")
            house_addr.extend([link.get_text(strip=True) for link in addr_links])
        # 获取所有消息文本
        # messages = [msg.get_text(strip=True) for msg in house_messages]
        house_title = item.find("a",class_="twoline")
        if house_title:
            title = house_title.string if house_title.string else "标题缺失"
        else:
            title = "标题缺失"
        # 价格
        house_money = item.find("em")
        if house_money:
            price = house_money.string.replace("元/月", "").replace(",", "").strip()
            # 检查价格是否为范围（以字符串的形式检查）
            if '-' in price:
                # 提取范围的最低值和最高值
                low_price, high_price = map(float, price.split('-'))
                price = (low_price + high_price) / 2  # 使用平均值，或者选择其中一个
            else:
                price = float(price)  # 转换为浮动类型
            price = float(price)  # 转换为浮动类型
        else:
            price = None  # 如果缺失价格

        try:
             # ... (爬取详情页的代码)
             # 获取详情链接
            # time.sleep(50)
            detail_link = item.find('a',class_="twoline")['href']  # 假设链接在<a>标签中
            if not detail_link.startswith("http"):
                detail_link = "https://sy.zu.ke.com" + detail_link  # 确保链接完整
                # 检查是否需要跳过特定链接
                if detail_link.startswith("https://sy.zu.ke.com/apartment"):

                    pass  # 跳过这个链接，不做任何输出
            # 请求详情页
            driver.get(detail_link)

            # 等待直到元素可见
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@id="info"]/ul[1]/li[last()]'))
            )

            message_01 = driver.find_element(By.XPATH, '//div[@id="info"]/ul[1]/li[2]').text.split('：')[-1]  # 面积
            # 提取面积中的数值
            area_value = re.search(r'\d+\.?\d*', message_01)  # 匹配数字（可能带小数点）
            message_01 = area_value.group(0) if area_value else "面积缺失"  # 获取匹配的数
            message_02 = driver.find_element(By.XPATH, '//div[@id="info"]/ul[1]/li[3]').text.split('：')[-1]  # 朝向
            message_03 = driver.find_element(By.XPATH, '//div[@id="info"]/ul[1]/li[8]').text.split('：')[-1]  # 楼层
            message_04 = driver.find_element(By.XPATH, '//div[@id="info"]/ul[1]/li[9]').text.split('：')[-1]  # 电梯
            message_05 = driver.find_element(By.XPATH, '//div[@id="info"]/ul[1]/li[11]').text.split('：')[-1]  # 车位
            message_06 = driver.find_element(By.XPATH, '//div[@id="info"]/ul[1]/li[12]').text.split('：')[-1]  # 用水
            message_07 = driver.find_element(By.XPATH, '//div[@id="info"]/ul[1]/li[14]').text.split('：')[-1]  # 用电
            message_08 = driver.find_element(By.XPATH, '//div[@id="info"]/ul[1]/li[15]').text.split('：')[-1]  # 燃气
            message_09 = driver.find_element(By.XPATH, '//div[@id="info"]/ul[1]/li[last()]')  # 采暖


            tags = driver.find_elements(By.CSS_SELECTOR, 'p.content__aside--tags i')
            found_tag = False
            for tag in tags:
                if '近地铁' in tag.text:
                    message_10 = tag.text.strip()
                    found_tag = True
                    break

            if not found_tag:
                message_10 = "无"  # 如果没有找到“近地铁”

            if message_09:
                message_09 = message_09.text.split('：')[-1]
            else:
                print("未找到匹配的元素，请检查选择器或页面结构。")
        except Exception as e:
            print(f"发生错误: {e}")



        house_data = {
            "title": title,
            "address":  house_addr[0] if len(house_addr) > 1 else "地址缺失",
            # "messages": messages,
            "price": price,
            '面积m²': message_01 if message_01 else "面积缺失",
            '朝向': message_02 if message_02 else "朝向缺失",
            '楼层': message_03 if message_03 else "楼层缺失",
            '电梯': message_04 if message_04 else "电梯缺失",
            '车位': message_05 if message_05 else "车位缺失",
            '用水': message_06 if message_06 else "用水缺失",
            '用电': message_07 if message_07 else "用电缺失",
            '燃气': message_08 if message_08 else "燃气缺失",
            '采暖': message_09 if message_09 else "采暖缺失",
            "近地铁": message_10

        }
        print(house_data)
        if price is not None:  # 只保存有价格的数据
            data.append(house_data)

def main():
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }

    # 爬取第一页
    url_first_page = "https://sy.zu.ke.com/zufang/rt200600000001l0/?showMore=1"
    response_first_page = requests.get(url=url_first_page, headers=header)
    handle_detail_xpath(response_first_page.text)

    # 爬取2~100
    for i in range(2,101):
        url = "https://sy.zu.ke.com/zufang/pg{}rt200600000001l0/#contentList".format(i)
        response = requests.get(url=url,headers=header)
        handle_detail_xpath(response.text)

    # 数据处理
    df= pd.DataFrame(data)
    df.to_excel("租房数据.xlsx", index=False)
    # 确保 price 列为数值类型
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # 检查是否还有有效的价格数据
    print(df['price'].describe())  # 打印描述信息以检查数据

    average_prices = df.groupby('address')['price'].mean().reset_index()

    # 可视化
    plt.figure(figsize=(10, 5))
    plt.plot(average_prices['address'], average_prices['price'], marker='o')
    plt.title('Average Price per Address')
    plt.xlabel('Address')
    plt.ylabel('Average Price (元/月)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
