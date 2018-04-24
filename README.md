<center><img src='/assets/kogu.gif' width='100' alt='Kogu Logo' aria-label='kogu.ai' /></center>

# Five minute guide
With Kogu's help you can keep track and monitor your experiments. This guide will show you how to install kogu and log your first experiment.

# Getting Kogu

Kogu has platform installers for Windows, macOS and Ubuntu Linux, as well as plain binary archives. All the downloads are available at our [install location](https://github.com/kogu-io/kogu/releases). 

Alternatively you can use Homebrew to install Kogu on macOS.
```cli
$ brew tap kogu-io/kogu
$ brew install kogu
```

# Kogu components

There are three main components of Kogu:
* Local server to handle requests and store all the data,
* Command line interface to run and manage your experiments,
* Web interface to explore and analyze all your experiment details.

# Running your experiments
Now that we've got Kogu installed, let's start up the server with:
```cli
$ kogu-server
```
This starts a local server that manages and displays all the experiments and serves them at `localhost:8193`
Open up a new terminal tab and let's run a simple script to see that everything is working: create a file called `hello.py` and make it print to standard output:
```python
print("Hello kogu.")
```

Now instead of running your scripts with the `$ python hello.py` you run:
```cli
$ kogu run hello.py
```

This logs the experiment. You can check it in the log out by calling:
```cli
$ kogu list
```

Now open the web interface at `http://localhost:8193` and click on the experiment id that you just created. This shows you the details about the experiment including the standard output that was printed out via the script.

---

These are just a few things you can do with kogu. To learn more – follow the rest of the docs. For example if you are running your experiments with different [parameters](cli.md) – kogu can help you log and keep track of them. Or check out how you can easily plot real-time graphs or upload results with Kogu using [Python library](python-library.md).

#### Feedback
Please send us feedback at [hello@kogu.io](mailto:hello@kogu.io) or create an issue on [GitHub](https://github.com/kogu-io/kogu/issues).
