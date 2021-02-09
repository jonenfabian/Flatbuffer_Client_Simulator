# Flatbuffer_Client_Simulator

1. To run the client install [Python](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe) (Version 3.7)
> while walking through the install wizard make sure to enable PATH
![activate PATH](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png)

2. start the server that will receive the data from the client. Make sure you listen to Port 8089 on your localhost
> If you don't have a server, open CMD, cd into ```samples``` and run ``` python flatbuffer_server.py ```

3. execute the client: open another CMD, cd into ```samples``` and run ``` python flatbuffer_test_client.py ```. The Client sends data to the Port 8089.

Note: The flatbuffer schema is [buttons_schema_test_v2.fbs](samples/buttons_schema_test_v2.fbs)

Compile it using the [Tutorial](https://google.github.io/flatbuffers/flatbuffers_guide_tutorial.html) 
