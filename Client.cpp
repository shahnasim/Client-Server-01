#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define SERVER_PORT 12345 // Replace this with the last 4 digits of your UM-ID
#define MAX_BUFFER_LENGTH 1024

using namespace std;

int main(int argc, char *argv[]) {
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " <server_ip>" << endl;
    return 1;
  }

  int sockfd;
  struct sockaddr_in serv_addr;

  if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
    cerr << "Error: Unable to create socket" << endl;
    return 1;
  }

  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family = AF_INET;
  serv_addr.sin_port = htons(SERVER_PORT);

  if (inet_pton(AF_INET, argv[1], &serv_addr.sin_addr) <= 0) {
    cerr << "Error: Invalid server IP address" << endl;
    return 1;
  }

  if (connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
    cerr << "Error: Unable to connect to server" << endl;
    return 1;
  }

  while (true) {
    cout << "Enter command (BUY, SELL, LIST, BALANCE, SHUTDOWN, QUIT): ";
    string cmd;
    cin >> cmd;

    string request;
    if (cmd == "BUY") {
      string stock_symbol, user_id;
      int stock_amount;
      double price;
      cout << "Enter stock symbol: ";
      cin >> stock_symbol;
      cout << "Enter stock amount: ";
      cin >> stock_amount;
      cout << "Enter price per stock: ";
      cin >> price;
      cout << "Enter user ID: ";
      cin >> user_id;
      request = cmd + " " + stock_symbol + " " + to_string(stock_amount) + " " + to_string(price) + " " + user_id + "\n";
    } else if (cmd == "SELL") {
      string stock_symbol, user_id;
      int stock_amount;
      double price;
      cout << "Enter stock symbol: ";
      cin >> stock_symbol;
      cout << "Enter stock amount: ";
      cin >> stock_amount;
      cout << "Enter price per stock: ";
      cin >> price;
      cout << "Enter user ID: ";
      cin >> user_id;
      request = cmd + " " +
