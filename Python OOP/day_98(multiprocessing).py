import concurrent.futures
import multiprocessing

import requests


def download_file(url, name):
    print(f"Started downloading {name}")
    response = requests.get(url)
    open(f"Python OOP/file{name}.jpg", "wb").write(response.content)
    print(f"Finished downloading {name}")


url = "https://picsum.photos/212/313"
# pros = []
# for i in range(1, 3):
#     # download_file(url, i)
#     p = multiprocessing.Process(target=download_file, args=[url, i])
#     p.start()
#     pros.append(p)
#
# for p in pros:
#     p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(12)]
    l2 = [i for i in range(12)]
    results = executor.map(download_file, l1, l2)
    for r in results:
        print(r)
