 
package fizzbuzz2;

import java.util.*;  
import java.util.stream.IntStream; 

public class FizzBuzz2English { 
    
    public static void main(String args[]){  
        Scanner scanner = new Scanner(System.in);  
        System.out.print("Enter The Number:");  
        int number = scanner.nextInt();  
        IntStream.rangeClosed(1, number).mapToObj(i->i%3==0?(i%5==0? "FizzBuzz ":"Fizz "):(i%5==0? "Buzz ": i+" ")).forEach(System.out::print);  
        scanner.close();  
    }  
}  