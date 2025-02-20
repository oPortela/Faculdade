//def contar_vogais(texto0):
//   vogais = ['a', 'e', 'i', 'o', 'u']

   // Your First Program

import java.util.Scanner;

public class SomaEMedia {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantos números você deseja somar e calcular a média? ");
        int quantidadeNumeros = scanner.nextInt();

        int soma = 0;

        for (int i = 1; i <= quantidadeNumeros; i++) {
            System.out.print("Digite o número " + i + ": ");
            int numero = scanner.nextInt();
            soma += numero;
        }

        double media = (double) soma / quantidadeNumeros;

        System.out.println("A soma dos números é: " + soma);
        System.out.println("A média dos números é: " + media);

        scanner.close();
    }
}