
## 版本历史
```

1.2     2024-04-20     更新表和字段替换的Key-Value信息，增加FRAME层288张产品表原始开发SQL和产品混淆表名后的SQL
1.1     2023-12-27     更新目录，调整说明，配置文件存放部分示例
1.0     2023-12-18     初始化资源目录，修改README文件

```

## before
文件替换之前保留的原始版本


## config
存放配置文件的路径，将table和column的key-value键值对直接用excel进行存储
</br>
[table-key-value.xlsx](./config/table-key-value.xlsx)
</br>
[column-key-value.xlsx](./config/column-key-value.xlsx)

#@ workdir
待替换的工作目录，当程序运行时，可将被替换资源放入此路径下
可对xml、txt、SQL、js、java、md等代码文件进行规则替换