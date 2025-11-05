import terminal_wrapper 

def main():
    op = terminal_wrapper.start()
    if op == 1:
        terminal_wrapper.automail()
    elif op == 2:
        terminal_wrapper.check_balance()
    

if __name__ =="__main__":
    main()
