![Apache Log Analyzer Banner](A_banner_with_the_title_"Apache_Log_Analyzer"_is_d.png)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Platform](https://img.shields.io/badge/Platform-Kali%20%7C%20Ubuntu-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-success)

## 🕵️ Apache Log File Analyzer

A Python script that analyzes Apache access.log files to extract useful insights such as:
- Most frequent IP addresses
- Most requested URLs
- Status code breakdown
- User agent summary

## 🔧 How It Works
The script reads Apache access logs and uses regular expressions to extract data. It then counts and displays:
- Top IPs
- Top requested URLs
- Most common HTTP status codes
- Most used user agents

## 📂 Files
- apache_analyzer.py: The main log analyzer script.
- access.log: Sample Apache access log file.
- README.md: This file you're reading now.

## 🚀 Usage

1. Clone the repo or download the files:
   ```bash
   git clone https://github.com/Reinhard1268/apache_log_analyzer.git
   cd apache_log_analyzer

2.  Run the analyzer:
python3 apache2_analyzer.py access.log

3. View the summary output directly in your terminal
--- Apache Log Analysis ---
Total requests: 10000

## 💻Example Output
Top 5 IP addresses:
66.249.73.135: 482 requests
46.105.14.53: 364 requests
130.237.218.86: 357 requests
75.97.9.59: 273 requests
50.16.19.13: 113 requests

Requests per day:
17/May/2015: 1632 requests
18/May/2015: 2893 requests
19/May/2015: 2896 requests
20/May/2015: 2579 requests

404 Not Found URLs:
/doc/index.html?org/elasticsearch/action/search/SearchResponse.html                                                                                                                          
/files/logstash/logstash-1.3.2-monolithic.jar                                                                                                                                                
/presentations/logstash-puppetconf-2012/images/office-space-printer-beat-down-gif.gif                                                                                                        
/presentations/logstash-puppetconf-2012/images/office-space-printer-beat-down-gif.gif                                                                                                        
/files/logstash/logstash-1.3.2-monolithic.jar                                                                                                                                                
/wp-login.php                                                                                                                                                                                
/administrator/index.php                                                                                                                                                                     
/files/logstash/logstash-1.3.2-monolithic.jar                                                                                                                                                
/files/logstash/logstash-1.3.2-monolithic.jar                                                                                                                                                
/presentations/logstash-puppetconf-2012/images/office-space-printer-beat-down-gif.gif                                                                                                        
                                                                                       

## 🧠 Learnings
-  Working with Apache log formats
-  Regez parsing in Python
-  Counting frequency with collections.Counter
-  Reading large text files efficiently

## 🛡️ License
 
   MIT License

Built 💻 by Reinhard1268
