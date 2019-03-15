# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
   
    g = float(input("Digite la calificacion del alumno"))
   
    if g >= 9.5:
        print "Su calificacion es: A+ "
    elif g>= 9.0 and g<9.5:
            print "Su calificacion es: A-"
    elif g>=8.5 and g<9.0:
        print "Su calficacion es: B+"
    elif g>=8 and g<8.5:
        print "Su calificacion es: b-"
    elif g<=7.9:
        print"El alumno ha reprobado"
    else:
        print "comando no valido"    
    
    
            
            
