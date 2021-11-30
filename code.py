import math
def format_duration(seconds):
    #seconds=120
    minutes = 0
    hours=0
    days=0
    years=0
               
    if seconds >= 60:
        minutes = seconds//60
        seconds = seconds%60
        
    
    if minutes >= 60:
        hours = minutes//60
        minutes = minutes%60
        
    if hours >= 24:
        days = hours//24
        hours = hours%24
        
    if days >= 365:
        years = days//365
        days = days%365
    
   

    output=[]
    andd=0
    ohibkatut=0
    if years == 1:
        output+=', ',str(years),' year'
        andd=1
    if years > 1:
        output+=', ',str(years),' years'
        andd=1  
        
    if days == 1:
        output+=', ',str(days),' day'
        andd=1
    if days > 1:
        output+=', ',str(days),' days'
        andd=1
        
    if hours == 1:
        output+=', ',str(hours),' hour'
        andd=1
    if hours > 1:
        output+=', ',str(hours),' hours'
        andd=1
    
    if minutes == 1:
        output+=', ',str(minutes),' minute'
        andd=1
        
    if minutes > 1 and (seconds == 0) :
        output+=' and ',str(minutes),' minutes'
        andd=1
        #ohibkatut=1
        
    if minutes > 1 and (seconds > 0) :
        output+=', ',str(minutes),' minutes'
        andd=1    
        
    
    if seconds == 1 and (andd!=1):
        output+="1 second"
    if seconds == 1 and (andd==1):
        output+=' and ',str(seconds),' second'
        andd=1
    if seconds > 1 and (andd==1):
        output+=' and ',str(seconds),' seconds'
        andd=1
    
    #print('Years -',years)
    #print('Days -',days)
    #print('Hours -',hours)
    #print('Minutes -',minutes)
    #print('Seconds -',seconds)
    if seconds==0 and (andd==0) and (minutes==0)and (hours==0)and (days==0)and (years==0):
        #output+="now"
        ohibkatut=1
        #return('now')
    
    if ohibkatut ==1:
        if (len(output)==0):
            print('now')
            return('now')
    else:
        #print(output)
        if output[0]==', ':
            del(output[0])
        if output[0]==' and ':
            del(output[0])
           
        o=''
        o=o.join(output)
        print(o)
        return(o)

seconds=input('Enter seconds: ')
seconds=int(seconds)
format_duration(seconds)