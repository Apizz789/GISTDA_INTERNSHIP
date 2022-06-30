# Create your tasks here

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .views import Spacetrack_to_TLE,POWER,SGP4_120km
import mysql.connector
import datetime
from sgp4.api import days2mdhms


@shared_task
def test():
    print('sucessfully exceuted')
    return 1

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y

@shared_task
def importTLE():
    print('DONE')
    #Assign TLE
    tle1,tle2=Spacetrack_to_TLE()
    
    #SGP4 propagation
    #create list for every error condition
    #Error0 = no error
    #Error1-5 = SGP4 error
    #Error6 = negative altitude
    #Error7 = diverge
    CoordLst=[]
    speedLst=[]
    idLst=[]
    timeLst=[]
    time_idLst=[]
    altLst=[]
    epochError0=[]
    coordError0=[]
    speedError0=[]
    epochLst=[]
    
    idLstError1=[]         
    timeLstError1=[] 
    altLstError1=[]
    epochError1=[]        
    idLstError7=[]         
    idLst_negativeAlt=[]
    timeLst_negativeAlt=[]
    epochNegativeAlt=[]
    altLst_negativeAlt=[]
    ErrorLst=[]
    idLstError_other=[]
    timeLstError_other=[]
    for i in range (len(tle1)):
        time,epoch_time,altitude,coord,speed,ErrorCheck=SGP4_120km(tle1[i],tle2[i])
        ErrorLst.append(ErrorCheck)
        CoordLst.append(coord)
        speedLst.append(speed)
        epochLst.append(epoch_time)
        if ErrorCheck==0:
            #print(time)
            idLst.append(i)
            timeLst.append(time)
            time_id=time.copy()
            time_id.append(i)
            
            time_idLst.append(time_id)
            
            altLst.append(altitude)
            epochError0.append(epoch_time)
            coordError0.append(coord)
            speedError0.append(speed)
        elif ErrorCheck==1:
            idLstError1.append(i)
            timeLstError1.append(time)
            altLstError1.append(altitude)
            epochError1.append(epoch_time)
            
            """
            print(tle1[i])
            print(tle2[i])
            """
        elif ErrorCheck==7:
            idLstError7.append(i)
            
        elif ErrorCheck==6:
            idLst_negativeAlt.append(i)
            timeLst_negativeAlt.append(time)
            altLst_negativeAlt.append(altitude)
            epochNegativeAlt.append(epoch_time)
        else:
            idLstError_other.append(i)
            timeLstError_other.append(time)
    
    #sorting error0 object by time
    sort_time_idLst=sorted(time_idLst)
    tle=[]
    tle1Lst=[]
    tle2Lst=[]
    sort_coordLst=[]
    sort_speedLst=[]
    
    id_data_Lst=[]
    for i in range (len(idLst)):
        n=sort_time_idLst[i][6]
        tle1Lst.append(tle1[n])
        tle2Lst.append(tle2[n])
        sort_coordLst.append(CoordLst[n])
        sort_speedLst.append(speedLst[n])
        
    for i in range (len(idLst)):
        id_data=[]
        id_data.append(tle1Lst[i])
        id_data.append(tle2Lst[i])
        id_data.append(sort_time_idLst[i])
        id_data.append(sort_coordLst[i])
        id_data.append(sort_speedLst[i])
        id_data_Lst.append(id_data)
    
    Norad_ID_lst=[]
    doy_lst=[]
    Epoch_lst=[]
    Epoch120c_lst=[]
    for i in tle1Lst:
        Norad_ID_lst.append(i[2:8])
        doy_lst.append(i[18:32])
    for i in doy_lst:
        year='20'+i[0:2]
        month, day, hour, minute, second = days2mdhms(int(i[0:2]), float(i[2:14]))
        Epoch = datetime.datetime(int(year), int(month), int(day),int(hour),int(minute),int(second))
        Epoch_lst.append(Epoch)
    for i in sort_time_idLst:
        Epoch120=datetime.datetime(int(i[0]),int(i[1]),int(i[2]),int(i[3]),int(i[4]),int(i[5]))
        Epoch120c_lst.append(Epoch120)   
    for i in range (len(tle1Lst)):
       upload_to_mysql(Norad_ID_lst[i],tle1Lst[i],tle2Lst[i],Epoch_lst[i],Epoch120c_lst[i],sort_coordLst[i],sort_speedLst[i])
    
    return  


def upload_to_mysql(Norad_ID,TLE1,TLE2,Epoch,Epoch_120km,coord,velo):
    X_coord=coord[0]
    Y_coord=coord[1]
    Z_coord=coord[2]
    X_velo=velo[0]
    Y_velo=velo[1]
    Z_velo=velo[2]
    try:
        mydb = mysql.connector.connect(host='172.27.188.71',
                                        database='Internship',
                                        user='arlapp',
                                        password='fdsus2019')
    except:
        print('Login Error')
        return
    select_TLE = "SELECT * FROM Internship.TLE_Prediction"
    cursor = mydb.cursor()
    cursor.execute(select_TLE)
    # get all records
    current_data = cursor.fetchall()
    for i in range (len(current_data)):
        #if same Norad and Epoch, skip this data
        if current_data[i][0] == Norad_ID and current_data[i][3] == Epoch:
            print('Data is already existed. Skip the process')
            return
        #if same Norad but different Epoch, update this data
        elif current_data[i][0] == Norad_ID and current_data[i][3] != Epoch:
            sql_delete="DELETE FROM Internship.TLE_Prediction WHERE Norad_ID = '"+Norad_ID+"'"
            mycursor = mydb.cursor()
            mycursor.execute(sql_delete)
            mydb.commit()
            print('New data updated')
            mycursor = mydb.cursor()

            sql_add = "INSERT INTO TLE_Prediction (Norad_ID, TLE1, TLE2, Epoch, Epoch_120km, X_coord, Y_coord, Z_coord, X_velo, Y_velo, Z_velo) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
            val = (Norad_ID, TLE1, TLE2, Epoch, Epoch_120km, X_coord, Y_coord, Z_coord, X_velo, Y_velo, Z_velo)
            mycursor.execute(sql_add, val)
            

            mydb.commit()
            return
    
    #if no existed data, add this data    
    mycursor = mydb.cursor()

    sql_add = "INSERT INTO TLE_Prediction (Norad_ID, TLE1, TLE2, Epoch, Epoch_120km, X_coord, Y_coord, Z_coord, X_velo, Y_velo, Z_velo) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
    val = (Norad_ID, TLE1, TLE2, Epoch, Epoch_120km, X_coord, Y_coord, Z_coord, X_velo, Y_velo, Z_velo)
    mycursor.execute(sql_add, val)

    mydb.commit()

    print("New data added")   
    return 