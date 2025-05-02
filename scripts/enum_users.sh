#!/bin/bash

echo "[*] Enumerating through /home dir..."
for user in /home/*; do
  if [ -d "$user" ]; then
    echo -e "\n: User = $(basename $user)"
    echo "[+] Listing files in $user"
      ls -la "$user"

      echo "[+] Checking .bash_history:"
      if [ -f "$user/.bash_history" ]; then
        cat "$user/.bash_history"
      else
        echo "No .bash_history found for $user"
    fi
    echo "[+] Checking .ssh keys"
      if [ -d "$user/.ssh" ]; then
        ls -la "$user/.ssh"
        cat "user/.ssh/id_rsa" 2>/dev/null
        cat "$user/.ssh/authorized_keys" 2>/dev/null
      else
        echo "No .ssh directory found"
      fi
      echo "[+] Searching for cleartext passwords:"
      grep -i 'pass\|user\|login' "$user"/* 2>/dev/null
    fi
done
