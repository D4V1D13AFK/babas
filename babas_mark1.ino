#include <Servo.h>

Servo servo;
Servo servo2;
Servo servo3;
Servo gripper;
char dato;
int angulo_hombro;
int angulo_codo;
int angulo_cintura;
int angulo_gripper;

void setup() {
  servo.attach(11);
  servo2.attach(10);
  servo3.attach(9);
  gripper.attach(6);
  Serial.begin(9600);

}

void loop() {
  if (Serial.available()>0){
    dato = Serial.read();
 
    
    if (dato == 'L'){
      angulo_hombro -= 2;
    }
    if (dato == 'R'){
      angulo_hombro += 2;
    }
    if (dato == 'E'){
      angulo_codo -= 2;
    }
    if (dato == 'H'){
      angulo_codo += 2;
    }
    if (dato == 'J'){
      angulo_cintura -= 2;
    }
    if (dato == 'K'){
      angulo_cintura += 2;
    }
    if (dato == 'D'){
      angulo_gripper -= 2;
    }
    if (dato == 'A'){
      angulo_gripper += 2;
    }
  }
  servo.write(angulo_hombro);
  servo2.write(angulo_codo);
  servo3.write(angulo_cintura);
  gripper.write(angulo_gripper);
}
