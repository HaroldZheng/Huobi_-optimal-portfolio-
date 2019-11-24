# Huobi_-optimal-portfolio-
To create an optimal portfolio using free historical data from the Houbi Derivatives Market RESTful API. 
### Files in the folder
- `data/` 
  - `data.py`: get data from huobi
  - `HuobiDMService.py`
  - `HuobiDMUtil.py`
  - `BTC_CQ.csv`:current quarterly data of BTC
  - `XRP_CQ.csv`:current quarterly data of XRP
  - `LTC_CQ.csv`:current quarterly data of LTC
- `Main.py`

### Required packages
The code has been tested running under Python 3.7.4, with the following packages installed (along with their dependencies):
- pandas == 0.25.1
- numpy == 1.16.5
- matplotlib == 3.1.0
- urllib3 == 1.24.2
### Running the code
#### Get data
```
$ cd data
$ python data.py (get BTC,XRP,LTC... .csv)
```
 
#### optimal portfolio
```
$ python main.py 
```
