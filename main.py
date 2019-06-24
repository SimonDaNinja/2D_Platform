if __name__ == '__main__':
    while True:
        yn = input('do you want periodic boundaries? [y/n] ').lower()
        if yn == 'y' or yn == 'n':
            break
        else:
            print('invalid response')
    import example_stage
    if yn == 'y':
        example_stage.stage.isPeriodic = True
    if yn == 'n':
        example_stage.stage.isPeriodic = False

    example_stage.stage.Run()
