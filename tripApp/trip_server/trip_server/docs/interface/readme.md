# 旅游网的接口文档
RESTful风格接口

* 200 请求数据成功
* 201 提交数据成功
* 400 参数错误
* 403 未登录
* 404 目标资源丢失
* 500 服务器正忙
## 接口请求地址
1. 测试环境
http:test.xxx.top
2. 生成环境
http://www.xx.com
## 错误代码文字提示
```
{
    "error_code":"400000"
    "error_msg":"该字段不能为空"
    "error_list":{
        "password":["该字段不能为空"]
    }
}
```
## 请求头添加内容

## 分页

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
        <tr>
            <td>total_count</td>
            <td>int</td>
            <td>分页元数据，解释如下</td>
        </tr>
        <tr>
            <td>meta</td>
            <td>int</td>
            <td>分页元数据，解释如下</td>
        </tr>
    </tbody>
</table>
