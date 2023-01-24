#include <OneWire.h> 
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup(void) 
{
  Serial.begin(9600);
  sensors.begin();
}

void loop(void) 
{
 Serial.print("\n");
sensors.requestTemperatures();
 Serial.print(sensors.getTempFByIndex(0));
 delay(4000);
}
