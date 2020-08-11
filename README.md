# Upload your sliced .gcode file to multiple octopriont instances

<p align="center">
  <img src="https://i.ibb.co/THxgn6P/instance.png" />
</p>

This project provides python code for simplify 3d automatic .gcode file upload to multiple printers that use octoprint and raspberry pi. Click save toolpaths to disk, save file to temp dir, dialog will pop up with configured printers and after selecting one, hit button send and file will be uploaded to selected printer

# Todo's

  - checkbox for "Print after upload"
  - checkbox for "Select File after upload"

# Setup

    1. Download python code
    2. Configure printers in myPrinters dictionary
    3. place this script somewhere safe
    4. Add it to scripts in simplify3d
    
**Configuring printers in list**

![Config image](https://i.ibb.co/g6hhk5N/config.png)

You can read how to obtain API key here: https://docs.octoprint.org/en/master/api/general.html#authorization


**Add script to your Simplify3D scripts tab**
![simplify3d](https://i.ibb.co/0DPkJC5/simplify.png)
