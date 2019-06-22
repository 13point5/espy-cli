# espy-cli
A CLI tool to easily manage your ESP-IDF projects.

# Features
* Manage all your projects and change their configuration with ease
* Use multiple IDF versions without the need to update Environment variables
* Change the IDF used in a project at any time.

### Note
> Projects are called apps.<br>
> Before creating an app make sure you have added atleast 1 IDF path.<br>
> In case you forget espy will remind you :bowtie:

# Usage
1. Managing IDFs
    * Add a new IDF
        ```
        $ espy idf new -n idf1 -f /home/user/esp/esp-idf

        Successfully added idf1 to config
        ```

    * Get all or specific IDF(s)
        ```
        $ espy idf get

        +------+--------------------------------------+
        | name | filepath                             |
        +------+--------------------------------------+
        | idf1 | /home/user/esp/esp-idf               |
        | idf2 | /home/user/esp/esp-idf-v3.3-beta3    |
        +------+--------------------------------------+
        ```


        ```
        $ espy idf get -n idf1

        +------+--------------------------------------+
        | name | filepath                             |
        +------+--------------------------------------+
        | idf1 | /home/user/esp/esp-idf               |
        +------+--------------------------------------+
        ```

    * Modify a specific IDF
        ```
        $ espy idf mod -n idf1

        +------+--------------------------------------+
        | name | filepath                             |
        +------+--------------------------------------+
        | idf1 | /home/user/esp/esp-idf-v3.3-beta3    |
        +------+--------------------------------------+
        Enter the new name for the IDF: default

        Change the path of the IDF? [y/N]: y
        Enter the new path for the IDF: /home/user/esp/esp-idf

        Note: If this IDF has been used in an app, modify them if needed.
        Continue to modify IDF? [y/N]: y
        Succesfully modified the IDF
        ```

    * Delete all or specific IDF(s)
        ```
        $ espy idf del

        Delete all IDFs? [y/N]: y
        Successfully deleted required IDF(s)
        ```

        ```
        $ espy idf del -n idf1

        Delete IDF: idf1 [y/N]: y
        Successfully deleted required IDF(s)
        ```

2. Managing apps
   * Create a new app
      ```
      $ espy app new -n hello_world -idf idf1
      Project created!
      
      $ tree hello_world/
      hello_world/
      ├── CMakelists.txt
      ├── main
      │   ├── CMakelists.txt
      │   ├── component.mk
      │   └── main.c
      └── Makefile

      1 directory, 5 files
      ```
      
