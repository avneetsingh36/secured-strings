# SecuredStringsOSI: Password Manager and an OSI Network Approach

This project is a Python-based program that serves as a rudimentary password manager. It takes a user's password and stores it securely, using a file as an intermediary node. Notably, the design of the program is inspired by the OSI reference model's layered architecture; motivation to start and finish this project was to help better understand networking and the intracacies of the OSI Reference Model.

## Overview

The code utilizes seven layers, each representing a layer in the OSI model. It takes a password from the user, encrypts it, transmits it to an intermediary node (another file), and then makes it accessible to the final node.

Below is a quick walkthrough of each layer's functionality:

Application Layer: This layer collects the password from the user.
Presentation Layer: The password is encrypted here using various techniques, including basic mathematical operations and ASCII conversions.
Session Layer: A connection is established with the intermediary node via file manipulation.
Transport Layer: The size of the encrypted password is checked to determine if the information needs to be segmented before transmission.
Network Layer: Routing checks are conducted. In this case, the only path is to our intermediary node.
Data Link Layer: The encrypted password is transmitted to the intermediary node and stored in binary form.
Physical Layer: The medium of communication and bit synchronization is described.
The program is then executed in a sequence that resembles a network communication process.

## Setup

You'll need Python 3 installed on your machine. Once that's set up, you can clone this repository to your local machine. Make sure to set the correct path to your intermediaryNode.txt file in the code.

## Usage

To use this program, run python3 file1.py in your terminal. Follow the prompts to input your password. The program will then execute all the layers described above, and you'll see a step-by-step output in your terminal.

## Note

This program is only a simulation of a network communication process using the OSI model. While it does "encrypt" passwords and move them to a separate file, it doesn't offer real security and shouldn't be used to store important passwords or data. The primary goal here is to create a learning tool for understanding the OSI model and network communication processes.

Feel free to explore and modify the code as you wish to better understand the concepts or add more features.

### Contributor
- [Avneet Singh](https://github.com/avneetsingh36)

Special thanks to [@slano-ls](https://github.com/slano-ls) for guidance on this project.
