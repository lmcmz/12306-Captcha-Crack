from model.densenet import DenseNet
from Demo_Webpage import client
import utils
import numpy as np
import time
import shutil
import os, translate
import json

import GoogleLens
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

n_classes = 80
image_shape = (64, 64, 3)
image_model_weight = "./saves/DenseNet_k=12_d=40.weight"
save_path = "./temp"
save_fail_path = "temp/faild"

demo_path = "./Demo_Webpage/static/img"

def load_model():
    text_model = None
    image_model = DenseNet(classes=n_classes, input_shape=image_shape, depth=40, \
    growth_rate=12, bottleneck=False,reduction=0.0, dropout_rate=0.0, weight_decay=1e-4)
    image_model.load_weights(image_model_weight)
    return text_model, image_model

def load_label_dict():
    '''
    Read Label
    '''
    label_dict = {}
    label_dict_en = {}
    with open("labels.txt", encoding="utf-8") as file:
        for line in file:
            class_name, id , class_en = line.strip().split('\t')
            label_dict[int(id)] = class_name
            label_dict_en[int(id)] = class_en
    return label_dict, label_dict_en

def demo_test(text_model, image_model, label_dict, label_dict_en):
    """
    获取验证码图片、模型识别、提交
    :return:
    """
    image_path = utils.download_captcha()
    raw_texts, raw_images = utils.process_raw_images(image_path, (image_shape[0], image_shape[1]))
    utils.save_name(raw_texts[0], demo_path, 'text')
    for i, img in enumerate(raw_images):
        utils.save_name(raw_images[i], demo_path, i)
        
    shutil.copy(image_path, os.path.join(demo_path, 'demo.png'))
    
    images = np.array([np.asarray(image) for image in raw_images])
    image_predict = image_model.predict(images)
    image_result = np.argmax(image_predict, 1)
    image_prob = np.max(image_predict, 1)
    
    image_label = [label_dict[r].replace("\xa0","") for r in image_result]
    image_label_en = [label_dict_en[r] for r in image_result]
    text_label = GoogleLens.get_target_text(image_path)
    
    print(text_label)
    print(image_label)
    print(image_label_en)
            
    ids = set()
    for id, r2 in enumerate(image_label):
        if text_label == r2:
            ids.add(id)
    
    if len(ids) == 0:
        txt, score = process.extractOne(text_label, image_label)
        print(text_label, txt)
        text_label = txt
        for id, r2 in enumerate(image_label):
            if txt == r2:
                ids.add(id)
    
    result = utils.submit_captcha(ids)
    utils.draw_circle(ids, demo_path, 'demo.png')
    
    label = {}
    for i, l in enumerate(image_label):
        label[i] = {}
        label[i]['cn'] = l
        label[i]['en'] = image_label_en[i]
    
    dict = {}
    dict['text_label'] = text_label
    dict['text_label_en'] = utils.find_en_word(image_label, image_label_en, text_label)
#     translate.translate(text_label)
    dict['label'] = label
    if "成功" in result:
        dict['result'] = True
    else:
        dict['result'] = False
    with open(os.path.join(demo_path,'file.txt'), 'w') as file:
         file.write(json.dumps(dict, indent=4, ensure_ascii=False))
    
if __name__ == '__main__':
    text_model, image_model = load_model()
    label_dict, label_dict_en = load_label_dict()
    demo_test(text_model, image_model, label_dict, label_dict_en)
