latitude = []
longitude = []
datas = []
while(True) :
    _lat = input('Enter Latitude : ')
    if(_lat == "0"):
        break
    _long = input('Enter Longtitude : ')
   
    latitude.append(_lat)
    longitude.append(_long)

for i in range(len(latitude)):
    latt = latitude[i].split('.')
    # South
    if(latt[0][0] == "-") :
        d = latt[0][1:]
        if len(d) == 1 :
            d = "0"+ d
        _min = str(float("0."+ latt[1]) * 60 ).split('.')
        dmin = _min[0]
        if len(dmin) == 1 :
            dmin = "0"+ dmin
        _sec = str(float("0."+ _min[1]) * 60).split('.')
        dsec = _sec[0]
        if len(dsec) == 1 :
            dsec = "0"+ dsec
        DDN = "S"+ d + dmin + dsec
    else:
        d = latt[0]
        if len(d) == 1 :
            d = "0"+ d
        _min = str(float("0."+ latt[1]) * 60 ).split('.')
        dmin = _min[0]
        if len(dmin) == 1 :
            dmin = "0"+ dmin
        _sec = str(float("0."+ _min[1]) * 60).split('.')
        dsec = _sec[0]
        if len(dsec) == 1 :
            dsec = "0"+ dsec
        DDN = "N"+ d + dmin + dsec


    longg = longitude[i].split('.')
    if(longg[0][0] == "-") :
        d1 = longg[0][1:]
        if len(d1) == 1 :
            d = "00"+ d
        _min1 = str(float("0."+ longg[1]) * 60 ).split('.')
        dmin1 = _min1[0]
        if len(dmin1) == 1 :
            dmin1 = "0"+ dmin1
        _sec1 = str(float("0."+ _min1[1]) * 60).split('.')
        dsec1 = _sec1[0]
        if len(dsec1) == 1 :
            dsec1 = "0"+ dsec1
        DDS = "W"+ d1 + dmin1 + dsec1
    else:
        d1 = longg[0]
        if len(d1) == 1 :
            d = "00"+ d
        _min1 = str(float("0."+ longg[1]) * 60 ).split('.')
        dmin1 = _min1[0]
        if len(dmin1) == 1 :
            dmin1 = "0"+ dmin1
        _sec1 = str(float("0."+ _min1[1]) * 60).split('.')
        dsec1 = _sec1[0]
        if len(dsec1) == 1 :
            dsec1 = "0"+ dsec1
        DDS = "E"+ d1 + dmin1 + dsec1
            
    datas.append(DDN+DDS)
 

print(datas)

with open('notam.txt', 'w') as f:
    for data in datas:
        f.write(data)
        f.write(' ')