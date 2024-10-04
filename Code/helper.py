import yaml
import argparse
import os
import cv2
import matplotlib.pyplot as plt
from Stage1_ToothSegm import Stage1
from Stage2_Mask2Mask import Stage2_Mask2Mask
from Stage3_Mask2Teeth import Stage3_Mask2Teeth
from Restore.Restore import Restore


# args = None

def loadModelConfig():
    parser = argparse.ArgumentParser()
    
    with open("./Config.yaml", 'r') as f:
        GeneratorConfig = yaml.load(f, Loader=yaml.SafeLoader)['C2C2T_v2_facecolor_lightcolor']
    parser.set_defaults(**GeneratorConfig)
    args = parser.parse_args()

    return args

def inference_image(img_path,args):
    img_name = os.path.basename(img_path).split('.')[0]
    stage1_data = Stage1(img_path, mode=args.mode, state=args.stage1, if_visual=False)
    stage2_data = Stage2_Mask2Mask(stage1_data, mode=args.mode, state=args.stage2, if_visual=False)
    stage2_data.update(stage1_data)
    stage3_data = Stage3_Mask2Teeth(stage2_data, mode=args.mode, state=args.stage3, if_visual=False)
    stage3_data.update(stage2_data)
    pred = Restore(stage3_data['crop_mouth_align'], stage3_data)   # restore to original size
    pred_face = pred['pred_ori_face']

    return pred_face