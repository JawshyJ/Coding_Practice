//This old code was made for a class exercise, where we have to accept a correct SSN input and reject an incorrect SSN input

import java.util.Scanner;
public class CheckSSN{
   public static void main(String args[]){

   Scanner input = new Scanner(System.in);
   System.out.println("Type your Social Security Number (SSN) in this format XXX-XX-XXXX:");
   String SSN = input.next();

   String S1 = SSN.substring(1,3);
   String S2 = SSN.substring(4,6);
   String S3 = SSN.substring(7);

   if (SSN.length() == 11){ //&& SSN.substring(0,3).isDigit() && SSN. isDigit() && SSN. isDigit()
   System.out.println("You entered: " + SSN);
   }else{
   System.out.println("You entered an invalid SSN.");
   System.out.println(SSN);
   }

   //if (SSN. isDigit() && SSN. isDigit() && SSN. isDigit()){
   //}

   }
}
