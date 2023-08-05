import java.util.Scanner;

public class task3
{
    public static void main(String[] args) {
        Scanner yearinput = new Scanner(System.in);
        int yearl = yearinput.nextInt();
        if (yearl % 400 == 0 & yearl % 100 == 0)
            System.out.println("A leap year ");
        else
            System.out.println("Not a Leap Year");

    }
    

}
