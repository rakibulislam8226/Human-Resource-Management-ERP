## Human-Resource-Management-ERP

* python 3.10

**First clone the repo;**

```shell
 git clone git@github.com:rakibulislam8226/Human-Resource-Management-ERP.git
```

---
**Create virtual environment based on your operating system**
 * **For ubuntu**
 ```shell
python -m venv venv
  ```

  ###### Activate the virtual environment
 ```shell
source venv/bin/activate
  ```
 * **For windows**
 ```shell
python -m venv venv
  ```

  ###### Activate the virtual environment
 ```shell
venv\Scripts\activate
  ```
---

**Install the requirements.txt file**
 ```shell
pip3 install -r requirements.txt
  ```
  * If needed then upgrade pip version. (Optional)
    ```shell
    pip install --upgrade pip
    ```
---
* Go to src directory
    ```shell
    cd src
    ```

---
**Copy .env.example file to .env:**

  * For linux
    ```shell
    cp .env.example .env
    ```
  * For windows
    ```shell
    copy .env.example .env
    ```
  ###### Create Mysql database and set up in .env and fill up other necessary fields with proper credentials.

---

**Migrate all the fields**
 ```shell
python manage.py migrate
  ```

**Create superuser**
 ```shell
python manage.py createsuperuser
  ```

**Run the server**
 ```shell
python manage.py runserver
  ```

---

### Connect redis server
TODO:
