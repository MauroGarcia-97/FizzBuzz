 
package fizzbuzz2;

import java.util.*;  
import java.util.stream.IntStream; 

public class FizzBuzz2Spanish { 
    
    public static void main(String args[]){  
        Scanner escaner = new Scanner(System.in);  
        System.out.print("Ingrese El Numero: ");  
        int numero = escaner.nextInt();  
        IntStream.rangeClosed(1, numero).mapToObj(i->i%3==0?(i%5==0? "FizzBuzz ":"Fizz "):(i%5==0? "Buzz ": i+" ")).forEach(System.out::print);  
        escaner.close();  
    }  
}  