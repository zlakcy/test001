import sys

sys.path.insert(0,"C:\\pycharm\\Automation_project")
project_file=sys.path[0]

url="http://iwebsns.pansaifei.com/index.php"
driver_path=project_file+r'\driver\chromedriver.exe'
datafile_path=project_file+r'\data\testdata.xlsx'
case_path=project_file+r'\testcases'
report_path=project_file+r'\result\report'
log_path=project_file+r'\log\log.txt'