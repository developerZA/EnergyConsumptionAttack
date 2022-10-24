#include <Wire.h> 
#include "EmonLib.h" 
#include <SPI.h> 
#include <Ethernet.h>
#include "Thread.h"
#include "ThreadController.h"
EnergyMonitor emon1;
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
byte ip[] = { 192, 168, 0, 178 }; 
byte IP4Address[] = { 127, 0, 0, 1}; 
byte gateway[] = { 192, 168, 0, 1 }; 
byte subnet[] = { 255, 255, 255, 0 }; 
EthernetClient cliente; 
double sensor_data=0;
String readString;
unsigned long previousMillis=0; 
double A=0.0;
double v=0.0;
double watt=0.0;
int sec=0;
int hours=1;
int count=0;
int led = 5; 
EthernetServer server(80);
int digitalReadOutputPin(uint8_t pin)
{
 uint8_t bit = digitalPinToBitMask(pin);
 uint8_t port = digitalPinToPort(pin);
 if (port == NOT_A_PIN) 
   return LOW;

 return (*portOutputRegister(port) & bit) ? HIGH : LOW;
}

ThreadController mainThread;

Thread threadDofun1;

void function1(){
       Serial.println("loop1");
        double Irms=emon1.calcIrms(1480);
        if(Irms==NULL){
         Irms = 0.0;
        }
        //check if the pin have electricity
        if(digitalReadOutputPin(3) == 1){
            Irms=0.00;
        }
        Serial.print("Amp= ");
        Serial.println(Irms);
        Serial.print(Irms);
        A = (A + (Irms * 220))/2;
        v=A/Irms;
        Serial.print("A=");
        Serial.println(A);
        Serial.println("W=");
        Serial.println(v);
        sensor_data=Irms;
}
Thread threadDofun2;
void function2(){
   Serial.println("I am in loop 2 I will send data in one hour");
   Ethernet.begin(mac, ip, gateway, subnet);
  if (count == 2){ //239
  if (cliente.connect(IP4Address, 80)) {
        Serial.println("connected");
        watt = A ;
        cliente.print("GET /power.php?"); 
        cliente.print("watt=");
        cliente.print(watt);
        cliente.print("&hours=");
        cliente.print(hours);
        cliente.print("&id=");
        cliente.println(1); 
        cliente.print("&vol=");
        cliente.println(v); 
        Serial.print("watt=");
        Serial.println(watt);
        Serial.print("hours= ");
        Serial.println(hours);
        cliente.stop();
        hours = 1;
        watt = 0.0;
        A = 0.0;  
      } else {
        Serial.println("connection failed");
        hours++;
      }
      count = 0;
  }
  count++;
}
void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600); 
   Ethernet.begin(mac, ip, gateway, subnet);
   server.begin(); 
   Serial.print("server is at ");
   Serial.println(Ethernet.localIP());
   pinMode(A1, INPUT);
   emon1.current(A1, 62);
   //***************************************
  threadDofun1.setInterval(1000);
  threadDofun1.onRun(function1);
  threadDofun2.setInterval(15000);
  threadDofun2.onRun(function2);
  mainThread.add(&threadDofun1);
  mainThread.add(&threadDofun2);
}

void loop() {

  EthernetClient client = server.available();
  double Irms=emon1.calcIrms(1480);
  if (client) {
    while (client.connected()) {   
      if (client.available()) {
        char c = client.read();
        //read char by char HTTP request
        if (readString.length() < 100) {
          readString += c;
          Serial.print(c);
         }
         if(digitalReadOutputPin(3) == 1){
            Irms=0.00;
        }
         //if HTTP request has ended
         if (c == '\n') {          
           Serial.println(readString);
          client.println("HTTP/1.1 200 OK"); 
          client.println("Content-Type: application/json");
          client.println(); 
          digitalReadOutputPin(led);
          client.print("{\"arduino\":[{\"current\":\"");
          client.print(sensor_data);
          client.print("\"},{\"pin3\":\"");
          client.print(digitalReadOutputPin(3));
          client.print("\"},{\"pin6\":\"");
          client.print(digitalReadOutputPin(6));
          client.print("\"}");
          client.print("]}");
          delay(1);
          client.stop();
         }
      }
    }
  }
  mainThread.run();
   /* Serial.print("Electric Meter");
    Serial.print(Irms);
    A = (A + (Irms * 220))/2;
    Serial.print("A=");
    Serial.println(A);
    sensor_data=Irms;
    Serial.println("");
    delay(2000);*/
}
