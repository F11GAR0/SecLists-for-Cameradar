# SecLists-for-Cameradar
 Simple python converter for convert .txt usernames and password to .json cameradar credentials format.

# Usage:
```
python transform.py usernames.txt passwords.txt outcredentials.json
python push.py <-f(ront),-b(ack)> credentials.json Username Password
```

### Example what's going on:
    ** usernames.txt **
    ```
    admin
    root
    ```
    ** passwords.txt **
    ```
    admin
    qwerty12345
    toor
    root
    ```
    ** Enterning command: **
    ```
    python transform.py usernames.txt passwords.txt outcredentials.json
    ```

    ** outcredentials.json **
    ```
    {
        "usernames":
        ["admin", root],
        "passwords":
        ["admin", "qwerty12345", "toor", "root"]
    }
    ```

Big lists you can find on: https://github.com/danielmiessler/SecLists