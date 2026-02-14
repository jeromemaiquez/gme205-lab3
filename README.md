# Project Title
GmE 205 - Laboratory Exercise 3

# How to set up the virtual environment
1. Create a folder on your computer and open it in your IDE (e.g., VS Code)
2. Open the terminal then create the virtual environment by running the following:
    ```
    py -m venv .venv
    .\.venv\Scripts\activate
    ```
3. Press ```Ctrl + Shift + P``` in VS Code, search for *Python: Select Interpreter*, then choose the interpreter inside the ```.venv``` folder
4. Install the required packages by running the following in the terminal:
    ```
    python -m pip install --upgrade pip
    pip install pandas matplotlib
    ```
5. (Recommended) List the installed packages via:
    ```
    pip freeze > requirements.txt
    ```

# How to run Python scripts

In the terminal, ensuring that ```(.venv)``` is present in the prompt, run the following:
    ```
    python <folder/script_name.py>
    ```

# Reflection - Part B.5

Internally, the Point `lat` and `lon` attributes were now represented as the `y` and `x` attributes of the `shapely.Point` class. However, externally, these coordinates are still easily accessible, albeit with slightly different syntax: `Point.geometry.x` instead of `Point.lat`. Since the representation of the geometry is now delegated to Shapely, this library can now handle most spatial computation applicable to point objects.