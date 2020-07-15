# Vue Mall后台开发日志

像写博客那样记录自己是如何一步步写出来的。

## 一 初始化

#### 克隆代码

```shell
git clone https://github.com/PanJiaChen/vue-admin-template.git forntend

```
#### 修改`package.json`文件
```
# 依赖文件安装修改
# 个人学习vue较晚，更喜欢npm run serve启动。
"dev": "vue-cli-service serve", 改为 "serve": "vue-cli-service serve",

# 由于我用的webstorm eslint一直提示报错，之前搜过是版本太高

"eslint": "^6.7.2", 改为 "eslint": "^5.6.0",

```

#### 添加tagsview 快捷导航(标签栏导航)

参考 https://github.com/PanJiaChen/vue-admin-template/issues/349

也可以直接clone我这个 v1_init 版本

https://github.com/CoderCharm/FastAdmin/tree/v1_init

## 二 首页 echarts 集成

搜Github上面 Vue echarts 插件, star最高的就是这俩

https://github.com/ecomfe/vue-echarts (4.9k star 百度家开源的)
https://github.com/ElemeFE/v-charts  （5.8k star 饿了么开源的）

[v-charts文档](https://v-charts.js.org/#/) https://v-charts.js.org/#/

还是直接用`echarts`,这个库没人维护了, https://github.com/ElemeFE/v-charts/issues/842

https://echarts.apache.org/zh/api.html#echarts
