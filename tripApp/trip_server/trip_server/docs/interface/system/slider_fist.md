## 首页轮播图的接口
### 请求地址
/system/slider/list
### 调用方式
GET
### 请求参数
<table>
    <thead>
        <tr>
            <th>字段</th>
            <th>必选</th>
            <th>类型</th>
            <th>说明</th>
        </tr>
    </thead>
 <tbody>
        <tr>
            <td>types</td>
            <td>true</td>
            <td>int</td>
            <td>轮播图类型(10：首页轮播)</td>
    </tbody>
</table>

### 返回结果

```
{
 "meta":{
    "total_count":3,
    "page_count":2,
    "current_page":1,
 },
 "objects":[
        {
            "id":1,
            "name":"轮播图1",
            "desc":null,
            "img":"http://djang.xxx.com/medias/slider/banner1.jpg",
            "target_url":null
        },
        {
            "id":2,
            "name":"轮播图2",
            "desc":null,
            "img":"http://djang.xxx.com/medias/slider/banner2.jpg",
            "target_url":null
        }
    ]
 }
```

## 返回字段说明
<table class="table table-hover table-condensed">
    <thead>
        <tr>
            <th>
                字段
            </th>
            <th>
                类型
            </th>
            <th>
                说明
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>meta</td>
            <td></td>
            <td>分页源数据，解释如下</td>
        </tr>
        <tr>
            <td>total_count</td>
            <td>int</td>
            <td>根据传入的条件检索出的记录条</td>
        </tr>
        <tr>
            <td>current_count</td>
            <td>int</td>
            <td>当前第几页</td>
        </tr>
        <tr>
            <td>page_count</td>
            <td>int</td>
            <td>总页数</td>
        </tr>
<tr class="info">
            <td>page_count</td>
            <td>Array</td>
            <td>objects为返回的对象列表</td>
        </tr>
    </tbody>
</table>

## 分页
### 返回字段说明

<table class="table table-hover table-condensed">
    <thead>
        <tr>
            <th>
                字段
            </th>
            <th>
                类型
            </th>
            <th>
                说明
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>meta</td>
            <td></td>
            <td>分页元数据，解释如下</td>
        </tr>
        <tr class="info">
            <td>objects</td>
            <td>Array</td>
            <td>objects 为轮播图对象，详细如下</td>
        </tr>
        <tr>
            <td>pk</td>
            <td>String</td>
            <td>名称</td>
        </tr>
        <tr>
            <td>desc</td>
            <td>String</td>
            <td>描述信息</td>
        </tr>
        <tr>
            <td>img</td>
            <td>String</td>
            <td>图片地址</td>
        </tr>
        <tr>
            <td>target_url</td>
            <td>String</td>
            <td>跳转html链接地址</td>
        </tr>
    </tbody>
</table>