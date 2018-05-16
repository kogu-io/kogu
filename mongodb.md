# Running Kogu with MongoDB storage backend

It is possible to use [MongoDB](https://www.mongodb.com/) as an alternative storage backend for your experiment data. MongoDB backend is used to store both experiment metadata and also attachments uploaded to Kogu server. 

In order to do that define ```KOGU_DB``` environment variable for ```kogu-server``` with [MongoDB connection string](https://docs.mongodb.com/manual/reference/connection-string/) as a value.

Assuming that you are running MongoDB instance in your localhost with defaults you can use:

```bash
$ export KOGU_DB=localhost
```
You may want to define this parameter in your environment to ensure that it stays active after system reboot.

**Note** that the information previously stored to Kogu default database is not uploaded to the MongoDB!

## Connecting several Kogu servers to one MongoDB database
In principle this is shold work however there are limitations.
All experiments would be visible and fully accessible (this includes deletion) in all Kogu servers. It is not possible to easily understand which Kogu server created the experiment. New experiments created from other server instances would appear in web-browser only after page reload. Data for these experiments will not be updated in real time. 

### Using custom name for Kogu database
The default name for Kogu database is "kogu". It is possible to override the database name with environment variable ```KOGU_DB_NAME```

```bash
$ export KOGU_DB_NAME=kogu-my-computer
```
This, for example, allows to store several independent Kogu databases on a single MongoDB instance. 