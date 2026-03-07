from datetime import datetime
import random

VOICE = [
    "旧规章",
    "失效的规定",
    "无人解释的习惯",
    "被沿用太久的命令",
    "没有来源的通知",
    "奇怪但被默认执行的要求",
]

TEXTURE = [
    "冷静",
    "不解释",
    "像默认所有人都明白",
    "略显不安",
    "语气克制",
    "带一点不合理",
]

STRANGE = [
    "允许一点荒谬",
    "允许模糊对象",
    "允许不完整逻辑",
    "不要像生活建议",
    "不要像哲学句子",
]

def build_prompt(mode: str, history: list[str]) -> str:
    voice = random.choice(VOICE)
    texture = random.choice(TEXTURE)
    strange = random.choice(STRANGE)

    return f"""生成一句中文命令。

要求：
- 只输出一句
- 不要解释，不要思考过程，不要英文
- 不要引用任何作品或世界观
- 风格像{voice}
- 语气{texture}
- {strange}

句子特点：
- 看起来像一条奇怪的规矩
- 不需要说明原因
- 不要像生活建议
- 不要像诗句或谜语
- 长度 8 到 22 个汉字


现在只输出一句命令："""