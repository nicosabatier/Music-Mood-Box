const int sensorPin = 2;
const int sensor2Pin = 4;
const int sensor3Pin = 13;

// variables:
int lum_sensorValue = 0;
int temp_sensorValue = 0;
int sensorMin = 1023; // minimum sensor value 
int sensorMax = 0; // maximum sensor value
int mvmnt_sensorValue = -1;


void setup() {
  pinMode(13, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // read the sensor:
  lum_sensorValue = analogRead(sensorPin);
  temp_sensorValue = analogRead(sensor2Pin);
  mvmnt_sensorValue = analogRead(sensor3Pin);

  
  byte * lum_b = (byte *) &lum_sensorValue;
  //byte * temp_b = (byte *) &temp_sensorValue;
  temp_sensorValue = constrain(temp_sensorValue, 0, 1023); 
  float temp = ((temp_sensorValue/1023.01) - 0.5 ) / 0.01;
  byte * temp_b = (byte *) &temp;

  int mvmnt = 0;
  if (mvmnt_sensorValue>0){
    mvmnt=1;
  }
  byte * mvmnt_b = (byte *) &mvmnt;

  
  Serial.write(lum_b,4);
  Serial.write(temp_b,4);
  Serial.write(mvmnt_b,4);

  //Serial.print("sensor 1: ");
  //Serial.println(lum_sensorValue);
  //Serial.print("sensor 2: ");
  //Serial.println(temp);
  //Serial.print("sensor 3: ");
  //Serial.println(mvmnt);
  
  delay(1000);
}
