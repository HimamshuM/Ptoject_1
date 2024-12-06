import os 
import sys
import logging

logging_str = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"

#This defines the directory where log files will be stored. Here,
# it is simply named "logs" and is expected to be in the current working directory.
log_dir = "logs"

"""This creates the full path for the log file named "logging.log" inside the "logs" directory.
The os.path.join() function is used to ensure compatibility across operating systems (Windows, Linux, macOS),
 as different systems use different path separators (\ for Windows and / for others)."""

log_filepath = os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True) # With exist_ok=True, the function essentially acts as a "create if not exists" operation.

logging.basicConfig(
    level= logging.INFO,
    format = logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("datasciencelogger")