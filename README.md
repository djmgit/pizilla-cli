# Pizilla-cli

**pizilla-cli** is a terminal based download client for Pizilla webapp.
It allows users to view list of files currently present on pizilla, download
all the files or downlaod given specific files by their names.

## Usage

Pizilla-cli has been developed using python.
Inorder to use **pizilla-cli** do the following.

* First download or clone this repository using ```git clone https://github.com/djmgit/pizilla-cli.git```
* Next install dependencies using ```pip install -r requirements.txt```

Now you are ready to use the script. Open the directory containing the script in terminal.

Inorder to know about the various options use ```python pizilla.py -h```

For viewing a list of files currently present on pizilla use ```python pizilla -l```

For downloading all the files use ```python pizilla -a```

For downloading specific files use ```python pizilla -f "[fie_name1] [file_name2] [file_name3] ..."```

When specifying individual file names, put the list of files under **quotes** and two file names
should be delimited by **space**
