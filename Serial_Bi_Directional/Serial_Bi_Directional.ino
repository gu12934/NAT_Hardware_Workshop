int dataIn;         // to hold incoming data

const int ledPin = 6;

void setup() {
  pinMode(ledPin, OUTPUT); 
  digitalWrite(ledPin, LOW);
  Serial.begin(9600);  // initialize serial:
}

void loop() {
  delay(2);
  while (Serial.available() > 0) {
    dataIn = Serial.parseInt();
    analogWrite(ledPin, dataIn); 
    Serial.println(analogRead(A1)); //Determine which Arduino pin is input and write it here. Must be an ANALOG pin
  }
  
}
