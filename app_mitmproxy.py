import json
import time
import requests


def response(flow):
    refresh_url = 'https://edith.xiaohongshu.com/api/sns/v6/'
    if flow.request.url.startswith(refresh_url):
        for data in json.loads(flow.response.text)['data']:
            article = dict()
            # 标题
            article['title'] = data['display_title']
            # 描述
            article['desc'] = data['desc']
            # 图片列表
            images_list = data['images_list']
            # 具体图片url
            image_url = list()
            for image in images_list:
                image_url.append(image['url_size_large'])
            # 保存到本地
            data = requests.get(image_url[0])
            file = open('./' + str(image_url[0]).split('/')[3].split('?')[0] + '.jpg', "wb")
            file.write(data.content)
            file.close()
            article['images'] = image_url
            article['time'] = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(time.time()))
            print(article)
            print('-------------------')
        print(flow.response.text)
        print('++++++++++++++++++++++++++++++++++++++++++++++++')
        print(flow.request.url)
        print('=================================================')