# AirBnB clone - RESTful API

Creation of a RestAPI in Python with Flask

to run the program:

```bash

HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd \
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db \
HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
```

---

NOTES:

1. When someone says, “REST service,” “REST API” or “RESTful API” they more-than-likely mean an HTTP or Web-based server that accepts requests over HTTP and responds in human-readable JSON.

2. - REST == "REpresentational State Transfer"
   - Resource-based Representations

     Six Contraints:

   **- Uniform interface:**

   > The method of communication between a client and a server must be uniform.

   **- Stateless:**

   > Statelessness means that every HTTP request happens in complete isolation. When the client makes an HTTP request, it includes all information necessary for the server to fulfill the request.

   **- Client-server:**

   > The server doesn’t know who is talking to it. Clients are not concerned with data storage => the portability of client code is improved. Servers are not concerned with the user interface or user state so that servers can be simpler and more scalable

   **- Cacheable:**

   > storing the server response in the client itself, so that a client need not make a server request for the same resource again and again.

   **- Layered system**

   > REST allows you to use a layered system architecture where you deploy the APIs on server A, and store data on server B and authenticate requests in Server C, for example. A client cannot ordinarily tell whether it is connected directly to the end server or an intermediary along the way.

   **- Code on demand**

3. CORS, which stands for “Cross-Origin Resource Sharing,” is a security standard that enables servers to indicate the origins from which browsers are allowed to request resources. It was created to refine the same-origin policy (SOP), which browsers use to prevent malicious applications from accessing sensitive data on domains they do not control.

---

**RESOURCES**:

- https://www.restapitutorial.com/introduction
- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/301/flask_cheatsheet.pdf
