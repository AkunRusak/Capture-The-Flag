int main(void) {
    char input[32];

    printf("Enter serial: ");
    scanf("%s", input);

    if (strcmp(input, "CTF2025") == 0) {
        puts("Correct!");
    } else {
        puts("Wrong serial.");
    }
    return 0;
}