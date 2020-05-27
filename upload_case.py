import os
import django
import shutil
import glob


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduWeb.settings')# environ是字典，同os.environ['DJANGO_SETTINGS_MODULE']
django.setup()

from mainsite.models import RawCase

def upload_case(child_dir,case_num):

    rawcase = RawCase(case_id='case'+str(case_num))

    prn0 = open(child_dir + '/prn_rch0.txt',encoding='UTF-8-sig')
    diagnosis = []
    while True:
        line = prn0.readline()
        if not line:
            break
        else:
            diagnosis.append(line)
    prn0.close()
    rawcase.diagnosis = '|'.join(diagnosis)
    # print(str.split(rawcase.diagnosis,'|'))

    prn1 = open(child_dir + '/prn_rch1.txt',encoding='UTF-8-sig')
    symptoms = []
    while True:
        line = prn1.readline()
        if line == "医嘱：\n":
            break
        else:
            symptoms.append(line)
    rawcase.symptoms = '|'.join(symptoms)

    prescription = []
    while True:
        line = prn1.readline()
        if not line:
            break
        else:
            prescription.append(line)
    rawcase.prescription = '|'.join(prescription)
    prn1.close()

    photo_path = []
    for pic_name in glob.glob(child_dir+'/caporg*.jpg'):
        pic_name = str.split(pic_name,'/')
        pic_name = pic_name[-1]
        cp_from = child_dir+'/'+pic_name
        cp_to = 'media/img/'
        shutil.copy(cp_from, cp_to)
        original_filename = cp_to + pic_name
        new_filename = cp_to + "/case" + str(case_num) + '-' + pic_name
        os.rename(original_filename, new_filename)
        photo_path.append('img'+ "/case" + str(case_num) + '-' + pic_name)
    rawcase.photo_path = '|'.join(photo_path)
    rawcase.save()


if __name__ == '__main__':
    root_dir = '/home/williaml/exp_case/'
    f = open('record','r')
    case_num = int(f.readline())
    f.close()
    for dir_name in os.listdir(root_dir):
        child_dir = root_dir + dir_name
        print(child_dir)
        upload_case(child_dir,case_num)
        case_num+=1
    f=open('record','w')
    f.write(str(case_num))
    f.close()