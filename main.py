from src.utils import setup_logger
from src.bronze import run_bronze
from src.silver import run_silver
from src.gold import run_gold
from src.loyalty import run_loyalty_engine


def main():
    setup_logger()
    run_bronze()
    run_silver()
    run_gold()
    run_loyalty_engine()

if __name__ == "__main__":
    main()