# CSV数据分析智能工具

一个基于Streamlit和大语言模型的CSV数据分析工具，允许用户通过自然语言与数据交互。

## 功能特点

- 上传CSV文件并进行自动分析
- 使用自然语言查询数据
- 生成数据可视化（条形图、折线图、散点图）
- 自动提取数据洞察
- 优化的JSON响应处理

## 本地运行

1. 克隆仓库
2. 安装依赖
```bash
pip install -r requirements.txt
```
3. 运行应用
```bash
streamlit run "CSV数据分析智能工具.py"
```

## Streamlit Cloud部署说明

该应用已优化以在Streamlit Cloud上运行。为了处理依赖冲突，我们做了以下调整：

1. 创建了简化的`requirements_streamlit.txt`文件，包含最小必要依赖
2. 将`langchain`库降级到兼容的版本
3. 使用`PyMySQL`替代`mysqlclient`以避免构建问题

如果您在Streamlit Cloud上部署遇到问题，请参考`.streamlit/config.toml`中的配置。

## 使用说明

1. 输入DeepSeek API密钥
2. 上传CSV文件
3. 输入自然语言查询
4. 查看生成的分析和可视化

## 依赖项

主要依赖项包括：
- streamlit
- pandas
- matplotlib
- langchain
- openai（DeepSeek） 