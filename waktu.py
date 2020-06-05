def waktu():
    import time
    a=time.localtime()
    hr=a.tm_hour
    mn=a.tm_min
    sc=a.tm_sec
    return ('{}.{}.{}'.format(hr,mn,sc))
