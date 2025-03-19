# Photo Info Extractor

Easily see the secret details of your photos!

## What It Does

* Simple photo uploading.
* Shows you photo info like date, location (if any), and camera type.
* Gives you a Google Maps link if your photo has location data.

## What You Need

* **Front (The Look):**
    * HTML
    * CSS
    * JavaScript
* **Back (The Brains):**
    * Python 3.x
    * Flask
    * Pillow (for handling photos)
    * pymongo (for saving data)
* **Database:**
    * MongoDB

## Project Setup

* `front/`: All the website files (`index.html`, `style.css`, `script.js`).
* `back/`: All the Python code (`app.py`, `database_handler.py`, `exif_extractor.py`).
* `back/images/`: Where your uploaded photos go.

## How to Run It

1.  **Download the project:**

    ```bash
    git clone <your_project_link>
    ```

2.  **Go inside the project folder:**

    ```bash
    cd image-exif-extractor
    ```

3.  **Install the Python stuff:**

    ```bash
    pip install Flask Pillow pymongo
    ```

4.  **Make sure MongoDB is running.**
5.  **Start the back part:**

    ```bash
    python back/app.py
    ```

6.  **Open `front/index.html` in your web browser.**

## Quick Tweaks

* **MongoDB Link:** Change the MongoDB link in `back/app.py` and `back/database_handler.py`.
* **Server Address:** Update the server IP and port in `front/script.js` to match your server.

## Wanna Help?

1.  Fork this project.
2.  Make your changes in a new branch.
3.  Save your changes.
4.  Send them back to us.

## License

This project is under the MIT License.

## Get in Touch

[jafaryaz220@gmail.com](mailto:jafaryaz220@gmail.com)
