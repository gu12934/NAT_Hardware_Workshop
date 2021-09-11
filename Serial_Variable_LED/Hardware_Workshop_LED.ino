

String inputString = "";         // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

int brightness = 0; 

const int ledPin = 6;

void setup() {
  pinMode(ledPin, OUTPUT); 
  digitalWrite(ledPin, LOW);
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    Serial.println(inputString);
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
  analogWrite(ledPin, brightness); 
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
  brightness = inputString.toInt();  
}
