int moistureSensor = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(moistureSensor);
  Serial.println(sensorValue);
  delay(1000);
}
