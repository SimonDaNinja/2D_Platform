if __name__ == '__main__':
    choice = ''
    while True:
        choice = input('do you want the small stage [1] or the big stage [2]? ')
        if (choice == '1') or (choice == '2'):
            break
        else:
            print('Invalid response!')
    if choice == '1':
        import example_stage as stage
    elif choice == '2':
        import new_stage as stage
    else:
        print('Something went wrong!')
        exit()
    stage.stage.Run()
