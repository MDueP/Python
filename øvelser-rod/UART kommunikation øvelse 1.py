from machine improt UART
uart2 = UART(2, baudrate=9600)

uart2.write('hello')
