# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
# 默认按钮颜色是 secondary
from toolbox import clear_line_break


def get_core_functions():
    return {
        "優化代码": {
            "Prefix":   r"Review the following code and refactor it to make it more DRY and adopt the SOLID programming principles." + "\n```\n",
            "Suffix":   "\n```\n",
            "Color": "stop",
        },
        "代碼修正":{
            "Prefix":   r"Review this code for errors and refactor to fix any issues." + "\n```\n",
            "Suffix":   "\n```\n",
            "Color": "stop",
        },
        "解释代码": {
            "Prefix":   r"请解释以下代码：" + "\n```\n",
            "Suffix":   "\n```\n",
        },
        "找图片": {
            "Prefix":   r"我需要你找一张网络图片。使用Unsplash API(https://source.unsplash.com/960x640/?<英语关键词>)获取图片URL，" +
                        r"然后请使用Markdown格式封装，并且不要有反斜线，不要用代码块。现在，请按以下描述给我发送图片：" + "\n\n",
            "Suffix":   r"",
        },

    }
