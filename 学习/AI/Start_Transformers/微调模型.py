import openai

def openai_1():
    with open('GPT.txt', 'r')as file:
        key = file.read().strip()

    openai.api_key = key
    openai.proxy = '127.0.0.1:7890'

if __name__ == '__main__':
    data4 = 1000
    data1 = []
    with open('69万问题2.txt', 'r', encoding='utf-8') as f:
        while data4:
            data1.append(eval(f.readline()))
            data4 -= 1

    model1 = 'fenlei'
    'openai tools fine_tunes.prepare_data -f sport2.jsonl -q'
    'openai api fine_tunes.create -t "{}" -v "{}" --compute_classification_metrics --classification_positive_c'
    # 微调目前仅适用于以下基础模型：davinci、curie、babbage和ada。
    """
    条件生成是需要在给定某种输入的情况下生成内容的问题。这包括释义、总结、实体提取、编写给定规范的产品描述、聊天机器人等。对于此类问题，我们建议：
    在提示末尾使用分隔符，例如\n\n###\n\n. 当您最终向您的模型发出请求时，请记住还要附加此分隔符。
    在完成结束时使用结束标记，例如 END
    请记住在推理过程中将结束标记添加为停止序列，例如stop=[" END"]
    目标是至少 ~500 个示例
    确保提示+完成不超过 2048 个标记，包括分隔符
    确保示例具有高质量并遵循相同的所需格式
    确保用于微调的数据集在结构和任务类型上与模型将用于的数据集非常相似
    使用较低的学习率和仅 1-2 个时期往往更适合这些用例
    """
    result = openai.Completion.create(
        model=model1,
        prompt=data1[0]['hot'] + '\n\n###\n\n',
        max_tokens=1,
        temperature=0,
        logprobs=2
    )


