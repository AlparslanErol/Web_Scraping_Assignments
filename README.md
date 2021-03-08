## Assignment Submission Repository

This repository is used to assignment submission of Web Scraping and Social Media Scraping course under 2nd semester curriculum of 
``Data Science and Business Analaytics Master's degree program`` in ``University of Warsaw``.

### Folder ```01```
This folder is only created for first class and you can simply find student information of mine in `id.txt` file.
> Alparslan Erol \
> 428681

### Folder ``02``
In this folder, you can find the first assignment of the course which is ``Exercises in HTML parsing`` and my solutions.
There are 2 main exercise in this assignment,
1.  **Totally Normal Gifts - Easy**\
In this task ``pythonscraping.com``: http://www.pythonscraping.com/pages/page3.html page is used to scrap data. You can find the exact
definitions of tasks:
    - Extract **bolded** parts of the text.
    - Extract the last **Item Title** from the table.
    - Extract the **footer** of the webpage.
    
2.  **Pawel Domagala - Medium**\
In this task ``Wikipedia.org``: https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a page is used to scrap data. You can find the exact
definitions of tasks:
    - Extract Pawel's **date of birth**.
    - Extract Pawel's **three occupations**.
    - Extract the list of **references**.
    
> **Deadline:** 07.03.2021, 23:59

> ``Python 3.9.0`` was used to develop these piece of codes.\
> You can find the required python packages and their versions in ``02/requirements.txt`` file.\
> Thanks to ``Makefile``, you can create a virtual environment, install required packeges and delete virtual environment.
> If you do not want to use virtual environment, then you need to install required packages in your base python interpreter.
> * make ``venv`` creates python virtual environment.
> * make ``require`` install required packages.
> * make ``clean`` delete venv file.

You can simply run the code like as follows from command line:
```console
**LINUX**
...@...:project_root$ make venv
...@...:project_root$ make require
...@...:project_root$ python3 ex_1.py
...@...:project_root$ python3 ex_2.py

**WINDOWS**
project_root> make venv
project_root> make require
project_root> python ex_1.py
project_root> python ex_2.py
```

### Submissions to the course Web Scraping and Social Media Scraping

* Submissions deadline of weekly assignments is always Sunday, 23:59. 

* For every week create new folder ("01", "02", "03",...) and post your files there.

* In the folder "01" add "id.txt" file containing your Full Name and your Student ID.

* After the last class create "project" folder. In this folder include "project.txt" file, which contains github link to your project, and names and ID's of all group members.
