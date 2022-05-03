#!/usr/bin/env python
# coding: utf-8

# In[76]:


import xml.etree.ElementTree as ET
label={'Vehicle_Car':0, 'Vehicle_Bus' : 1, 'Vehicle_Motorcycle' : 2, 'Vehicle_Unknown' : 3,'Pedestrian_Pedestrian' :4, 'Pedestrian_Bicycle' : 5,'Lane_White_Dash' : 6, 'Lane_White_Solid' : 7, 'Lane_Yellow_Dash' : 8, 'Lane_Yellow_Solid' : 9, 'Lane_Blue_Dash' : 10, 'Lane_Blue_Solid' : 11, 'TrafficLight_Red' : 12, 'TrafficLight_Yellow' : 13, 'TrafficLight_Green' : 14, 'TrafficLight_Arrow' : 15, 'TrafficLight_RedArrow' : 16, 'TrafficLight_YellowArrow' : 17, 'TrafficLight_GreenArrow' : 18, 'TrafficSign_Speed' : 19, 'TrafficSign_Else' : 20, 'RoadMark_StopLine' : 21, 'RoadMark_Crosswalk' : 22, 'RoadMark_Number' : 23, 'RoadMark_Character' : 24, 'RoadMarkArrow_Straight' : 25, 'RoadMarkArrow_Left' : 26, 'RoadMarkArrow_Right' : 27, 'RoadMarkArrow_StraightLeft' : 28, 'RoadMarkArrow_StraightRight' : 29, 'RoadMarkArrow_Uturn' : 30, 'RoadMarkArrow_Else' : 31}
tree=ET.parse('C:/Users/kwak2/Desktop/도로주행영상예시/라벨링데이터/bb/도심로/야간일몰_맑음_30_전방/20200708_200952/1_annotations_v001_1/1_20200708_200952_000000_v001_1.xml')
root=tree.getroot()
obj = root.findall("object")
size = root.findall('size')
for i in size:
    w=i.findtext('width')
    h=i.findtext('height')
#print(w)
name =[x.findtext("name") for x in obj]
#print(name)
bndbox = obj[0].findall("bndbox")
for i in range(len(obj)):
    bndbox = obj[i].findall("bndbox")
    xmin = [x.findtext("xmin") for x in bndbox]
    #print(xmin)
    xmax = [x.findtext("xmax") for x in bndbox]
    #print(xmax)
    ymin = [y.findtext("ymin") for y in bndbox]
    #print(ymin)
    ymax = [y.findtext("ymax") for y in bndbox]
    #print(ymax)
    x_c,y_c,w1,h1 = (int(xmin[0])/int(w)+int(xmax[0])/int(w))/2,(int(ymin[0])/int(h)+int(ymax[0])/int(h))/2, (int(xmax[0])-int(xmin[0]))/int(w),(int(ymax[0])-int(ymin[0]))/int(h)
    if name[i] in label.keys():
        result = [str(label[name[i]]), str(x_c),str(y_c),str(w1),str(h1)]
    else:
        break
    f = open('1_20200708_200952_000000' + '.txt', 'w')
    f.write(' '.join(result))
    f.write('\n')
    f.close()
    #print(result)

