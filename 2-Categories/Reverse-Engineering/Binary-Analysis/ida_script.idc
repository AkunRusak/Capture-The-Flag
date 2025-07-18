// IDA IDC Script - rename function and set comments

static main() {
  auto addr;

  // Rename main function
  MakeName(0x08048400, "main");

  // Comment at address
  addr = 0x0804842A;
  MakeComm(addr, "Compare user input with correct password");
}