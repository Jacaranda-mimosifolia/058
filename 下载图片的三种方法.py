import os

os.makedirs('D:\\image', exist_ok=True)
IMAGE_URL = "https://w.wallhaven.cc/full/l3/wallhaven-l36l8q.jpg"


# def urllib_download():
#     from urllib.request import urlretrieve
#     urlretrieve(IMAGE_URL, './image/img1.png')


def request_download():
    import requests
    r = requests.get(IMAGE_URL)
    with open('D:\\image\\img2.png', 'wb') as f:
        f.write(r.content)


def chunk_download():
    import requests
    r = requests.get(IMAGE_URL, stream=True)
    with open('D:\\image\\img3.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)


# urllib_download()
# print('download img1')
request_download()
print('download img2')
chunk_download()
print('download img3')
