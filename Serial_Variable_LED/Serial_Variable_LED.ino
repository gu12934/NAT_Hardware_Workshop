int dataIn;         // to hold incoming data

const int ledPin = 6;

void setup() {
  pinMode(ledPin, OUTPUT); 
  digitalWrite(ledPin, LOW);
  Serial.begin(9600);  // initialize serial:
}

void loop() {
  while (Serial.available() > 0) {
    dataIn = Serial.parseInt();
    analogWrite(ledPin, dataIn); 
  }
  
}
