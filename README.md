# py-tools-fileop
## 介绍
PYTHON进行文件操作工具代码，包括一系列工具和方法

## 版本历史
```
2025-03-20      增加OCR相关的代码，进行图片信息识别
2024-04-20      增加KEY/VALUE信息批量替换代码

```

1.file-replace-key-value: 通过key-value定义，快速实现将key替换为value，针对before目录下的文件进行全部替换;
功能如：配置KEY/VALUE信息，选择某个文件目录，对目录下的限定后缀文件进行批量替换
```
应用场景：
数据库内表名整体替换为混淆表名
数据库内字段替换为混淆的字段名
```
2. ocr-webpage-tpl-api: 通过对webpage页面截图后标绘，设置识别区域，然后对标绘区域的文字进行OCR识别，并封装为api提供给后台使用
[tpl](./ocr-webpage-tpl-api/README.md)

## 参与贡献
1.  Fork 本仓库
2.  新建 Feat_1.0.0 分支
3.  提交代码
```
git config user.name linlaninfo
git config user.email linlanio@qq.com
```
4. 新建 Pull Request
5. 创建和提交tag
```
创建
git tag -a v1.0.0 -m "create new tag v1.0.0"
```
6. 其他
