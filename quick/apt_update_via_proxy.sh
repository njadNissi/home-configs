export http_proxy="http://localhost:7890"
export https_proxy="http://localhost:7890"
sudo apt update  # Try again after setting the proxy
unset http_proxy https_proxy #remove proxy settings after testing
