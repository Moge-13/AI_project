#include <stdio.h>

void log_message(const char *level, const char *message) {
    printf("[%s] %s\n", level, message);
}

int main() {
    log_message("INFO", "Application started");
    log_message("WARN", "Low disk space");
    log_message("ERROR", "Failed to open file");
    return 0;
}
