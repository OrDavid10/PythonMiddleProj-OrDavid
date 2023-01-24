from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()
def write_to_log(str):
    """
    :name :Or
    :date : 22/01/2023
    function that appends the exceptions to a log file
    :param str: string to write to the log
    :return:
    """
    f = open(os.getenv('LOG_FILE'), 'a')
    f.write(f"\n{str} , {datetime.now()}")
    f.close()



