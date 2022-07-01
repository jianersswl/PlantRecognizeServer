from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import cv2
import requests
import time
import os
from .yolov5.detect import detectByYolov5

### 保证算法的输入图像格式为(224,224,3)
def preprocess(image):
    x,y = image.shape[0:2]
    if(x>y):
        diff = int((x-y)/2)
        image = image[diff:x-diff,:,:]
    else:
        diff = int((y-x)/2)
        image = image[:,diff:y-diff,:]
    
    return cv2.resize(image,(224,224))

def downloadImg(url):
    _t = time.time()
    r = requests.get(url, stream=True, verify=False)
    print('Download code: {}'.format(r.status_code)) # 返回状态码
    if r.status_code == 200:
        image_name = url.split('/')[-1][-10:]
        image_name = 'static/image/'+image_name+'.jpg'
        open(image_name, 'wb').write(r.content) # 将内容写入图片
        print("Download time: {}".format(time.time()-_t))
    del r
    return image_name

def resultHandling(image, image_name):
    ### save result as image
    cv2.imwrite("static/recognize/flower/"+image_name, image)

    dict = {'code':200, 
            'msg':'识别成功',
            'PlantInfo':{'PlantResultURL':'static/flower/'+image_name,
                                   'leaf': '123',
                                  'stalk': '124',
                                  'fruit': '125',
                                    'age': '126',
            }
    }
    return dict

def recognizeUrl(url):
    image_path = downloadImg(url)
    image = cv2.imread(image_path)
    image_name = image_path.split('/')[-1]
    ### image preprocessing
    image = preprocess(image)
    ### image recognize
    '''
        to do
    '''
    return resultHandling(image, image_name)

def recognizeImage(image_path):
    image = cv2.imread(image_path)
    image_name = image_path.split('/')[-1]
    ### image preprocessing
    image = preprocess(image)

    ### image recognize
    ### cmd method
    # url = image_path
    # cmd = r'python D:\pyproject\yolov5-django\detect.py --source ' + url + ' --classes 0 --exist-ok'
    # text = os.popen(cmd).readlines()
    # print(text)

    # inline method
    detectByYolov5(source=image_path)

    return resultHandling(image, image_name)

def uploadUrl(request):
    print("postBody: {}".format(request.POST))
    url = request.POST.get('imageURL','')
    print("url: {}".format(url))
    respon = json.dumps(recognizeUrl(url))

    return HttpResponse(respon)

def uploadImage(request):
    print("postBody: {}".format(request))
    file_obj = request.FILES.get("image")

    print("file_obj", file_obj.name)
    file_path = 'static/recognize/image/' + file_obj.name
    print("file_path", file_path)
 
    with open(file_path, 'wb+') as f:
      for chunk in file_obj.chunks():
        f.write(chunk)
    
    respon = json.dumps(recognizeImage(file_path))
    
    return HttpResponse(respon)

def get(request):
    print("getBody: {}".format(request.GET))
    dict = {'code':200, 
            'msg':'识别成功',
            'PlantInfo':{'PlantResultURL':'static/recognize/flower/yueji.jpg',
                                   'leaf': '123',
                                  'stalk': '124',
                                  'fruit': '125',
                                    'age': '126',
            }
    }
    respon = json.dumps(dict)
    return HttpResponse(respon)