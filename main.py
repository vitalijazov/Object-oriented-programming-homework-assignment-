from logging_utils import setup_logger
from logging_utils import get_logger
from mathematical_operations import mathematical_operations
from operations import division_by_zero 


# докончить пателны проектирования




def main():
      global a
      global b
      setup_logger()
      logger = get_logger('calculator')

      logger.info("Калькулятор запущен.")

      logger.info("ОТВЕТ:")

      division_by_zero()
      mathematical_operations()
      



if __name__ == "__main__":
   main()


