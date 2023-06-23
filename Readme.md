# Deribit Client and a custom API

### Overview
The app provides a client to make requests to [Deribit API](https://docs.deribit.com/) and save the recieved responses into a database. Moreover there is a custom API that reads from the same database and provides three routes.
1. **/currency-all-info**: provides all the historical data of a specific currency that exist in the database. The name of the currency is passed to the route under the parameter 'ticker_name'. 
2. **/currency-price**: provides the price of a specific currency. The name of the currency is passed to the route under the parameter 'ticker_name'. 
3. **/currency-by-date**: provides all the historical data of a specific currency on a specific date. The name of the currency is passed to the route under the parameter 'ticker_name' and the date is passed under the parameter 'dt', the format of the date argument ***must*** be `%Y-%m-%d`.    
  
The last component of the app is a CLI that provides three main commands.
1. **createdb**: creates a database at the very first time starting the app, otherwise it returns that there is a database exists.
2. **call_deribit**: Starts a scheduler that sends requests to Deribit API every minute.
3. **run_api**: Starts the custom API app.
---
### Installation
1. Clone the repo.
2. Install the dependencies     
```Python
pip install -r requirements.txt
```
3. Fill in the database credentials in the `.env` file.
---
### Usage
The following commands should be run at the root of the app.
1. Create a database by running **createdb** command from the command line as follows:
```Python
python main_cli.py createdb
```
2. Populate the database with data from Deribit API, by running
```Python
python main_cli.py call-deribit
```
3. Run the custom API by using
```Python
python main_cli.py run-api
```