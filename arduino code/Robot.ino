 char i;


void setup() 
{
  pinMode(3, OUTPUT);   
  pinMode(4,OUTPUT);    
  pinMode(5,OUTPUT); 
  pinMode(6,OUTPUT);    
  Serial.begin(9600);
  

}

void loop() {
 while(Serial.available()>0)
  {
     i=Serial.read(); 
     if(i=='F')                       
     {
        Serial.println("Moving Forward");
        digitalWrite(3, HIGH);        
        digitalWrite(4, LOW);
        digitalWrite(5, HIGH);
        digitalWrite(6, LOW);
      }
     if(i=='B')                         
     {  
        Serial.println("Moving Reverse");
        digitalWrite(3, LOW);        
        digitalWrite(4, HIGH);
        digitalWrite(5, LOW);
        digitalWrite(6, HIGH);
         
     }
     if(i=='L')                       // Load
     {
        Serial.println("Moving Left");
        digitalWrite(3, LOW);        
        digitalWrite(4, LOW);
        digitalWrite(5, HIGH);
        digitalWrite(6, LOW);
     }
     if(i=='R')
     {
        Serial.println("Moving Right");
        digitalWrite(3, HIGH);        
        digitalWrite(4, LOW);
        digitalWrite(5, LOW);
        digitalWrite(6, LOW);
     }
     if(i=='S')
     {  
        Serial.println("Stop");
        digitalWrite(3, LOW);        
        digitalWrite(4, LOW);
        digitalWrite(5, LOW);
        digitalWrite(6, LOW);
     }
   }
}
  
 
