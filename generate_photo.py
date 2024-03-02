import math
import os
import random
from shutil import rmtree
from PIL import Image, ImageDraw

# Функция для генерации случайного цвета
def random_color():
    #return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return (255,255,255)


    # Функция для создания изображения и сохранения его в указанную директорию
def draw_triangle_random_rotated(w, h, fc, mfs):
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)

    side_length = random.randint(mfs, min(w, h) // 2 - 1)
    angle = random.uniform(0, 360)
    angle_rad = math.radians(angle)

    x1 = w // 2
    y1 = h // 2 - side_length // 2
    x2 = w // 2 - side_length // 2
    y2 = h // 2 + side_length // 2
    x3 = w // 2 + side_length // 2
    y3 = h // 2 + side_length // 2

    # Поворачиваем координаты точек
    x1_rotated = int((x1 - w // 2) * math.cos(angle_rad) - (y1 - h // 2) * math.sin(angle_rad) + w // 2)
    y1_rotated = int((x1 - w // 2) * math.sin(angle_rad) + (y1 - h // 2) * math.cos(angle_rad) + h // 2)
    x2_rotated = int((x2 - w // 2) * math.cos(angle_rad) - (y2 - h // 2) * math.sin(angle_rad) + w // 2)
    y2_rotated = int((x2 - w // 2) * math.sin(angle_rad) + (y2 - h // 2) * math.cos(angle_rad) + h // 2)
    x3_rotated = int((x3 - w // 2) * math.cos(angle_rad) - (y3 - h // 2) * math.sin(angle_rad) + w // 2)
    y3_rotated = int((x3 - w // 2) * math.sin(angle_rad) + (y3 - h // 2) * math.cos(angle_rad) + h // 2)

    draw.polygon([(x1_rotated, y1_rotated), (x2_rotated, y2_rotated), (x3_rotated, y3_rotated)], fill=fc, outline=(0, 0, 0))
    return img

def draw_box_random_rotated(w, h, fc, mfs):
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)

    side_length = random.randint(mfs, min(w, h) // 2 - 1)
    angle = random.uniform(0, 360)
    angle_rad = math.radians(angle)

    # Центр прямоугольника
    x_center = random.randint(side_length // 2, w - side_length // 2)
    y_center = random.randint(side_length // 2, h - side_length // 2)

    # Половина длины и ширины
    half_length = side_length // 2
    half_width = side_length // 2

    # Координаты углов прямоугольника
    x1_rotated = int(x_center - half_length * math.cos(angle_rad) + half_width * math.sin(angle_rad))
    y1_rotated = int(y_center - half_length * math.sin(angle_rad) - half_width * math.cos(angle_rad))
    x2_rotated = int(x_center + half_length * math.cos(angle_rad) + half_width * math.sin(angle_rad))
    y2_rotated = int(y_center + half_length * math.sin(angle_rad) - half_width * math.cos(angle_rad))
    x3_rotated = int(x_center + half_length * math.cos(angle_rad) - half_width * math.sin(angle_rad))
    y3_rotated = int(y_center + half_length * math.sin(angle_rad) + half_width * math.cos(angle_rad))
    x4_rotated = int(x_center - half_length * math.cos(angle_rad) - half_width * math.sin(angle_rad))
    y4_rotated = int(y_center - half_length * math.sin(angle_rad) + half_width * math.cos(angle_rad))

    draw.polygon([(x1_rotated, y1_rotated), (x2_rotated, y2_rotated), (x3_rotated, y3_rotated), (x4_rotated, y4_rotated)], fill=fc, outline=(0, 0, 0))
    return img

def draw_circle_random_rotated(w, h, fc, mfs):
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)

    r = random.randint(mfs // 2, min(w, h) // 2 - 1)
    angle = random.uniform(0, 360)
    angle_rad = math.radians(angle)

    x = random.randint(r, w - r)
    y = random.randint(r, h - r)

    # Поворачиваем координаты центра
    x_rotated = int((x - w // 2) * math.cos(angle_rad) - (y - h // 2) * math.sin(angle_rad) + w // 2)
    y_rotated = int((x - w // 2) * math.sin(angle_rad) + (y - h // 2) * math.cos(angle_rad) + h // 2)

    draw.ellipse((x_rotated - r, y_rotated - r, x_rotated + r, y_rotated + r), fill=fc, outline=(0, 0, 0))
    return img

def genererate_pictures(_path, num_samples,w,h,min_fig_size):


    

    if os.path.exists(_path): 
        rmtree(_path)
    os.makedirs(_path)
    _folder = os.path.join(_path, "boxes")
    if not os.path.exists(_folder): os.makedirs(_folder)
    _folder = os.path.join(_path, "circles")
    if not os.path.exists(_folder): os.makedirs(_folder)
    _folder = os.path.join(_path, "treangle")
    if not os.path.exists(_folder): os.makedirs(_folder)



    for i in range(num_samples):
        # Генерация прямоугольника с одним из 7 цветов
        img_box = draw_box_random_rotated(w=w, h=h, fc=random_color(), mfs=min_fig_size)
        img_box.save(os.path.join(os.path.join(_path, "boxes"), f"box-{i}.png"))

        # Генерация круга с одним из 7 цветов
        img_circle = draw_circle_random_rotated(w=w, h=h, fc=random_color(), mfs=min_fig_size)
        img_circle.save(os.path.join(os.path.join(_path, "circles"), f"circle-{i}.png"))

        # Генерация круга с одним из 7 цветов
        img_treangle = draw_triangle_random_rotated(w=w, h=h, fc=random_color(), mfs=min_fig_size)
        img_treangle.save(os.path.join(os.path.join(_path, "treangle"), f"treangle-{i}.png"))

