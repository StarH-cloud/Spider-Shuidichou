import requests


def download_image(url, file_path):
    # 夸克浏览器的 User - Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  QuarkPC/2.4.0.281',
        'Referer':'https://weibo.com/'
    }
    try:
        # 发送 GET 请求，添加请求头
        response = requests.get(url, stream=True, headers=headers)
        # 检查响应状态码
        response.raise_for_status()

        # 以二进制写入模式打开文件
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"图片已成功下载到 {file_path}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 错误发生: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"请求错误发生: {req_err}")
    except Exception as err:
        print(f"发生未知错误: {err}")


if __name__ == "__main__":
    # 替换为你要下载的图片 URL
    image_url = 'https://wx4.sinaimg.cn/large/007q0mqYly1hznj4l0ullj34mo62rx6z.jpg'
    # 替换为你想要保存图片名称
    save_path = '4.jpg'
    download_image(image_url, save_path)

