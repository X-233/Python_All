import os
import shutil
import time
import requests

# Github仓库的API地址
api_url = "https://api.github.com/repos/{}/{}/tarball/{}"

# 仓库所有者和名称
owner = "your_username"
repo_name = "your_repository"

# 保存代码的路径
save_path = "/home/python"

# 获取代码的分支或标签
branch_or_tag = "main"

# 循环获取最新代码
while True:
    # 构造API地址
    url = api_url.format(owner, repo_name, branch_or_tag)

    # 发送HTTP请求
    response = requests.get(url, stream=True)

    # 如果响应码为200，则表示请求成功
    if response.status_code == 200:
        # 获取文件名
        filename = response.headers.get("Content-Disposition").split("filename=")[-1]

        # 构造保存路径
        save_pathname = os.path.join(save_path, filename)

        # 删除已存在的文件
        if os.path.exists(save_pathname):
            os.remove(save_pathname)

        # 创建文件并写入数据
        with open(save_pathname, "wb") as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)

        # 输出日志
        print("成功获取最新代码，并保存到：{}".format(save_pathname))
    else:
        # 输出错误日志
        print("获取最新代码失败，错误码：{}".format(response.status_code))

    # 休眠60秒
    time.sleep(60)
