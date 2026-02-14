import os
from dotenv import load_dotenv
from zai import ZhipuAiClient


load_dotenv()


class DreamAnalyzer:
    def __init__(self):
        api_key = os.getenv("ZHIPU_API_KEY")
        if not api_key:
            raise ValueError("ZHIPU_API_KEY environment variable not set")
        self.client = ZhipuAiClient(api_key=api_key)
    
    def analyze(self, dream_content):
        system_prompt = """你是一位温暖专业的心理学解梦师。请从心理学角度，结合弗洛伊德精神分析、荣格分析心理学等理论，对用户的梦境进行科学理性的解析。

请按以下格式解析：
🌙 梦境解析（潜意识含义，100字内）
💭 心理状态（当前情绪，100字内）
💡 建议（3条实用心理学建议）

要求：科学理性、温暖有同理心、适当使用emoji增强可读性，避免封建迷信内容。"""
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"请解析我的梦境：{dream_content}"}
        ]
        
        try:
            response = self.client.chat.completions.create(
                model="glm-4.7-flash",
                messages=messages,
                thinking={"type": "enabled"},
                max_tokens=2000,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"AI分析失败：{str(e)}")


if __name__ == "__main__":
    analyzer = DreamAnalyzer()
    test_dream = "我梦见自己在一片花海中奔跑，周围都是美丽的花朵，但突然天空变暗了，我开始感到害怕。"
    print("测试梦境分析...")
    result = analyzer.analyze(test_dream)
    print("分析结果：")
    print(result)
