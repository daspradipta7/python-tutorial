import threading
import requests
import time

def download(url):
    print(f"Starting download from {url}...")
    resp = requests.get(url)

    if resp.status_code == 200:
        # Extract the file name (e.g., "jpeg", "png") from the URL
        filename = url.split("/")[-1]
        
        # Add a file extension if it's missing (httpbin paths end in jpeg/png/svg)
        if "." not in filename:
            filename = f"downloaded_image.{filename}"
            
        # Write the binary content to a file
        with open(filename, "wb") as file:
            file.write(resp.content)
            
        print(f"Successfully saved to {filename}")
    else:
        print(f"Failed to download from {url}. Status code: {resp.status_code}")


urls =  [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
thread = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    thread.append(t)

for t in thread:
    t.join()

end = time.time()

print(f"All downloads done in {end - start:.2f} seconds")
