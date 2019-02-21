<div align="center">

## TickPicBed

**基于Flask的聚合图床**

[![GitHub issues](https://img.shields.io/github/issues/jiangyx3915/TickPicBed.svg)](https://github.com/jiangyx3915/TickPicBed/issues)
[![GitHub forks](https://img.shields.io/github/forks/jiangyx3915/TickPicBed.svg)](https://github.com/jiangyx3915/TickPicBed/network)
[![GitHub stars](https://img.shields.io/github/stars/jiangyx3915/TickPicBed.svg)](https://github.com/jiangyx3915/TickPicBed/stargazers)
[![GitHub license](https://img.shields.io/github/license/jiangyx3915/TickPicBed.svg)](https://github.com/jiangyx3915/TickPicBed)
</div>
<br>

## 功能 特色

* 支持 web 上传图片
* 支持 API 上传图片
* 支持图床:
    
    * 搜狗
    * 新浪 (私有+公共)
    * SMMS 
    * 奇虎 (360)
    * 百度  
    * 阿里
    * 京东
    * Upload.cc
    * Flickr
    * 网易
    * 掘金
    * 本地 (由于需要对接后台，正在紧张开发中)

    
* API 可以设置 token 可以私用，也可以选择关闭 API，只保留 web 上传
* 可以设置是否开启新浪图床上传（因为新浪图床需要登录自己的账号）
* 可以设置允许上传的图片最大大小 和 一次性上传的最多张数
* 后台控制，用户和管理员双后台
* 支持Docker部署
    


## 项目截图

![首页](https://ws4.sinaimg.cn/large/ed24e93ely1fzeamnpm6yj21hc0o7n31.jpg)

![无上传图片样式](https://ws2.sinaimg.cn/large/ed24e93ely1fzeao21i4wj21hb0odad1.jpg)



## 部署使用


## API 上传

### API 上传实例

**图片上传 V1 接口**

| 功能 | 图片上传接口 |
| --- | --- |
| HTTP 请求方式 |  POST |
| URL  | http://pic.jiangyixin.top/api/v1/upload|

**请求参数**

| 参数名称 | 类型 | 是否必须|描述|
| --- | --- |---| --- |
| image | File | 是 | 表单名称,上传图片|
| token  | String | 是 | 认证所必须的 token ，如果站在没有开启则留空即可 |
| platform  | String | 是 | 所选择的 API 平台 类型 |

**apiSelect可选参数**

| apiSelect 可选参数 | 参数说明
| --- | ---|
| SouGou| 搜狗图床|
|Sina|新浪图床|
|Smms|SMMS 图床|


**成功上传返回**

```json
{
    "code": 200,
    "msg": "上传成功",
    "data": {
        "name": "Snipaste_2018-08-28_01-17-58.png",
        "url": "https://img04.sogoucdn.com/app/a/100520146/0dcb98aadb59c6b29dc0832eb7cc094a"
    }
}

```

```json
{
    "code": 200,
    "msg": "上传成功",
    "data": {
        "name": "Snipaste_2018-08-28_01-17-58.png",
        "url": "https://i.loli.net/2018/11/05/5be038b1b4af6.png"
    }
}
```

**失败返回值**

上传出错返回值

```json
{
    "code": 500,
    "msg": "上传失败"
}
```

API 未开启返回值

```json
{
    "code": 405,
    "msg": "Method not allowed"
}
```
 Token 验证失败返回值
 
```json
{
    "code": 403,
    "msg": "Forbidden"
}
```

选择文件为空返回值

```json

{
    "code": 500,
    "msg": "No files were uploaded."
}

```

文件太大返回值

```json

{
    "code": 500,
    "msg": "File is too large."
}

```

## TODO 

* [] API 上传

* [ ] API 自动文档

* [ ] API v2 版本分发上传,返回所有图床储存链接 

* [ ] 用户系统

* [ ] 前后端分离,Vue 驱动前端

* [ ] 后台控制

* [ ] 本地上传，各大平台对接储存

* [ ] 使用 MySQL 而不是 JSON
