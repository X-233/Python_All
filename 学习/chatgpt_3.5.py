# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import openai

def openai_1():
    key = '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'

    openai.api_key = key

    openai.proxy = '127.0.0.1:7890'
    # openai.verify_ssl_certs = False
    # models = openai.Model.list()

def get_content(l_1=None):
    data = {
        "model": "gpt-3.5-turbo-0301",
        'messages': l_1,
    }
    completion = openai.ChatCompletion.create(
        model=data["model"],
        messages=data["messages"],
    )
    content = completion['choices'][0]['message']
    return content

if __name__ == '__main__':
    openai_1()
    list_1 = []

    # 超过5句话停止，并且保存对话内容，自己修改就行（把5改了就行）
    print('空格回车退出')
    while True:
        word = input('I:\t')
        if word == ' ':
            break
        # word = 'I: 你好'
        word_1 = {"role": "user", "content": word}
        list_1.append(word_1)
        data_1 = get_content(l_1=list_1)
        print('AI:\t' + data_1['content'].strip())
        word_2 = {"role": "assistant", "content": data_1['content']}
        list_1.append(word_2)

    with open('test.txt', 'a', encoding='utf-8') as f:
        for i in list_1:
            f.write(str(i) + '\n')
