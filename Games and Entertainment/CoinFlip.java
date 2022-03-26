import java.util.Scanner;

public class CoinFlip{

public static void main(String[] Args){

int Coin = (int)(Math.random() * 2);

int Heads = 0;
int Tails = 0;

String text = "test";

Scanner input = new Scanner(System.in);

while(text.toLowerCase() != "exit"){
System.out.println("Flip?");
if (Coin == 1){
   System.out.println("Heads");
   System.out.println(Coin);
   Heads++;
}else{
   System.out.println("Tails");
   System.out.println(Coin);
   Tails++;
}
System.out.println("Heads: " + Heads);
System.out.println("Tails " + Tails);
}

}
}