import google_images_download
code = "dog"
response = google_images_download.googleimagesdownload()
arguments = {"keywords": str(code),"limit":1,"no_download":True}
paths = response.download(arguments)
print(paths)