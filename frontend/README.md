## Mall 项目后台

> 这是配套 个人练习的 https://github.com/CoderCharm/Mall 而写的后台管理。
> 基于花裤衩的开源 https://github.com/PanJiaChen/vue-admin-template 后台模版构建，感谢花裤衩。


## 项目自定义初始化

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

#### 安装启动

```
# 安装依赖
npm install

# 建议不要直接使用 cnpm 安装以来，会有各种诡异的 bug。可以通过如下操作解决 npm 下载速度慢的问题
npm install --registry=https://registry.npm.taobao.org

# 启动服务
npm run dev

```

#### 添加tagsview 快捷导航(标签栏导航)

参考 https://github.com/PanJiaChen/vue-admin-template/issues/349

也可以直接clone我这个 v1_init 版本的


## 参考
- [vue-element-admin文档](https://panjiachen.github.io/vue-element-admin-site/zh/guide/) https://panjiachen.github.io/vue-element-admin-site/zh/guide/
