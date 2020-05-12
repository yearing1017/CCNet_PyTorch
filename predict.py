import os 
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset, random_split
from torchvision import transforms
#from deeplabv3 import resnet50, resnet101, resnet152, ResNet
#from CCNet.ccnet import resnet152
#from deeplabv3_dan_0408 import resnet152 
#from fcn import FCN16s, VGGNet
#from dan_v3_v0420 import resnet152
from ccnet_v3_v0509 import resnet152
import cv2
import numpy as np
from test_data import test_dataloader

colors = [(0,0,0),(0,128,128),(128,0,128),(128,0,0)] #黑、黄、紫、蓝

def label2color(colors, n_classes, predict):
    seg_color = np.zeros((predict.shape[1], predict.shape[2], 3))
    for c in range(n_classes):
        seg_color[:, :, 0] += ((predict[0,:,:] == c) *
                            (colors[c][0])).astype('uint8')
        seg_color[:, :, 1] += ((predict[0,:,:] == c) *
                            (colors[c][1])).astype('uint8')
        seg_color[:, :, 2] += ((predict[0,:,:] == c) *
                            (colors[c][2])).astype('uint8')
    seg_color = seg_color.astype(np.uint8)
    return seg_color

def save(save_dir, image_name_batch, seg_color):
    for image_name in image_name_batch:
        seg = seg_color[:,:,:]
        cv2.imwrite(save_dir+image_name, seg)
        print(image_name+"已保存!")

def predict():
    device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
    model = resnet152()
    #vgg_model = VGGNet()
    #model = FCN16s(pretrained_net=vgg_model)
    model.load_state_dict(torch.load("models_ccnet_v3_0509/ccnet_v3_32.pth"))
    model = model.to(device)
    #model = torch.load('checkpoints_v3p_v0316/deeplabv3plus_model_34.pt')
    save_dir = 'predict_test_ccnet_v3_0509/'
    model.eval()
    with torch.no_grad():
        for index, (image_name_batch, image, label) in enumerate(test_dataloader):
            #print(image_name_batch)
            image = image.to(device)
            #label = label.to(device)
            predict = model(image) #(4,5,640,640)
            predict_index = torch.argmax(predict, dim=1, keepdim=False).cpu().numpy()  #(4, 640,640)
            seg_color = label2color(colors, 4, predict_index)
            save(save_dir, image_name_batch, seg_color)

if __name__ == "__main__":
    predict()

