#define MOTOR1_EN 6
#define MOTOR1_INA1 2
#define MOTOR1_INB1 4
#define MOTOR1_PWM 9

#define MOTOR2_EN 12
#define MOTOR2_INA2 7
#define MOTOR2_INB2 8
#define MOTOR2_PWM 10

#define MOTOR3_EN  6
#define MOTOR3_INA3 51
#define MOTOR3_INB3 50
#define MOTOR3_PWM 5

#define MOTOR4_EN 12
#define MOTOR4_INA4 52
#define MOTOR4_INB4 53
#define MOTOR4_PWM 3

void motors(int m1, int m2, int m3, int m4)
{
  if (m1 > 255)
    m1 = 255;
  if (m1 < -255)
    m1 = -255;
  if (m2 > 255)
    m2 = 255;
  if (m2 < -255)
    m2 = -255;
  if (m3 > 255)
    m3 = 255;
  if (m3 < -255)
    m3 = -255;
  if (m4 > 255)
    m4 = 255;
  if (m4 < -255)
    m4 = -255;

  if (m1 > 0)
  {
    digitalWrite(MOTOR1_EN , HIGH);
    digitalWrite(MOTOR1_INA1, HIGH);
    digitalWrite(MOTOR1_INB1, LOW);
    analogWrite( MOTOR1_PWM, m1);
  }
  else
  {
    m1 = m1 * (-1);
    digitalWrite(MOTOR1_EN, HIGH);
    digitalWrite(MOTOR1_INA1, LOW);
    digitalWrite(MOTOR1_INB1, HIGH);
    analogWrite( MOTOR1_PWM, m1);
  }


  if (m2 > 0)
  {
    digitalWrite(MOTOR2_EN , HIGH);
    digitalWrite(MOTOR2_INA2, HIGH);
    digitalWrite(MOTOR2_INB2, LOW);
    analogWrite( MOTOR2_PWM, m2);
  }
  else
  {
    m2 = m2 * (-1);
    digitalWrite(MOTOR2_EN, HIGH);
    digitalWrite(MOTOR2_INA2, LOW);
    digitalWrite(MOTOR2_INB2, HIGH);
    analogWrite( MOTOR2_PWM, m2);
  }


  if (m3 > 0)
  {
    digitalWrite(MOTOR3_EN , HIGH);
    digitalWrite(MOTOR3_INA3, HIGH);
    digitalWrite(MOTOR3_INB3, LOW);
    analogWrite( MOTOR3_PWM, m3);
  }
  else
  {
    m3 = m3 * (-1);
    digitalWrite(MOTOR3_EN, HIGH);
    digitalWrite(MOTOR3_INA3, LOW);
    digitalWrite(MOTOR3_INB3, HIGH);
    analogWrite( MOTOR3_PWM, m3);
  }


  if (m4 > 0)
  {
    digitalWrite(MOTOR4_EN , HIGH);
    digitalWrite(MOTOR4_INA4, HIGH);
    digitalWrite(MOTOR4_INB4, LOW);
    analogWrite( MOTOR4_PWM, m4);
  }
  else
  {
    m4 = m4 * (-1);
    digitalWrite(MOTOR4_EN, HIGH);
    digitalWrite(MOTOR4_INA4, LOW);
    digitalWrite(MOTOR4_INB4, HIGH);
    analogWrite( MOTOR4_PWM, m4);
  }
}
