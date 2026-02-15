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

# Reflection - Part C.6

- `SpatialObject` is an abstraction of any real-world object with a geometric representation, whether it be points (e.g., POIs, sensors), polygons (e.g., parcels, buildings), or lines (e.g., roads, pipelines). It represents the fact that most spatial entities share a geometry, a corresponding bounding box, and their own spatial relationships with other entities.

- Inheritance allows a child class to inherit the state and behaviors of its parent class, without having to rewrite all of these for the child class. This saves time in code duplication and limits the risk of human error in retyping, and makes debugging and refactoring easier.

- The choice to store parcel attributes in a dictionary is a structural decision (rather than a behavioral one) because, from the external POV of the user, there is barely any difference in using a dictionary vs. storing the attributes as primitives (aside from a minor syntax change). A dictionary gives more "structure" to the attributes, where they can be stored inside of a Python iterable object that is easily understandable and reasoned about. Nonetheless, it is still very easy to extract specific attributes.

- If a new method is added in SpatialObject, this method will then be made available to all subclasses as well. This is the effect of inheritance: child classes effectively "inherit" the traits (i.e., attributes and behavior) of its parent class, without having to duplicate code.

- The hierarchical design of harnessing inheritance allows the programmer to add more and more subclass in the future, without having to duplicate much of the basic geometric logic (i.e., the logic we wish to assign to SpatialObject). This allows the code to scale better: the logic still flows clearly even with many more classes added. Without this, the programmer would have to repeat dozens to hundreds of code lines just for the same exact attribute/behavior to be added to each new class created in the code. 

# Reflection - Challenge Exercises

1. This shows the principle of _responsibility_: `from_dict()`'s responsibility is simply to parse an input dictionary for use in constructing a Point object. The responsibility to validate the `lon` and `lat` values remains with the Point `__init__()` method.

2. Because `as_dict()` is being modeled as a behavior of the object (`Point` or `Parcel`). This allows clearer logic and cleaner code. Instead of implementing this logic on its own in `demo.py` or `run_lab3.py`, we can instead bundle it inside the spatial classes we created.

3. It is better for `as_dict()` to return primitive data types, particulary for its `lon` and `lat` attributes (with the `float` data type). If a Shapely geometry object was returned instead, the terminal would simply display `<shapely.geometry ...>`, which only indicates the _existence_ of an object and is thus not legible for a human user.

4. This is because we have chosen to model `intersects()` as a behavior of spatial objects in general, and not specific to any particular class of spatial objects. In GIS, any sort of geometry can have an intersecting spatial relationship, whether it be points, lines, or polygons. Thus, it follows that any spatial entity modeled to have any of these geometry types must also have the ability to have this spatial relationship.

5. A new subclass (i.e. `Building`) would only have to be constructed to be a child class of `SpatiaObject` (i.e., `class Building(SpatialObject):`) for it to support the `intersects()` method. No changes (for now) are required to the method itself, because this is exactly the power of inheritance: as a method of the base class `SpatialObject`, `intersects()` is automatically inherited by any future subclass.