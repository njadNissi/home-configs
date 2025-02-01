#!/bin/bash

# Use sudo to get root privileges
sudo expect -c "
  spawn shutdown -h now
  expect \"Password:\"
  send \"your_password\r\"
  interact
"
