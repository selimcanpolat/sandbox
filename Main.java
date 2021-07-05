package com.company;

import java.text.NumberFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner_principal = new Scanner(System.in);
        System.out.print("Principal: ");
        int P = scanner_principal.nextInt();

        Scanner scanner_interest_rate = new Scanner(System.in);
        System.out.print("Interest Rate: ");
        float r = scanner_interest_rate.nextFloat();
        r = r/1200;

        Scanner scanner_period = new Scanner(System.in);
        System.out.print("Period: ");
        int n = scanner_period.nextInt();
        n = n*12;

        double M = P*r*Math.pow((1+r),n)/(Math.pow(1+r,n)-1);

        NumberFormat mortgage = NumberFormat.getCurrencyInstance();
        String result = mortgage.format(M);

        System.out.println("Mortgage: " + result);
        
    }
}
