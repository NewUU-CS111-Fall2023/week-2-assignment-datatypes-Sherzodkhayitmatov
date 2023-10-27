// task_1.h
bool isLeapYear(int year);

// main.cpp
#include "task_1.h"
#include <iostream>

int main() {
  int year;
  std::cout << "Enter a year: ";
  std::cin >> year;

  if (isLeapYear(year)) {
    std::cout << year << " is a leap year.\n";
  } else {
    std::cout << year << " is not a leap year.\n";
  }

  return 0;
}