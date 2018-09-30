int relyPinOne = 8;
int relyPinTwo = 12;

int relyPinThree = 13;
int relyPinFour = 11;

int direction_rotate = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(relyPinOne, OUTPUT);
  pinMode(relyPinTwo, OUTPUT);

  pinMode(relyPinThree, OUTPUT);
  pinMode(relyPinFour, OUTPUT);
  Serial.begin(9600);
  
  digitalWrite(relyPinOne, LOW );
  digitalWrite(relyPinTwo, LOW );
  digitalWrite(relyPinThree, LOW );
  digitalWrite(relyPinFour, LOW );
  
  Serial.println("This is my First Example.");
}

void rotate_motor_one_right(){
   digitalWrite(relyPinTwo, LOW );
   digitalWrite(relyPinOne, LOW );
   digitalWrite(relyPinTwo, HIGH );
}

//Motor One
void rotate_motor_one_left(){
   digitalWrite(relyPinTwo, LOW );
   digitalWrite(relyPinOne, LOW );
   digitalWrite(relyPinOne, HIGH );
}

void rotate_motor_one_stop(){
   digitalWrite(relyPinTwo, LOW );
   digitalWrite(relyPinOne, LOW );
}

//Motor Two
void rotate_motor_two_right(){
   digitalWrite(relyPinThree, LOW );
   digitalWrite(relyPinFour, LOW );
   digitalWrite(relyPinFour, HIGH );
}

void rotate_motor_two_left(){
   digitalWrite(relyPinThree, LOW );
   digitalWrite(relyPinFour, LOW );
   digitalWrite(relyPinThree, HIGH );
}

void rotate_motor_two_stop(){
   digitalWrite(relyPinThree, LOW );
   digitalWrite(relyPinFour, LOW );
}

int delay_b = 40;
void loop() {
  while (Serial.available())
  {
    direction_rotate = Serial.read();
  }

  if (direction_rotate == '1'){
     Serial.println("Right Motor One");
     rotate_motor_one_right();
     delay(delay_b);
     rotate_motor_one_stop();
     direction_rotate = 0;
     
  }

  if (direction_rotate == '2'){
     Serial.println("Left Motor One");
     rotate_motor_one_left();
     delay(delay_b);
     rotate_motor_one_stop();
     direction_rotate = 0;
  }

  if (direction_rotate == '3'){
     Serial.println("Stop Motor One");
     rotate_motor_one_stop();
     direction_rotate = 0;
  }

    if (direction_rotate == '4'){
     Serial.println("Right Motor Two");
     rotate_motor_two_right();
     delay(delay_b);
     rotate_motor_two_stop();
     direction_rotate = 0;
  }

  if (direction_rotate == '5'){
     Serial.println("Left Motor Two");
     rotate_motor_two_left();
     delay(delay_b);
     rotate_motor_two_stop();
     direction_rotate = 0;
  }

  if (direction_rotate == '6'){
     Serial.println("Stop Motor Two");
     rotate_motor_two_stop();
     direction_rotate = 0;
  }
//
//  // put your main code here, to run repeatedly:
//    delay(1000);
//      digitalWrite(relyPinTwo, HIGH );
//      Serial.println("pin two off");
//
//       delay(1000);
//      digitalWrite(relyPinOne, HIGH);
//      Serial.println("Turing off pin one");
//       delay(1000);
//       
//      digitalWrite(relyPinTwo, LOW );
//       delay(1000);
//
//      digitalWrite(relyPinOne, HIGH );
//     Serial.println("pin two off");
//   
//           
//      digitalWrite(relyPinTwo, HIGH );
//       delay(1000);
//
//      digitalWrite(relyPinOne, LOW );

  
      
 
}
