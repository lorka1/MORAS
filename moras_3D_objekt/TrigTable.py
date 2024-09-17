import math

content = """
class Trig {
  field Array sinTable;
  constructor Trig new(){
    let sinTable = Array.new(360);
INSERT
    return this;
  }
  method int sin(int degrees){
    if(degrees < 0) {
      let degrees = - degrees;
    }
    while(degrees > 359){
      let degrees = degrees - 360;
    }
    return sinTable[degrees];
  }
  method int cos(int degrees){
    let degrees = 90 - degrees;
    if(degrees < 0) {
      let degrees = - degrees;
    }
    while(degrees > 359){
      let degrees = degrees - 360;
    }
    return sinTable[degrees];
  }
  method void dispose() {
    do Memory.deAlloc(sinTable);
    return;
  } 
}
"""

sin_table = [f'    let sinTable[{i}] = {int(math.sin(math.radians(i))*100)};' for i in range(360)]

content = content.replace('INSERT', '\n'.join(sin_table))

f = open('Trig.jack', 'w')

f.write(content)

f.close()