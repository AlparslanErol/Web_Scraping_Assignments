## Assignment Submission Repository

This repository is used to assignment submission of Web Scraping and Social Media Scraping course under 2nd semester curriculum of 
``Data Science and Business Analaytics Master's degree program`` in ``University of Warsaw``.

### Folder ```01```
This folder is only created for first class and you can simply find student information of mine in `id.txt` file.
> Alparslan Erol \
> 428681

### Folder ``02``
In this folder, you can find the first assignment of the course which is ``Exercises in HTML parsing`` and my solutions.
There are 2 main exercises in this assignment,
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

### Folder ``03``
In this folder, you can find the second assignment of the course which is ``Exercises in regular and lambda expressions``
and my solutions.\
There are 2 main exercises in this assignment,
1.  **War and Peace - Easy**\
In this task ``pythonscraping.com``: http://www.pythonscraping.com/pages/warandpeace.html page is used to scrap data. You can find the exact
definitions of tasks:
    - Using ``lambda expressions`` print out how many times a tag consisting of a string ``Anna Pavlovna`` appears in the text.
    - Using ``lambda expressions`` enlist **tags with exactly one attribute**. Also, print out the length of this list.
    
2.  **Flags - Medium**\
In this task ``Wikipedia.org``: https://en.wikipedia.org/wiki/United_Nations_Development_Programme page is used to scrap data. You can find the exact
definitions of tasks:
    - Using ``regex`` extract all of the **flags' image paths**.
    
> **Deadline:** 17.03.2021

### Folder ``04``
In this folder, you can find the third assignment of the course which is ``Exercises in scraping single static page``
and my solutions.\
There are 1 main exercises in this assignment with 3 sub points,
1.  **Musicians**\
In this task ``Wikipedia.org``: 
-   https://en.wikipedia.org/wiki/Lists_of_musicians
-   https://en.wikipedia.org/wiki/List_of_rock_music_performers
-   https://en.wikipedia.org/wiki/Queen_(band)

pages are used to scrap data.

You can find the exact definitions of points:
- From the page ``first`` linked above extract links to web pages containing information about ``musicians specialising in music
 genre beginning with "R"``. 
- From the page ``second`` linked above extract links to web pages containing information about ``musicians whose name begin with "Q"``.
- From the page ``third`` linked above extract extract: the ``name of the band``, ``the genre``, ``number of years active``.
    
> **Deadline:** 21.03.2021 - 23:59

### Folder ``05``
In this folder, you can find the fourth assignment of the course which is ``Exercises in scraping multiple static pages``
and my solutions.\
There are 1 main exercises in this assignment with 4 sub points,
1.  **Musicians**\
In this task ``Wikipedia.org``: 
-   https://en.wikipedia.org/wiki/Lists_of_musicians is used to scrap data.

You can find the exact definitions of points:
- Extract links to web pages containing information about ``musicians specialising in music genre beginning with "A"``.
- Extract links to artists' web pages for the first of the links from the previous step.
- From artist's pages extract: ``name of the band``, ``years active``.
- As an output use ``default print function on pandas data frame``.

This script is scrap the data if and only if ``name`` and ``year_active`` features have value(not None valued) in the 
website.

> In the python script there is a function ``scraper`` to  scrap data from links in musician genre links.\
> You can use argument ``scrap_all`` to decide if you want to scrap all data in this links or only the first links in
> music genre links. This argument is ``False`` as default. But if you want to scrap all data, simply update this as ``True``.
    
> **Deadline:** 28.03.2021 - 23:59

### Folder ``06``
In this folder, you can find the fifth assignment of the course which is ``Exercises in static scraping using Scrapy``
and my solutions.\
There are 1 main exercises in this assignment with 4 sub points,
1.  **Musicians**\
In this task ``Wikipedia.org``: 
-   https://en.wikipedia.org/wiki/Lists_of_musicians is used to scrap data.

You can find the exact definitions of points:
- Extract links to web pages containing information about ``musicians specialising in music genre beginning with "A"``.
- Extract links to artists' web pages for the first of the links from the previous step.
- From artist's pages extract: ``name of the band``, ``years active``.
- As an output use ``default print function on pandas data frame``.

This script is scrap the data if and only if ``name`` and ``year_active`` features have value(not None valued) in the 
website.

After you create a project template for Scrapy, you can put those python scripts inside your spider folder. After that
you are ready to scrape data from the allowed domain. To do this, go your Scraper project root folder and run:
```shell script
# If you want to write output of the scraper in a .csv file
scrapy crawl link_lists -o link_lists.csv
scrapy crawl links -o links.csv
scrapy crawl musicians -o musicians.csv
``` 
> **Deadline:** 11.04.2021 - 23:59

### Folder ``07``
In this folder, you can find the sixth assignment of the course which is ``Exercises in HTML parsing``
and my solution.\
There are 1 main exercise in this assignment with 4 sub points,
1.  **Selenium Bot**\
In this task ``campuswire.com`` is used to scrap data.

You can find the exact definitions of points:
- Write a ``selenium``bot, that will log into a Campuswire account, and will send itself (its .py file, not it's code) 
to your tutor.

> Here is the process of selenium bot:
> - Connect to campuswire.com.
> - Take e-mail and password as an input of login process and login the user account.
> - Search the name of tutor from the people list.
> - Send messages to tutor about the homework and upload homework file as ```.py``` file.

> **Deadline:** 18.04.2021 - 23:59


### Virtual Environment with Project Requirements
> ``Python 3.9.0`` was used to develop for the homework assignments.\
> You can find the required python packages and their versions in ``requirements.txt`` file.\
> Thanks to ``Makefile``, you can create a virtual environment, install required packages and delete virtual environment.
> If you do not want to use virtual environment, then you need to install required packages in your base python interpreter.
> * make ``venv`` creates python virtual environment.
> * make ``require`` install required packages.
> * make ``clean`` delete venv file.

You can simply run the code like as follows from command line:
```console
**LINUX**
## For linux, you need to update the makefile commands compatible for linux environment.
...@...:project_root$ make venv
...@...:project_root$ make require
...@...:project_root$ python3 .\02\ex_1.py
...@...:project_root$ python3 .\02\ex_2.py

**WINDOWS**
project_root> make venv
project_root> make require
project_root> python .\02\ex_1.py
project_root> python .\02\ex_2.py
```
If you face problem about creating virtual environment from makefile, you can create virtual environment manually and
install packages from ``requirements.txt`` file.

### Submissions to the course Web Scraping and Social Media Scraping

* Submissions deadline of weekly assignments is always Sunday, 23:59. 

* For every week create new folder ("01", "02", "03",...) and post your files there.

* In the folder "01" add "id.txt" file containing your Full Name and your Student ID.

* After the last class create "project" folder. In this folder include "project.txt" file, which contains github link to your project, and names and ID's of all group members.
