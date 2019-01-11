import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 60))
count = 0
for cluster, path in zip(labels, os.listdir(image_directory)):
    img = Image.open(image_directory + path)
    img = img.convert('RGB')
    img = img.resize((100, 100))
    img_array = np.array(img)
    if cluster == 1:
        count += 1
        ax = fig.add_subplot(20, 4, count)
        ax.set_title(path)
        ax.imshow(img_array)

plt.show()