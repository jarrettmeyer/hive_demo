LOAD DATA INPATH '/user/vagrant/weather_part/weather_ext_2000_1.txt' INTO TABLE weather_part PARTITION(year=2000, month=1);
LOAD DATA INPATH '/user/vagrant/weather_part/weather_ext_2000_2.txt' INTO TABLE weather_part PARTITION(year=2000, month=2);
