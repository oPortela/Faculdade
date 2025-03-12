#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void swap(char **a, char **b) {
    char *temp = *a;
    *a = *b;
    *b = temp;
}

int partition(char **words, int low, int high) {
    char *pivot = words[high];  
    int i = low - 1; 

    for (int j = low; j < high; j++) {
        if (strcmp(words[j], pivot) <= 0) {
            i++;  
            swap(&words[i], &words[j]);
        }
    }
    swap(&words[i + 1], &words[high]);
    return i + 1;
}


void quickSort(char **words, int low, int high) {
    if (low < high) {
        int pi = partition(words, low, high);

        quickSort(words, low, pi - 1);
        quickSort(words, pi + 1, high);
    }
}

int readWordsFromFile(const char *filename, char ***words) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Erro ao abrir o arquivo");
        return -1;
    }

    int capacity = 10000;
    int count = 0;
    *words = malloc(capacity * sizeof(char *));
    if (!*words) {
        perror("Erro ao alocar memória");
        fclose(file);
        return -1;
    }

    char buffer[256];
    while (fgets(buffer, sizeof(buffer), file)) {
        buffer[strcspn(buffer, "\n")] = 0;

        (*words)[count] = strdup(buffer);
        if (!(*words)[count]) {
            perror("Erro ao alocar memória");
            fclose(file);
            return -1;
        }

        count++;
        if (count >= capacity) {
            capacity *= 2;
            *words = realloc(*words, capacity * sizeof(char *));
            if (!*words) {
                perror("Erro ao realocar memória");
                fclose(file);
                return -1;
            }
        }
    }

    fclose(file);
    return count;
}

int main() {
    char **words;
    int wordCount = readWordsFromFile("dicionario.txt", &words);

    if (wordCount < 0) {
        return 1;
    }

    clock_t start = clock();
    quickSort(words, 0, wordCount - 1);
    clock_t end = clock();

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Tempo de execução: %.6f segundos\n", time_spent);

    for (int i = 0; i < 10; i++) {
        printf("%s\n", words[i]);
    }

    for (int i = 0; i < wordCount; i++) {
        free(words[i]);
    }
    free(words);

    return 0;
}