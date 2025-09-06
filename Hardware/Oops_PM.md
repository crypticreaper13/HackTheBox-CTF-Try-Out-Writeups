# Hardware Challenges – HackTheBox TryOuts

This document contains my writeups for the **Hardware CTF challenges** from HTB TryOuts.  


# Oops PM – Hardware Challenge

## Challenge Overview
This challenge was based on a **Trusted Platform Module (TPM)** – a chip used in computers to securely store keys, passwords, and other sensitive information.  
The task was to analyze the provided **VHDL code** to uncover a hidden **backdoor** that exposes the secret key.

## 🛠️ Files Provided
- `TPM.vhdl` – main TPM logic  
- `backdoor.vhdl` – suspicious code  
- `encryption.vhdl` – encryption logic  
- `key.vhdl` – contains the secret key  

## Analysis
1. **Normal TPM Behavior:**  
   - Takes `Data` as input  
   - Encrypts it with a `Key`  
   - Decides (via logic) whether to store or output the encrypted data  

2. **The Flaw (Backdoor):**  
   - In `backdoor.vhdl`, I found a condition where if the **input matches a specific pattern**, the TPM doesn’t encrypt data.  
   - Instead, it **directly outputs the secret key**.  
   - This is a serious security issue, because attackers can bypass normal TPM protection.

## Solution Path
- I inspected the `backdoor.vhdl` code.  
- The trigger input was clearly defined:  "1111111111101001"
- 
- When the Docker is spawned, it asked for an input.  
- I provided this sequence as input.  
- The TPM immediately revealed the **flag**.

## Flag: HTB{------}


