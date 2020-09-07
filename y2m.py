# -*- coding: utf-8 -*-
import sys

def y2m_main(파일위치):
    datapack = open('datapack.data',"rb")
    unpackdata = datapack.read()
    sam88="0"
    sam8820="0"   
    f=open(파일위치,"rb")
    fxfx = f.read()
    f.seek(0)
    anti_live=0

    f.seek(1232)
    kimdo = f.read(4)
    f.seek(1260)
    ddol = f.read(4)
    f.seek(1288)
    jadong = f.read(4)
    f.seek(1316)
    homubird = f.read(4)
    
    LAYER = 0
    kasumi = 'empty'
    tae = 'empty'
    rimi = 'empty'
    arisa = 'empty'
    
    if kimdo == b'\x00\x00\x00\x01' :
        kasumi = 'po' 
    elif kimdo == b'\x00\x00\x00\x02' :
        kasumi = 'pi' 
    elif kimdo == b'\x00\x00\x00\x03' :
        kasumi = 'popi' 
    elif kimdo == b'\x00\x00\x00\x04' :
        kasumi = 'pa' 
    elif kimdo == b'\x00\x00\x00\x05' :
        kasumi = 'popa' 
    elif kimdo == b'\x00\x00\x00\x06' :
        kasumi = 'pipa' 
    elif kimdo == b'\x00\x00\x00\x07' :
        kasumi = 'popipa' 
    elif kimdo == b'\x00\x00\x02\x00' :
        kasumi = 'kirakira' 
    else :
        print ("FILE ERROR!")
        f.close()
        exit()
    
    if ddol == b'\x00\x00\x00\x01' :
        tae = 'po' 
    elif ddol == b'\x00\x00\x00\x02' :
        tae = 'pi' 
    elif ddol == b'\x00\x00\x00\x03' :
        tae = 'popi' 
    elif ddol == b'\x00\x00\x00\x04' :
        tae = 'pa' 
    elif ddol == b'\x00\x00\x00\x05' :
        tae = 'popa'
    elif ddol == b'\x00\x00\x00\x06' :
        tae = 'pipa' 
    elif ddol == b'\x00\x00\x00\x07' :
        tae = 'popipa' 
    elif ddol == b'\x00\x00\x02\x00' :
        tae = 'kirakira' 
    else :
        LAYER = 1
        anti_live=-56
    
    if LAYER == 0:
        if jadong == b'\x00\x00\x00\x01' :
            rimi = 'po' 
        elif jadong == b'\x00\x00\x00\x02' :
            rimi = 'pi' 
        elif jadong == b'\x00\x00\x00\x03' :
            rimi = 'popi' 
        elif jadong == b'\x00\x00\x00\x04' :
            rimi = 'pa' 
        elif jadong == b'\x00\x00\x00\x05' :
            rimi = 'popa' 
        elif jadong == b'\x00\x00\x00\x06' :
            rimi = 'pipa' 
        elif jadong == b'\x00\x00\x00\x07' :
            rimi = 'popipa' 
        elif jadong == b'\x00\x00\x02\x00' :
            rimi = 'kirakira' 
        else :
            LAYER = 2  
            anti_live=-28
    
    if LAYER == 0:
        if homubird == b'\x00\x00\x00\x01' :
            arisa = 'po' 
        elif homubird == b'\x00\x00\x00\x02' :
            arisa = 'pi' 
        elif homubird == b'\x00\x00\x00\x03' :
            arisa = 'popi' 
        elif homubird == b'\x00\x00\x00\x04' :
            arisa = 'pa' 
        elif homubird == b'\x00\x00\x00\x05' :
            arisa = 'popa' 
        elif homubird == b'\x00\x00\x00\x06' :
            arisa = 'pipa' 
        elif homubird == b'\x00\x00\x00\x07' :
            arisa = 'popipa' 
        elif homubird == b'\x00\x00\x02\x00' :
            arisa = 'kirakira' 
        else :
            LAYER = 3          
    
    if LAYER == 0:
        LAYER = 4  
        anti_live=28
    
    if LAYER >= 1 :
        z1=open('out1.mid','bw')
        z1.write(unpackdata)
        z1.close
    if LAYER >= 2 :
        z2=open('out2.mid','bw')
        z2.write(unpackdata)
        z2.close    
    if LAYER >= 3 :
        z3=open('out3.mid','bw')
        z3.write(unpackdata)
        z3.close    
    if LAYER >= 4 :
        z4=open('out4.mid','bw')
        z4.write(unpackdata)
        z4.close    
        
rrrr=sys.argv[1]    
y2m_main(rrrr)
    