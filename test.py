#!/bin/bash

# Define questions and answers
questions=("What encoding algorithm converts binary data to ASCII text?" 
           "Which command helps us to controlling permission on windows?" 
           "What is central database of Windows OS?" 
           "What command helps us to schedule tasks in Windows?" 
           "I am not alive, but I grow; I don’t have lungs, but I need air; I don’t have a mouth, but water kills me. What am I?")
answers=("base64" "icacls" "registry" "schtasks" "fire")

# Function to ask questions
ask_questions() {
  for i in "${!questions[@]}"; do
    echo "Question $((i+1)): ${questions[i]}"
    read -p "Your answer: " user_answer
    if [ "${user_answer,,}" != "${answers[i]}" ]; then
      echo "Incorrect answer. Try again!"
      exit 1
    fi
  done
  
  generate_gpg_file
}

# Define the flag text
FLAG_TEXT="Congratulations! Here is your flag: CTF{You_Are_A_Crypto_Master_~--~nissan~--~}"

# Function to generate a GPG-encrypted file
generate_gpg_file() {
  echo "Creating a GPG-encrypted file with your flag..."
  echo "$FLAG_TEXT" > flag.txt
  gpg --symmetric --cipher-algo AES256 --passphrase nissan --batch flag.txt
  if [ $? -eq 0 ]; then
    echo "GPG file created successfully: flag.txt.gpg"
    rm flag.txt
  else
    echo "Failed to create GPG file."
  fi
}

# Start the quiz
echo "Welcome to the CTF challenge! Answer all questions correctly to get the flag."
ask_questions
