import urllib.request
import time
from os import fsync
from sys import exit

test_link = "http://download.thinkbroadband.com/10MB.zip"

file = ""
url = input("File url: ")
if url == "_test":
    url = test_link
    file = "test.zip"
else:
    file = input("Save to: ")

print("\nInitializing Download...\n")
try:
    req = urllib.request.urlopen(url)
    print("Request Obtained\n")
    file_size = int(req.getheader("Content-Length"))
except urllib.request.HTTPError:
    print("404: File not found")
    q = input("Press <Enter> to exit")
    exit()
except ValueError:
    print("Bad Url")
    q = input("Press <Enter> to exit")
    exit()

file_size_dl = 0
chunk = 16 * 1024

total_elapsed_time = 0

with open(file, 'wb') as fp:
    while True:
        start_time = time.time()
        buffer = req.read(chunk)
        if not buffer:
            break
        end_time = time.time()
        delta_time = end_time - start_time
        total_elapsed_time += delta_time

        file_size_dl += len(buffer)
        try:
            status = "Downloading... ({0:.2f}MB of {1:.2f}MB at {3:.1f}KBPS) {2:.2f}%".format(file_size_dl/1024**2, file_size/1024**2, (file_size_dl/file_size)*100, (file_size_dl/1024)/total_elapsed_time)
        except ArithmeticError:
            status = "Downloading... ({0:.2f}MB of {1:.2f}MB at {3:.1f}KBPS) {2:.2f}%".format(file_size_dl/1024**2, file_size/1024**2, (file_size_dl/file_size)*100, 0)
        print(status, end='\r')
        
        fp.write(buffer)
        fp.flush()
        fsync(fp)

print("\n\nDownload Complete\n")

print("Total download time: {0:.2f}\n".format(total_elapsed_time))

q = input("Press <Enter> to exit")