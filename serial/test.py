import serial 
import mysql.connector
import paho.mqtt.client as mqtt
import datetime
THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'Y3wJ8SUkSDe2CIdXKWdu'
#database configure
mydb = mysql.connector.connect(
   host="us-cdbr-iron-east-02.cleardb.net",
   user="b801f230629d30",
   passwd="91690179",
   database="heroku_c56b50141fa0f31"
)
mycursor = mydb.cursor()

#thingsboard configure
client - mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()
#USB configure
port = "/dev/ttyUSB0"
serialfromarduino = serial.Serial(port,115200)  
#serialfromarduino.flushInput()
file = open ("data.txt","a+")
count_t = 0
count_h = 0
count_e = 0
count_p = 0
count_l = 0
count_wt= 0
count=0
temp= []
watertemp = []
humi = []
ec = []
ph = []
lux = []
status = {'status' : ''}
while True:
 if(serialfromarduino.inWaiting()>0) : 
      a = serialfromarduino.readline() 
      file.write(a)
      a=a.decode()
      a=a.rstrip()
      
      #print(a)
      b = serialfromarduino.readline() 
      c = b
      b=b.decode()
      b=b.rstrip()
      #print(type(b))
      if (a == 'Temperature') :
          count_t=b 
          temp.append(b)
          print ("Temp:")
          print (temp)
          count=count+1
      if (a == 'WaterTemperature') :
          count_wt=b  
          watertemp.append(b)
          print ("Water temp:")
          print (watertemp)
          count=count+1
      if (a == 'Humidity') : 
          count_h=b 
          humi.append(b)
          print ("Humi:")
          print (humi)
          count=count+1
      if (a == 'EC') : 
          count_e=b 
          ec.append(b)
          print ("EC:")
          print (ec)
          count=count+1
      if (a == 'pH') : 
          count_p=b 
          ph.append(b)
          print ("pH:")
          print (ph)
          count=count+1
      if (a == 'LightIntensity') : 
          count_l=b 
          lux.append(b)
          print ("Light Intensity:")
          print (lux)
          count=count+1
      if (count%6==0) : 
         x = datetime.datetime.now()
         sql = "INSERT INTO data_nct (temp,humi,lux,pH,ec,water_temp,timestamp) value (%s,%s,%s,%s,%s,%s,%s)"  
         val = (count_t,count_h,count_l,count_p,count_e,count_wt,x)
         mycursor.execute(sql,val)
         mydb.commit()
         if (count_t == 0 || count_h == 0 || count_l == 0 || count_p ==0 || count_e == 0 || count_wt == 0) :
             status['status'] = 'Sensor is not active'
             client.publish('v1/devices/me/telemetry',json.dumps(status),1)
         else :
             status['status'] = 'Sensor is active'
             client.publish('v1/devices/me/telemetry',json.dumps(status),1)
      file.write(c)
      file.seek(0,2)
client.loop_stop()
client.disconnect()
file.close()

