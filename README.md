# streaming-05-smart-smoker

Before you Begin:

Fork this starter repo into your GitHub.

Clone your repo down to your machine.

View / Command Palette - then Python: Select Interpreter

Select your conda environment.

Make sure to import pike or copy the file from a previous module

Task 1. Create a Place to Work

In GitHub, create a new repo for your project - name it streaming-05-smart-smoker.

Add a README.md during the creation process. (If not, you can always add it later.)

Clone your repo down to your machine.

In VS Code, add a .gitignore (use one from an earlier module), start working on the README.md. Create it if you didn't earlier.

Add the csv data file to your repo.

Create a file for your bbq producer.

Task 2. Design and Implement Your Producer

Here's how the code works:

Imports: The script imports necessary libraries such as csv, pika (RabbitMQ client library), sys, webbrowser, and traceback.

Logger Setup: The script initializes logging using a custom function setup_logger from util_logger module. This helps in logging errors and other information for debugging purposes.

RabbitMQ Admin Site: The function offer_rabbitmq_admin_site() prompts the user to open the RabbitMQ Admin website. If the user chooses to do so, it opens the web browser to the RabbitMQ Admin site.

Main Work: The main_work() function is the core of the script. It performs the following tasks:

Establishes a connection to the RabbitMQ server running on localhost.
Deletes any existing queues named "01-smoker", "02-food-A", and "02-food-B" and then declares new queues with these names.
Processes a CSV file containing smoker temperature data.
For each row in the CSV file, it extracts the timestamp, smoker temperature, food A temperature, and food B temperature.
If the smoker temperature is available (not empty), it converts it to a float and sends a message to the "01-smoker" queue.
Similarly, if food A or food B temperatures are available, it converts them to float and sends messages to the respective queues.
If any errors occur during these operations, they are caught and logged with detailed traceback information.

<img width="1911" alt="Screenshot 2024-06-07 at 1 11 20 PM" src="https://github.com/akandola47/streaming-05-smart-smoker/assets/143216836/caf79fea-b2d6-4282-8442-67c4332ac114">

Send Message: The send_message() function is responsible for publishing a message to the specified RabbitMQ queue. It takes parameters channel, queue_name, and message, where channel is the communication channel to RabbitMQ, queue_name is the name of the queue to publish the message to, and message is the content of the message to be sent.

Main Block: Finally, in the main block, the script offers to open the RabbitMQ Admin site and then calls the main_work() function to perform the necessary tasks.
