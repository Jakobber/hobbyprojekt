import terminal_wrapper 

def main():
    op = terminal_wrapper.start()
    if op == 1:
        terminal_wrapper.automail()
    elif op == 2:
        terminal_wrapper.check_balance()
    elif op == 3:
        terminal_wrapper.get_transaction_since()

if __name__ =="__main__":
    main()