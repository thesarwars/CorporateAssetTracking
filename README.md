# Corporate Asste Tracking App

A Django app to track corporate assets such as phones, tablets, laptops 
and other gears handed out to employees.

# Goals:
1. The application might be used by several companies
2. Each company might add all or some of its employees
3. Each company and its staff might delegate one or more devices to employees for a certain period of time
4. Each company should be able to see when a Device was checked out and returned
5. Each device should have a log of what condition it was handed out and returned

# Instruction to Run the project:

1. Create the virtual environment by command 'pyhton -m venv tenv'
2. Activate the 'tenv'. Command is for Mac 'source tenv/bin/activate' & for Windows PC 'tenv\Scripts\activate'. You can also use 'pipenv shell'.
3. Install Django and it's dependencies using pip commands. "pip install -r requirements.txt"
4. After that migrate the database using command "python manage.py migrate"
5. Then run the project by command "python manage.py runserver"

Bingo...!!!

# Image Sample of POSTMAN

![Asset Tracking](/AssetTrack.png)

![Employee](/Employee.png)


# API Documentation URl (POSTMAN):
https://documenter.getpostman.com/view/28624290/2s9YC2zDgR