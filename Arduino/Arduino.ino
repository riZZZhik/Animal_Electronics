#define backward 1
#define forward 2
#define left 3
#define right 4
#define LEFT 5
#define RIGHT 6
#define wheel 0.25
#define clockwise 7
#define unclockwise 8
float v0 = wheel / 255;
int a = 0;
int b = 0;
int c = 0;
int d = 0;
int e = 0;
String x;

void setup()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
{
 pinMode(12, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(10, OUTPUT);
   pinMode(6, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(9, OUTPUT);
    pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
    pinMode(50, OUTPUT);
  pinMode(51, OUTPUT);
    pinMode(52, OUTPUT);
  pinMode(53, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0)
  {
    x = Serial.readString();
    a = round(x[0] * 100 + x[1] * 10 + x[2]) - 255;
    b = round(x[4] * 100 + x[5] * 10 + x[6]) - 255;
    c = round(x[8] * 100 + x[9] * 10 + x[10]) - 255;
    d = round(x[12] * 100 + x[13] * 10 + x[14]) - 255;
    e = round(x[16] * 100 + x[17] * 10 + x[18]) - 255;
  }
  
  motors(a, b, c, d);
  delay(0.25);
  

  /*if (e > 0) {
    turn(LEFT, 254, e);
    delay(0.1);
  }
  else if (e < 0) {
    turn(RIGHT, 254, e);
    delay(0.1);
  }*/
}
