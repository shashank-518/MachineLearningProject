import sys
import logging


logging.basicConfig(
    filename="error.log",        # log file name
    level=logging.INFO,          # log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))


class CustomException(Exception):
    def __init__(self,error_message,error_details):
        super().__init__(error_message)
        self.error_message= error_message_detail(error=error_message,error_detail=error_details)
    
    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a= 1/0
    except Exception as e:
        logging.info("Exception raised by zero")
        raise CustomException(e , sys)