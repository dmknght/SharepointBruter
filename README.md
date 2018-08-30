## About this project
Another URL brute forcing. But this project is aimed Sharepoint platform. I included some trick to get more information than a static wordlist and better result than regular tools (dirb, gobuster)

## Requirement
python2, mechanize

## Usage:
Bruter.py is a script that automatic brute path from wordlist.
  - `python Bruter.py <TARGET>`
Modu.py is a script that test a list of functions can be used on target platform. This script needs a custom wordlist
  - If you want to test functions like: "add user", "edit user", "change password"
  - run `python Modu.py <TARGET> adduser,edituser,changepassword` or create a text file and run
  - `python Modu.py <TARGET> $(cat <WORDLIST>)` 
  - This script is not fully tested. Google dork can be better in some case
  
## Quick modify
  Brute forcing id maximum is 50. If you want to change this value, go to `lib/actions.py`.
  Goto `bruteID` function at `line 13`. It should look like this `MAX_RANGE = 50`.
  I don't change it because i want simple options
 
Based
- `https://the-infosec.com/2017/04/18/penetration-testing-sharepoint/` Penetration testing Sharepoint
- `https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/CMS/sharepoint.txt` Sharepoint wordlist