pixels = [[[0, 0, 0, 0] for i in range(49)] for j in range(49)]
pixels[0][1] = [1, 2, 3, 4]

def add_pixels(pixel, increment):
    new_pixel = [0, 0, 0, 0]
    # 创建一个新的像素列表，避免修改原始像素引发拷贝意外
    new_pixel[0] = pixel[0] + increment[0]  # 红色通道
    new_pixel[1] = pixel[1] + increment[1]  # 绿色通道
    new_pixel[2] = pixel[2] + increment[2]  # 蓝色通道
    new_pixel[3] = pixel[3] + increment[3]  # 不透明度通道
    #new_pixel = [p + i for p, i in zip(pixel, increment)]
    return new_pixel

# 使用函数更新 [0][1] 位置的像素值
increment = [1, 3, 3, 6]
pixels[0][1] = add_pixels(pixels[0][1], increment)

print(pixels[0][1])  # 输出：[2, 5, 6, 10]
