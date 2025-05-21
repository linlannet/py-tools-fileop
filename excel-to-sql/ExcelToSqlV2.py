import pandas as pd
import os
from datetime import datetime
import uuid
import json


def excel_to_sql(config_file):
    """
    从配置文件读取参数并生成SQL插入脚本

    参数:
    config_file (str): 配置文件路径

    返回:
    str: 生成的SQL文件路径
    """
    # 读取配置文件
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print(f"成功读取配置文件: {config_file}")
    except Exception as e:
        print(f"读取配置文件失败: {e}")
        return None

    # 从配置中获取参数
    excel_file = config.get('excel_file')
    output_file = config.get('output_file')
    table_name = config.get('table_name', 'school_ranking')
    schema = config.get('schema', 'public')
    mapping = config.get('mapping', {})
    use_uuid = config.get('use_uuid', False)
    pk_start = config.get('pk_start', 1)
    pk_name = config.get('pk_name', 'id')
    generate_table = config.get('generate_table', True)  # 新增：是否生成建表语句

    # 检查必要参数
    if not excel_file:
        print("错误: 配置文件中缺少'excel_file'参数")
        return None

    if not mapping:
        print("错误: 配置文件中缺少'mapping'参数")
        return None

    # 读取Excel文件
    try:
        df = pd.read_excel(excel_file)
        print(f"成功读取Excel文件，共{len(df)}条记录")
    except Exception as e:
        print(f"读取Excel文件失败: {e}")
        return None

    # 检查必要的列是否存在
    missing_columns = [excel_col for db_col, excel_col in mapping.items()
                       if excel_col not in df.columns]
    if missing_columns:
        print(f"错误: Excel文件缺少必要的列: {', '.join(missing_columns)}")
        return None

    # 自动生成输出文件名（如果未指定）
    if not output_file:
        base_name = os.path.splitext(os.path.basename(excel_file))[0]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{base_name}_sql_{timestamp}.sql"

    # 生成SQL脚本
    with open(output_file, "w", encoding="utf-8") as f:
        # 写入注释
        f.write(f"-- 从Excel导入数据到 {schema}.{table_name}\n")

        # 写入创建表语句（如果启用）
        if generate_table:
            f.write(f"-- 创建表 {schema}.{table_name}\n")
            f.write(f"CREATE TABLE IF NOT EXISTS {schema}.{table_name} (\n")

            if use_uuid:
                # 使用UUID主键
                f.write(f"    {pk_name} VARCHAR(36) PRIMARY KEY,\n")
            else:
                # 使用自增主键
                f.write(f"    {pk_name} INT PRIMARY KEY IDENTITY({pk_start},1),\n")

            # 添加其他列（根据映射关系）
            for db_col, excel_col in mapping.items():
                # 假设除了可能的排名列外，其他都是字符串类型
                if db_col.lower() in ['rank', 'ranking', 'score']:
                    f.write(f"    {db_col} INT,\n")
                else:
                    f.write(f"    {db_col} VARCHAR(255),\n")
            f.write(");\n\n")

        # 写入插入语句
        for _, row in df.iterrows():
            # 构建值列表
            values = []
            columns = list(mapping.keys())

            if use_uuid:
                # 生成UUID并添加到列和值列表中
                columns.insert(0, pk_name)
                values.append(f"'{str(uuid.uuid4())}'")

            # 添加其他值
            for db_col in mapping.keys():
                excel_col = mapping[db_col]
                value = row[excel_col]
                if pd.notna(value):
                    # 检查是否为数值类型
                    if db_col.lower() in ['rank', 'ranking', 'score']:
                        values.append(str(value))
                    else:
                        escaped_value = str(value).replace("'", "''")
                        values.append(f"'{escaped_value}'")
                else:
                    values.append("NULL")

            # 写入INSERT语句
            columns_str = ", ".join(columns)
            values_str = ", ".join(values)
            f.write(f"INSERT INTO {schema}.{table_name} ({columns_str}) VALUES ({values_str});\n")

    print(f"SQL脚本已生成: {output_file}")
    return output_file


def main():
    # 配置文件路径（请修改为实际配置文件路径）
    config_file_organ = "ConfigGlobalOrgan.json"

    # 执行转换
    output_file = excel_to_sql(config_file_organ)

    if output_file:
        print(f"SQL脚本已成功生成: {output_file}")
    else:
        print("生成SQL脚本失败")


if __name__ == "__main__":
    main()