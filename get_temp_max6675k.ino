#include <max6675.h>

const int port_sck = 8;
const int port_cs = 9;
const int port_so = 10;

MAX6675 thermocouple(port_sck, port_cs, port_so);

void setup() {
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  Serial.println(thermocouple.readCelsius());

  delay(1000);
}
