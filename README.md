# 2022_DL_project  
건주 파일  
xml_to_txt.py - 라벨 수정 파일  

효준 파일 - pretrained model  
효준 1 - 모델 : yolov5x, batch size : 64, image size : 640, out of memory  
효준 2 - 모델 : yolov5l, batch size : 64, image size : 640, out of memory  
효준 3 - 모델 : yolov5m, batch size : 64, image size : 640, out of memory  
효준 4 - 모델 : yolov5s6, batch size : 64, image size : 1280, out of memory  
효준 5 - 모델 : yolov5s6, batch size : 32, image size : 1280, out of memory  
효준 6 - 모델 : yolov5s6, batch size : 16, image size : 1280, success  
효준 7 - 모델 : yolov5x6, batch size : 32, image size : 640, out of memory  
효준 8 - 모델 : yolov5m, batch size : 32, image size : 640, success  

제우 파일 - not pretrained model  
제우 1 - 모델 : yolov5x, batch size : 64, image size : 640, out of memory  
제우 2 - 모델 : yolov5l, batch size : 64, image size : 640, out of memory  
제우 3 - 모델 : yolov5m, batch size : 64, image size : 640, out of memory  
제우 4 - 모델 : yolov5s, batch size : 64, image size : 1280, out of memory  
제우 5 - 모델 : yolov5s, batch size : 32, image size : 1280, out of memory   
제우 6 - 모델 : yolov5s, batch size : 32, image size : 640, success  
제우 7 - 모델 : yolov5x6, batch size : 32, image size : 640, out of memory  
제우 8 - 모델 : yolov5m, batch size : 32, image size : 640, success     


데이터 셋 링크 : https://aihub.or.kr/aidata/8007  
학습 환경 : colab pro 사용 (Tesla P100-PCIE-16GB)  
           GCP 사용 (Tesla V100-SXM2-16GB) - multi-GPU , n1-standard-8 (8 vCPUs, 30 GB RAM)  
                                             Ubuntu 20.04  
                                             TensorFlow Enterprise 2.8 (with LTS and Intel® MKL-DNN/MKL)  
                                             부팅 디스크 300 GB disk  
                                             데이터 디스크 200 GB disk  
시연 영상 : https://drive.google.com/drive/folders/1b1ci-6Wo_cHsmKmagt_0B2Bx8ayw0j2H?usp=sharing
