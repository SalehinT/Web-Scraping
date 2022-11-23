import teiki_jobs

options = int(input('1. Teiki 2. Spot 3. Full-Time\n'))

match options:
    case 1:
        teiki_jobs.teiki()
    case 2:
        pass
    case 3:
        pass
    case _:
        print('___')
