# 12306 CAPTCHA CRACK
## 介绍 🐸

12306验证码破解程序，单个图片识别率在94%左右，文字识别部分采用Google Vision识别，实际测试，整体正确率在80%左右。图片一共80种分类，支持12306爬虫登录，使用DenseNet 200层深层网络训练。附上已训练好的模型。Dataset来自Kaggle [传送门](https://www.kaggle.com/libowei/12306-captcha-image)

## 演示图片 🤖

![Pic](screenshot/text.png?raw=true)
![Pic](screenshot/result.png?raw=true)

## 使用方法 🐮

#### 环境要求
+ [Tensorflow](https://www.tensorflow.org)
+ [Keras](https://keras.io)

#### API要求
由于Google Vision API有调用次数限制，建议自行申请一个。~~由于Google安全警告，已移除API Key文件~~

### Demo
```
pip3 -r requirement.txt
python3 demo.py
python3 Demo_Webpage/client.py
```
打开浏览器输入地址 [127.0.0.1:5000](http://127.0.0.1:5000)
Mac 可以使用下面命令
```
open http://127.0.0.1:5000
```
### 训练模型
需要下载[数据集](https://www.kaggle.com/libowei/12306-captcha-image)在根目录，命名为captcha。建议在AWS或其它GPU运算能力强的机器上训练，MBP上训练至少40小时以上。训练好模型存在saves文件夹下，更多参数请看源代码。
```
python3 train.py --train --logs
```

## TODO 🎄
- [ ] 双词汇匹配
- [ ] 使用CTPN，对中文进行神经网络训练
- [ ] 中文近形字匹配
