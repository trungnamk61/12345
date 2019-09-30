//define lora
#define rx 16                                          //LORA TX
#define tx 17                                          //LORA RX
HardwareSerial myserial(1);
void setup() {
    Serial.begin(9600);
    myserial.begin(9600, SERIAL_8N1, rx, tx);
}      
String a = "temp";
int temp = 25;
String b = "humi";
int humi = 30;
String c = "ec";
int ec = 1500;
String d = "pH";
int pH = 7;
String e = "lux";
int lux = 100;
void loop() {
      Serial.println(a);
      delay(50);
      Serial.println(temp);
      delay(1000);
      Serial.println(b);
      delay(50);
      Serial.println(humi);
      delay(1000);
      Serial.println(c);
      delay(50);
      Serial.println(ec);
      delay(1000);
      Serial.println(d);
      delay(50);
      Serial.println(pH);
      delay(1000);
      Serial.println(e);
      delay(50);
      Serial.println(lux);
      delay(1000);
}
