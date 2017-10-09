Arduino IDE Ansible role
========================

Installs the Arduino IDE for developing on Arduino.
A brief description of the role goes here.

Requirements
------------

Assumes Debian Linux, but not a strict requirement.

Role Variables
--------------


```yaml
# Version of Arduino IDE to install, will be interpolated in download URLs.
arduino_version: "1.8.5"

# URLs for fetching the source files from remote.
arduino_ide_url: "https://downloads.arduino.cc/arduino-{{ arduino_version }}-linux64.tar.xz"
arduino_ide_checksums_url: "https://downloads.arduino.cc/arduino-{{ arduino_version }}.sha512sum.txt"

# Location for saving and extracting Arduino archives.
arduino_download_directory: /opt/arduino

# Communications port for interfacing with the Arduino board. Toolkit defaults
# to serial port COM1, but USB is a saner default.
arduino_port: /dev/ttyUSB0
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: workstations
  roles:
    - role: conorsch.arduino
      arduino_version: "1.8.5"
```

License
-------

MIT
