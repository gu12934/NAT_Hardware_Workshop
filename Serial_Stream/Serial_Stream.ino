int brightness = 0; 

const int ledPin = 13;

void setup() { 
   pinMode(ledPin, OUTPUT); 
   digitalWrite(ledPin, LOW);

  Serial.begin(9600); 
 }

 void loop() {
   int numchars=Serial.available();
   if ( numchars> 0){
     char serialdata[numchars+1];
     Serial.readBytes(serialdata,numchars);
     brightness = atoi(serialdata);
     Serial.println(brightness); 

   }
   analogWrite(ledPin, brightness); 
 }
