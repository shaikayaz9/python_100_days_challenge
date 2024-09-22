# Multi Processing python


import multiprocessing
# import multiprocessing.process
import requests

def DownlaodFile(url , name):
    responce = requests.get(url)
    open(f"files2/pic{name}.jpg", "wb").write(responce.content)


url = "https://picsum.photos/400/700"
for i in range(3):
    DownlaodFile(url , i)




# prop = []
# for i in range(3):
#     # DownlaodFile(url , i)
#     p = multiprocessing.process(target=DownlaodFile , args=[url , i])
#     p.start()
#     prop.append(p)

# for p in prop:
#     p.join()