@echo off
:en
tasklist |find "scrapy.exe"|| ( cd D:\mypy\kickstarter\kickstarter\ && scrapy crawl reward_spider )
echo "sleep for 3 minutes before next cralwer starts..."
ping -n 180 127.0.0.1>nul
goto en