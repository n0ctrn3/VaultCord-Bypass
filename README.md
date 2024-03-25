**Step 1: Installation**

1. Clone or download the Python bypass script repository.
   ```
   git clone https://github.com/n0ctrn3/VaultCord-Bypass.git
   ```
2. Navigate to the repository directory.
   ```
   cd VaultCord-Bypass
   ```
3. Install the required dependencies by running:
   ```
   pip3 install -r requirements.txt
   ```

<hr>

**Step 2: Preparation on Discord**

1. On Discord, locate the URL in the embed of the message sent by the Vault Cord bot.
2. Copy the URL.

![Vault Cord URL](https://github.com/n0ctrn3/VaultCord-Bypass/blob/main/images/step2.png)

<hr>

**Step 3: Obtaining Redirect URI**

1. Open a new tab in your browser.
2. Paste the copied URL into the address bar.
3. Copy the redirect URI from the Discord OAuth2 URL.

![Redirect URI](https://github.com/n0ctrn3/VaultCord-Bypass/blob/main/images/step3.png)

<hr>

**Step 4: Setting Breakpoints**

1. Paste the redirect URI into the address bar and navigate to it.
2. Open DevTools and go to the Debugger tab.
3. Find and open `cdn.vaultcord.com`.
4. Locate the file `verify-1-0.js`.
5. Set breakpoints at line 63 and line 99, where the request body is formed.
   - **Note:** The line numbers may vary. Ensure that the breakpoints are set at the correct lines.

![Breakpoints](https://github.com/n0ctrn3/VaultCord-Bypass/blob/main/images/step4.png)

<hr>
   
**Step 5: Initiating Authorization**

1. Now press the "Verify" button that's on the site and keep DevTools open.
3. Authorize the OAuth2 application when prompted.

![Authorization](https://github.com/n0ctrn3/VaultCord-Bypass/blob/main/images/step5.png)

<hr>

**Step 6: Retrieving Credentials**

1. Once redirected, the debugger will stop the request.
2. Obtain the code, domain, and token from the request body by overing over the variables in the debugger and copying the values.
   - **NOTE:** If theres no token in the request body, it's not a problem, continue to the next step.
3. These values will be needed for the Python script.

![Credentials](https://github.com/n0ctrn3/VaultCord-Bypass/blob/main/images/step6.png)

<hr>

**Step 7: Running the Python Script**

1. Run the Python bypass script.
   ```
   python3 VaultCordBypass.py
   ```
2. When prompted, input the code, domain, and token obtained earlier.
   - **Note:** If you don't have a token, leave the `Cloudflare captcha token` input empty and press enter.
3. The Vault Cord protection should now be bypassed.

![Python Script](https://github.com/n0ctrn3/VaultCord-Bypass/blob/main/images/step7.png)

<hr>

**Note:** Ensure that you have obtained the necessary credentials and set breakpoints correctly for the script to work effectively.