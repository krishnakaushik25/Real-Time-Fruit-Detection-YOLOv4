import os

image_files = []
os.chdir(os.path.join("data", "obj"))
for filename in os.listdir(os.getcwd()):
    path1=os.getcwd()
    path=os.path.join("data", "obj")
    if filename.endswith(".jpg"):
        image_files.append(path1+'/'+ path  + filename)
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")