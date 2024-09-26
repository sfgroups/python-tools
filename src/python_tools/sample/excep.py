import logging
import traceback

# Configure the logger
logging.basicConfig(
    # filename='app.log',  # Log to a file
    level=logging.ERROR,  # Set the logging level to ERROR or higher
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Log format
)

logger = logging.getLogger(__name__)

def function_that_might_fail():
    try:
        # Code that might raise an exception
        result = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        # Log the stack trace with logging.exception()
        logger.exception("An error occurred: %s", e)
        # Optionally, if you need to do something else with the exception
        # traceback.print_exc() # Prints the stack trace to stdout
        raise e

if __name__ == "__main__":
    try:
        function_that_might_fail()
    except Exception as e:
        # Catch unhandled exceptions in production
        logger.error("Unhandled exception: %s", e)
        # Log the stack trace explicitly using traceback module (optional)
        logger.error("Stack trace: %s", traceback.format_exc())
