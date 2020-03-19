#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <FS.h>


#define LAMP_PIN        D5              // lamp control pin, connect to a relay


#define HOSTNAME        "lumen"         // hostname of the device, making at accessable under HOSTNAME.local
#define PORT            80              // communication port (default: 80)

#define STA_SSID        "ssid"          // SSID of the network to connect to
#define STA_PSK         "password"      // password of the network to connect to


ESP8266WebServer server(PORT);
volatile bool lampOn = false;


void handleRequest() {
	String argName = server.argName(0);
	String arg = server.arg(0);
	
	if (argName.equals("state")) {
		if (lampOn) {
			if (arg.equals("off")) {
				digitalWrite(LAMP_PIN, LOW);
				lampOn = false;
			}
		}
		else if (arg.equals("on")) {
			digitalWrite(LAMP_PIN, HIGH);
			lampOn = true;
		}
	}
	server.send(200, "text/plain", "");
}


void handleNotFound() {
	String message = "<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'><title>WFHD control</title></head><body><h1 align='center' style='font-family:Arial'>404: Not Found</h1></body></hmtl>";
	server.send(404, "text/html", message);
}


void setup() {
	pinMode(LAMP_PIN, OUTPUT);
	digitalWrite(LAMP_PIN, LOW);
	
	Serial.begin(115200);
	WiFi.mode(WIFI_STA);
	WiFi.begin(STA_SSID, STA_PSK);
	while (WiFi.status() != WL_CONNECTED) {
		delay(500);
	}
	
	MDNS.begin(HOSTNAME);
	SPIFFS.begin();
	server.on("/", handleRequest);
	server.onNotFound(handleNotFound);
	server.begin();
}


void loop() {
	server.handleClient();
	MDNS.update();
}
