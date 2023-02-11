#include <iostream>
#include <cstring>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <vector>

const int SERVER_PORT = 12345; // Replace with the last 4 digits of your UM-ID

// User class to store user information
class User {
 public:
  User(int id, float balance) : id(id), balance(balance) {}
  int id;
  float balance;
};

// Stock class to store stock information
class Stock {
 public:
  Stock(std::string symbol, float price, int amount)
      : symbol(symbol), price(price), amount(amount) {}
  std::string symbol;
  float price;
  int amount;
};

// Function to process BUY command
void processBuy(std::vector<User> &users, std::vector<Stock> &stocks,
                int userId, float stockPrice, int stockAmount, std::string symbol) {
  for (auto &user : users) {
    if (user.id == userId) {
      float totalPrice = stockPrice * stockAmount;
      if (user.balance < totalPrice) {
        std::cout << "Not enough balance" << std::endl;
        return;
      }
      user.balance -= totalPrice;
      bool stockExists = false;
      for (auto &stock : stocks) {
        if (stock.symbol == symbol) {
          stock.amount += stockAmount;
          stockExists = true;
          break;
        }
      }
      if (!stockExists) {
        stocks.push_back(Stock(symbol, stockPrice, stockAmount));
      }
      std::cout << "200 OK " << user.balance << " "
                << stockAmount * stockPrice << std::endl;
      return;
    }
  }
  std::cout << "User not found" << std::endl;
}

// Function to process SELL command
void processSell(std::vector<User> &users, std::vector<Stock> &stocks,
                 int userId, float stockPrice, int stockAmount, std::string symbol) {
  for (auto &user : users) {
    if (user.id == userId) {
      bool stockExists = false;
      for (auto &stock : stocks) {
        if (stock.symbol == symbol) {
          if (stock.amount < stockAmount) {
            std::cout << "Not enough stocks" << std::endl;
            return;
          }
          stock.amount -= stockAmount;
          user.balance += stockPrice * stockAmount;
          stockExists = true;
          break;
        }
      }
      if (!stockExists) {
        std::cout << "Stock not found" << std::endl;
        return;
      }
      std::cout << "200 OK " << user.balance << " "
                << stockAmount * stockPrice << std::endl;
      return;
    }
  }
  std::cout << "User not found" << std::endl;
}
// Function to process LIST command
void processList(std::vector<User> &users, std::vector<Stock> &stocks,
                 int userId, float stockPrice, int stockAmount, std::string symbol){

}

// Function to process BALANCE command
void processBalance(){

}

// Function to process SHUTDOWN command
void processShutdown(){

}

// FUnction to process QUIT command
void processQuit(){
  
}
