#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> tasks = {
        "Review PR",
        "Train model",
        "Write documentation"
    };

    std::cout << "Today's tasks:\n";
    for (size_t i = 0; i < tasks.size(); ++i) {
        std::cout << i + 1 << ". " << tasks[i] << std::endl;
    }
    return 0;
}
