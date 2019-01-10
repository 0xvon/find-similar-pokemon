import cv2
import os


def calc_feature(img_path: str, detector: cv2.ORB_create()):

    IMG_SIZE = (100, 100)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, IMG_SIZE)

    # 特微量算出
    return detector.detectAndCompute(img, None)


# 表示
def show_imgs_match(file):
    img1 = cv2.imread('./material_images/me.jpg')
    img2 = cv2.imread('./blog/material_images/' + file)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    akaze = cv2.ORB_create()
    kp1, des1 = akaze.detectAndCompute(gray1, None)
    kp2, des2 = akaze.detectAndCompute(gray2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
    plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
    plt.show()


target_image = 'me.jpg'
image_directory = './material_images/'

bf = cv2.BFMatcher(cv2.NORM_HAMMING)

#特微量算出アルゴリズム
detector = cv2.ORB_create()
# detector = cv2.AKAZE_create()
(target_kp, target_des) = calc_feature(image_directory + target_image,
                                       detector)

print('target: %s' % (target_image))

min_value = 1000
min_path = ''

files = os.listdir(image_directory)
for file in files:
    if file == '.DS_Store' or file == target_image:
        continue

    comparing_img_path = image_directory + file
    try:
        (comparing_kp, comparing_des) = calc_feature(comparing_img_path,
                                                     detector)
        #画像同士をマッチング
        matches = bf.match(target_des, comparing_des)
        dist = [m.distance for m in matches]
        #類似度計算
        ret = sum(dist) / len(dist)
    except cv2.error:
        ret = 100000

    if min_value > ret:
        min_value = ret
        min_path = file

print(min_path, min_value)
show_imgs_match(min_path)