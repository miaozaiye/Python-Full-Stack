def trans_headline(head_line):

    b = ''
    print ('head_line in trans is :',head_line.split('%20'))
    for A in head_line.split('%20'):
        b = b+A+" "

    print (b)

    return (b.strip(' '))