# How to Install Jupyter in Windows

Jupyter Notebook is a popular open-source web application used for interactive data science and scientific computing. However, there are instances where you might encounter an error where "jupyter" is not recognized as an internal or external command, operable program or batch file. This can happen if you haven't installed the Jupyter module or if the path to Python and pip isn't added to your user's PATH environment variable. This guide will take you through the steps to install Jupyter in your Windows machine.

## Step 1: Install Jupyter Module

To install the Jupyter module, open your Command Prompt shell and run either one of these commands:

```
pip install jupyter
python -m pip install jupyter
py -m pip install jupyter
python3 -m pip install jupyter
```

If you encounter a permissions error, run this command instead:

```
pip install jupyter --user
```

You can also install Jupyter Lab by running this command:

```
pip install jupyterlab
```

## Step 2: Run the Notebook

After you have installed the Jupyter module, try to run the notebook with any of these commands:

```
jupyter notebook or jupyter-notebook
python -m notebook
py -m notebook
python -m jupyterlab
py -m jupyter lab
```

Note that the `python -m notebook` command should work even if you don't have the path to pip in your PATH environment variable.

## Step 3: Verify Installation

You can verify that the Jupyter module is installed by using the `pip show jupyter` command. If the package is not installed, run the installation command again. If the installation still fails, try running CMD as an administrator.

## Step 4: Add Python and pip to PATH

If you encounter the "not recognized as an internal or external command" error even after installing the Jupyter module, you will need to add the path to Python and pip to your user's PATH environment variable. Here's how:

1. Click on the search bar and type "environment variables".
2. Click on "Edit the system environment variables".
3. Click on the "Environment Variables" button.
4. In the "User variables for YOUR_USER" section, select the "Path" variable and click "Edit".
5. Click on "New" and then click "Browse".
6. Use the command `python -c "import os, sys; print(os.path.dirname(sys.executable))"` to find where your Python installation is located.

```
C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python310\Scripts
C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python310\
```

7. Add the path to Python and the path to the "**Scripts**" directory located in your Python3X folder. This is where the executable files are located, including pip.exe and jupyter.exe.
8. Close your Command Prompt application and then reopen it.
9. Try to run the jupyter notebook command again.

## Conclusion

By following these steps, you should now be able to install and run Jupyter with ease on your Windows machine. If you encounter any errors, try the additional resources provided or consult the official Jupyter documentation.
