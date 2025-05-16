"""
测试csv_utils模块的功能

此脚本用于测试csv_utils.py中的extract_json_from_text函数
是否能够正确解析各种格式的输出结果。
"""

import unittest
from csv_utils import extract_json_from_text


class TestCSVUtils(unittest.TestCase):

    def test_clean_json(self):
        """测试正常的JSON格式"""
        text = '{"answer": "测试回答"}'
        result = extract_json_from_text(text)
        self.assertEqual(result, {"answer": "测试回答"})

    def test_json_with_extra_text(self):
        """测试带有额外文本的JSON"""
        text = 'Thought: 计算平均值\nAction: python_repl_ast\n{"answer": "测试回答"}'
        result = extract_json_from_text(text)
        self.assertEqual(result, {"answer": "测试回答"})

    def test_multiple_json(self):
        """测试多个JSON"""
        text = '{"temp": "临时"} {"answer": "测试回答"}'
        result = extract_json_from_text(text)
        self.assertTrue("temp" in result or "answer" in result)

    def test_invalid_json(self):
        """测试无效JSON"""
        text = 'Invalid Format: Missing "Action:" after "Thought:"'
        result = extract_json_from_text(text)
        self.assertTrue("answer" in result)  # 应该返回默认响应

    def test_complex_output(self):
        """测试复杂输出格式"""
        text = """Thought: To find out which profession has the most people, I need to count the occurrences of each profession in the 'Profession' column of the dataframe and then identify the one with the highest count.

Action: python_repl_ast
Action Input: df['Profession'].value_counts().idxmax()
Healthcare{"answer": "人数最多的职业是Healthcare"}Invalid Format: Missing 'Action:' after 'Thought:'{"answer": "人数最多的职业是Healthcare"}"""

        result = extract_json_from_text(text)
        self.assertEqual(result, {"answer": "人数最多的职业是Healthcare"})


if __name__ == "__main__":
    unittest.main()
