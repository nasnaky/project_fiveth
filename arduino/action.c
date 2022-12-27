#include <WiFi.h>
#include<ArduinoJson.h>

#define HOME_SSID  "wi_gen"
#define HOME_PASSWORD  "gsmhs6800%"
#define POT "" // 센서 연결 핀
#define WA "http://10.82.18.147:8001/" //웹 주수


WiFiServer server(80);

void setup(){ // 서버연결
    Serial.begin(115200);

    delay(10);

    Serial.println();
    Serial.println();
    Serial.print("link : ");
    Serial.println(HOME_SSID);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("");
    Serial.println("WiFi connected.");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());

    server.begin();
}



int jsonse(){
    String jsondata = "";
    StaticJsonBuffer<256> jsonBuffer;
    JsonObject& root = jsonBuffer.createObject();
    root["TEMP"]  = ???; // 주소 저장 
    root.printTo(jsondata)


}